import os
import subprocess
import logging
import sys
from pathlib import Path
from fastmcp import FastMCP
from .valve import valve
from .vault import manager

# 1. 로깅 설정 (로그 파일 위치: ~/.gemini/antigravity/mcpv_debug.log)
LOG_DIR = Path.home() / ".gemini" / "antigravity"
try:
    LOG_DIR.mkdir(parents=True, exist_ok=True)
except:
    pass

LOG_FILE = LOG_DIR / "mcpv_debug.log"

# 기존 핸들러 제거 (중복 방지)
root_logger = logging.getLogger()
if root_logger.handlers:
    for handler in root_logger.handlers:
        root_logger.removeHandler(handler)

logging.basicConfig(
    filename=str(LOG_FILE),
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    encoding="utf-8",
    force=True
)
logger = logging.getLogger("mcpv-server")

# 2. 실행 위치 감지 및 로그
ROOT_DIR = Path.cwd()
logger.info("="*40)
logger.info(f"🚀 MCPV Server Started.")
logger.info(f"📂 Current Working Directory (ROOT_DIR): {ROOT_DIR}")
logger.info("="*40)

IGNORE_DIRS = {".git", "node_modules", "venv", ".venv", "__pycache__", "dist", "build"}
ALLOWED_EXTENSIONS = {".py", ".js", ".ts", ".md", ".json", ".txt", ".html", ".css", ".java", ".c", ".cpp", ".rs", ".go"}

mcp = FastMCP("mcpv", log_level="DEBUG")

@mcp.tool()
def get_initial_context(force: bool = False) -> str:
    """[Smart Valve] Loads the codebase context via Repomix. Blocks redundant calls."""
    logger.info(f"Function 'get_initial_context' called. force={force}")
    
    # 1. 밸브 체크
    allowed, msg = valve.check(force)
    logger.info(f"Valve check result: allowed={allowed}")
    
    if not allowed:
        logger.info("⛔ Request blocked by Smart Valve.")
        return msg

    try:
        # 2. Repomix 명령어 준비
        cmd = [
            "npx", "-y", "repomix",
            "--style", "xml",
            "--compress",
            "--remove-comments",
            "--output", "stdout"
        ]
        
        logger.info(f"▶️ Executing command: {' '.join(cmd)}")
        logger.info(f"   in Directory: {ROOT_DIR}")
        
        # 환경변수 설정 (CI=true로 설정하여 대화형 프롬프트 방지)
        env = os.environ.copy()
        env["CI"] = "true"
        
        # 3. 실행 (Timeout 60초 설정)
        result = subprocess.run(
            cmd,
            cwd=ROOT_DIR,
            capture_output=True,
            text=True,
            encoding="utf-8",
            shell=(os.name == 'nt'),
            timeout=60,  # 60초 지나면 강제 종료
            env=env
        )
        
        logger.info(f"✅ Command finished. Return code: {result.returncode}")
        
        if result.returncode != 0:
            err_msg = f"Repomix Error (Code {result.returncode}): {result.stderr}"
            logger.error(err_msg)
            return err_msg
            
        output_len = len(result.stdout)
        logger.info(f"📝 Context fetched successfully! Length: {output_len} chars")
        
        return f"=== Vault Context ===\n{result.stdout}\n=== End Vault ==="
        
    except subprocess.TimeoutExpired:
        logger.error("⏰ Repomix timed out after 60 seconds.")
        return "Error: Context fetching timed out (Repomix took too long). The project folder might be too large, or npx is hanging."
        
    except Exception as e:
        logger.exception("❌ Unexpected error in get_initial_context")
        return f"Vault Error: {str(e)}"

@mcp.tool()
async def use_upstream_tool(server_name: str, tool_name: str, args: dict = {}) -> str:
    """Routes a command to a specific server in the vault."""
    logger.info(f"Routing tool: {server_name} -> {tool_name}")
    try:
        session = await manager.get_session(server_name)
        res = await session.call_tool(tool_name, args)
        return "\n".join([c.text for c in res.content if c.type == "text"])
    except Exception as e:
        logger.error(f"Gateway Error: {e}")
        return f"Gateway Error: {e}"

@mcp.tool()
def list_directory(path: str = ".") -> str:
    """Secure, Lazy file listing."""
    logger.debug(f"list_directory called: {path}")
    full = (ROOT_DIR / path).resolve()
    if not str(full).startswith(str(ROOT_DIR)): return "⛔ Access Denied (Jailbreak attempt)"
    if not full.exists(): return "Not found"
    
    out = []
    try:
        with os.scandir(full) as it:
            for e in it:
                if e.name in IGNORE_DIRS or e.name.startswith("."): continue
                if e.is_dir(): out.append(f"[DIR]  {e.name}/")
                elif e.is_file() and Path(e.name).suffix in ALLOWED_EXTENSIONS: out.append(f"[FILE] {e.name}")
    except Exception as e:
        logger.error(f"list_directory error: {e}")
        return str(e)
    return "\n".join(sorted(out)) if out else "Empty"

@mcp.tool()
def read_file(path: str) -> str:
    """Secure file reader."""
    logger.debug(f"read_file called: {path}")
    full = (ROOT_DIR / path).resolve()
    if not str(full).startswith(str(ROOT_DIR)): return "⛔ Access Denied"
    if full.suffix not in ALLOWED_EXTENSIONS: return f"⛔ File type {full.suffix} not allowed in Vault"
    try: return full.read_text(encoding="utf-8", errors="replace")
    except Exception as e:
        logger.error(f"read_file error: {e}")
        return str(e)