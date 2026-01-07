import json
import sys
import shutil
import os
from pathlib import Path
from mcp.client.session import ClientSession
from mcp.client.stdio import stdio_client
from contextlib import AsyncExitStack

# [Import 호환성 처리]
try:
    from mcp.types import StdioServerParameters
except ImportError:
    try:
        from mcp import StdioServerParameters
    except ImportError:
        from typing import Any
        StdioServerParameters = Any

# 경로 설정
HOME_DIR = Path.home()
CONFIG_DIR = HOME_DIR / ".gemini" / "antigravity"
CONFIG_FILE = CONFIG_DIR / "mcp_config.json"
BACKUP_FILE = CONFIG_DIR / "mcp_config.original.json"
MY_SERVER_NAME = "mcpv-proxy"

# 안티그래비티 경로
ANTIGRAVITY_PATH = Path(os.environ["LOCALAPPDATA"]) / "Programs" / "Antigravity"
ANTIGRAVITY_EXE = ANTIGRAVITY_PATH / "Antigravity.exe"
BOOSTER_SCRIPT = CONFIG_DIR / "boost_launcher.bat"

class VaultManager:
    def __init__(self):
        self.stack = AsyncExitStack()
        self.sessions = {}

    def install(self, force: bool = False):
        """1. MCP Config 하이재킹"""
        success = self._hijack_config(force)
        if success:
            """2. 부스팅 스크립트 설치"""
            self._install_booster()
            print("✨ Installation complete. Please restart Antigravity using the new Desktop Shortcut!")

    def link(self):
        """[New] 현재 폴더를 Vault의 작업 경로(CWD)로 강제 연결합니다."""
        if not CONFIG_FILE.exists():
             print("❌ Config file not found. Run 'mcpv install' first.", file=sys.stderr)
             return

        try:
            with open(CONFIG_FILE, "r", encoding="utf-8") as f: config = json.load(f)
        except Exception as e:
            print(f"❌ Config file is corrupted: {e}", file=sys.stderr)
            return

        servers = config.get("mcpServers", {})
        if MY_SERVER_NAME not in servers:
             print("❌ mcpv-proxy not found in config. Run 'mcpv install' first.", file=sys.stderr)
             return
        
        # [핵심] CWD를 현재 명령어를 실행한 위치로 업데이트
        current_cwd = os.getcwd()
        servers[MY_SERVER_NAME]["cwd"] = current_cwd
        
        # 저장
        with open(CONFIG_FILE, "w", encoding="utf-8") as f:
             json.dump(config, f, indent=2)
             
        print(f"🔗 Vault target linked to: {current_cwd}", file=sys.stderr)
        print("👉 Please restart Antigravity to apply changes.", file=sys.stderr)

    def _hijack_config(self, force: bool) -> bool:
        if not CONFIG_DIR.exists():
            try:
                CONFIG_DIR.mkdir(parents=True, exist_ok=True)
            except:
                print(f"❌ Config dir creation failed at {CONFIG_DIR}", file=sys.stderr)
                return False

        if not CONFIG_FILE.exists():
             with open(CONFIG_FILE, "w", encoding="utf-8") as f:
                json.dump({"mcpServers": {}}, f)

        try:
            with open(CONFIG_FILE, "r", encoding="utf-8") as f: config = json.load(f)
        except:
            config = {"mcpServers": {}}

        servers = config.get("mcpServers", {})
        
        if len(servers) == 1 and MY_SERVER_NAME in servers:
            # 이미 설치되어 있어도, install 명령 시 CWD는 갱신해주는 것이 사용자 경험에 좋음
            print("✅ mcpv middleware is active. Updating CWD...", file=sys.stderr)
            servers[MY_SERVER_NAME]["cwd"] = os.getcwd()
            with open(CONFIG_FILE, "w", encoding="utf-8") as f:
                json.dump(config, f, indent=2)
            return True

        if len(servers) == 1 and not force:
            print(f"⚠️  Only 1 MCP server found: {list(servers.keys())}", file=sys.stderr)
            print("   Skipping installation. Use 'mcpv install --force' to override.", file=sys.stderr)
            return False

        upstream = {k: v for k, v in servers.items() if k != MY_SERVER_NAME}
        if upstream:
            with open(BACKUP_FILE, "w", encoding="utf-8") as f:
                json.dump({"mcpServers": upstream}, f, indent=2)
            print(f"📦 Backup created at: {BACKUP_FILE}", file=sys.stderr)

        my_config = {
            "command": "mcpv",  # 전역 설치라면 PATH에 등록된 mcpv 사용
            "args": ["start"],
            "cwd": os.getcwd(), # 설치 시점의 경로
            "env": {"PYTHONUNBUFFERED": "1"}
        }
        
        with open(CONFIG_FILE, "w", encoding="utf-8") as f:
            json.dump({"mcpServers": {MY_SERVER_NAME: my_config}}, f, indent=2)
        print("🔒 Vault locked. Config updated.", file=sys.stderr)
        return True

    def _install_booster(self):
        print("🚀 Installing Booster Script...", file=sys.stderr)
        if not ANTIGRAVITY_PATH.exists():
             print(f"⚠️  Antigravity path not found. Skipping booster.", file=sys.stderr)
             return

        batch_content = f"""@echo off
set __COMPAT_LAYER=RunAsInvoker
cd /d "{ANTIGRAVITY_PATH}"
powershell -NoProfile -ExecutionPolicy Bypass -Command "Get-NetTCPConnection -LocalPort 26646 -ErrorAction SilentlyContinue | Stop-Process -Force -ErrorAction SilentlyContinue; $env:Path = 'C:\\Windows\\System32\\WindowsPowerShell\\v1.0;' + [System.Environment]::GetEnvironmentVariable('Path', 'Machine') + ';' + [System.Environment]::GetEnvironmentVariable('Path', 'User'); Start-Process -FilePath '.\\Antigravity.exe' -ArgumentList '--disable-gpu-driver-bug-workarounds --ignore-gpu-blacklist --enable-gpu-rasterization --enable-zero-copy --enable-native-gpu-memory-buffers' -WorkingDirectory '{ANTIGRAVITY_PATH}'"
exit
"""
        try:
            with open(BOOSTER_SCRIPT, "w", encoding="utf-8") as f:
                f.write(batch_content)
            self._create_shortcut_vbs(str(BOOSTER_SCRIPT), "Antigravity Boost (mcpv)", str(ANTIGRAVITY_EXE))
        except Exception as e:
            print(f"⚠️  Booster installation failed: {e}", file=sys.stderr)

    def _create_shortcut_vbs(self, target, name, icon):
        desktop = Path(os.environ["USERPROFILE"]) / "Desktop"
        link_path = desktop / f"{name}.lnk"
        vbs_script = f'''
            Set oWS = WScript.CreateObject("WScript.Shell")
            sLinkFile = "{link_path}"
            Set oLink = oWS.CreateShortcut(sLinkFile)
            oLink.TargetPath = "cmd.exe"
            oLink.Arguments = "/c ""{target}"""
            oLink.IconLocation = "{icon},0"
            oLink.WindowStyle = 7 
            oLink.Save
        '''
        vbs_file = CONFIG_DIR / "create_shortcut.vbs"
        try:
            with open(vbs_file, "w", encoding="utf-8") as f: f.write(vbs_script)
            os.system(f"cscript //nologo {vbs_file}")
            print(f"   ✨ Shortcut created on Desktop: {name}", file=sys.stderr)
        finally:
            if vbs_file.exists(): os.remove(vbs_file)

    async def get_session(self, server_name):
        if server_name in self.sessions: return self.sessions[server_name]
        if not BACKUP_FILE.exists(): raise FileNotFoundError("Vault is empty.")
        with open(BACKUP_FILE, "r") as f: config = json.load(f)
        srv = config["mcpServers"].get(server_name)
        if not srv: raise ValueError(f"Server {server_name} not found.")
        
        params = StdioServerParameters(command=srv["command"], args=srv.get("args", []), env=os.environ | srv.get("env", {}))
        read, write = await self.stack.enter_async_context(stdio_client(params))
        session = await self.stack.enter_async_context(ClientSession(read, write))
        await session.initialize()
        self.sessions[server_name] = session
        return session

    async def cleanup(self):
        await self.stack.aclose()

manager = VaultManager()