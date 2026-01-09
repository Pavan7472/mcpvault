import os
import subprocess
import shutil
import fnmatch
import stat

# ==========================================
# [설정 영역] 여기에 정보를 입력하세요
# ==========================================
GITHUB_PAT = ""  # 사용자의 PAT (비워두면 실행 시 입력받음)
REPO_URL = "https://github.com/thekeunpie-hash/mcpvault"
OUTPUT_FILE = "mcpv_Full_Code.md"

IGNORE_PATTERNS = [
    # 1. 시스템 및 설정 디렉토리
    ".git", "node_modules", "__pycache__", "dist", "build", ".next", ".vercel",
    ".venv", "venv", ".idea", ".vscode", "coverage", ".DS_Store", "Archives",
    
    # 2. 락 파일
    "package-lock.json", "pnpm-lock.yaml", "yarn.lock",
    
    # 3. 이미지 및 미디어
    "*.png", "*.jpg", "*.jpeg", "*.gif", "*.ico", "*.svg", "*.webp",
    "*.mp4", "*.mp3", "*.wav",
    
    # 4. 폰트
    "*.eot", "*.ttf", "*.woff", "*.woff2", "*.otf",
    
    # 5. 바이너리, 압축, 데이터 모델
    "*.pdf", "*.zip", "*.gguf", "*.bin", "*.exe", "*.gz", "*.tar", 
    "*.pkl", "*.pt", "*.pth",
    
    # 6. 제외할 텍스트/스크립트/문서 (프로토타입 html, 배치파일 등 포함)
    
    # 7. 특정 파일명 (변환 도구, 복구 도구, 보안 키, 중복 코드 등)
    "convert.py",
    "restore_diff.py",
    "mcpv_Full_Code.txt", "mcpv_Slim_Code.txt"
]
# ==========================================

def remove_readonly(func, path, _):
    """Windows에서 삭제 불가 파일 강제 삭제"""
    os.chmod(path, stat.S_IWRITE)
    func(path)

def clone_repo(repo_url, pat, target_dir):
    if os.path.exists(target_dir):
        shutil.rmtree(target_dir, onerror=remove_readonly)

    auth_url = repo_url.replace("https://", f"https://{pat}@")

    print(f"📥 Cloning repository...")
    try:
        subprocess.run(["git", "clone", "--depth", "1", auth_url, target_dir], check=True)
        print("✅ Clone successful.")
    except subprocess.CalledProcessError:
        print("❌ Clone failed. Check your PAT or URL.")
        exit(1)

def is_ignored(path, names):
    ignored = set()
    for name in names:
        for pattern in IGNORE_PATTERNS:
            if fnmatch.fnmatch(name, pattern):
                ignored.add(name)
                break
    return ignored

def merge_files(source_dir, output_file):
    print(f"🔄 Merging files into {output_file}...")

    with open(output_file, "w", encoding="utf-8") as outfile:
        outfile.write(f"# Repository Dump: {REPO_URL}\n\n")
        outfile.write("This document contains the full source code of the repository.\n")
        outfile.write("Each file is denoted by a header showing its path.\n\n")

        for root, dirs, files in os.walk(source_dir):
            dirs[:] = [d for d in dirs if not any(fnmatch.fnmatch(d, p) for p in IGNORE_PATTERNS)]

            for file in files:
                if any(fnmatch.fnmatch(file, p) for p in IGNORE_PATTERNS):
                    continue

                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, source_dir)

                try:
                    with open(file_path, "r", encoding="utf-8") as infile:
                        content = infile.read()

                        outfile.write(f"## File: {relative_path}\n")
                        outfile.write(f"```{os.path.splitext(file)[1].replace('.', '')}\n")
                        outfile.write(content)
                        outfile.write("\n```\n\n---\n\n")

                        print(f"📄 Added: {relative_path}")
                except UnicodeDecodeError:
                    print(f"⚠️ Skipped (Binary): {relative_path}")
                except Exception as e:
                    print(f"❌ Error reading {relative_path}: {e}")

def main():
    temp_dir = "temp_repo_clone"

    pat = GITHUB_PAT
    if not pat:
        pat = input("GitHub PAT를 입력하세요: ").strip()

    try:
        clone_repo(REPO_URL, pat, temp_dir)
        merge_files(temp_dir, OUTPUT_FILE)
        print(f"\n🎉 Complete! File saved as: {os.path.abspath(OUTPUT_FILE)}")
    finally:
        if os.path.exists(temp_dir):
            try:
                shutil.rmtree(temp_dir, onerror=remove_readonly)
            except:
                pass

if __name__ == "__main__":
    main()