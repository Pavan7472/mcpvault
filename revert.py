import os
import re

# ==========================================
# [설정 영역]
# 이전에 convert.py로 생성한 백업 파일명을 입력하세요.
# ==========================================
BACKUP_FILE = "mcpv_Full_Code.md"
# ==========================================

def normalize_content(content):
    """
    비교를 위해 줄바꿈 문자를 통일하고 양끝 공백을 제거합니다.
    """
    if content is None:
        return ""
    return content.replace('\r\n', '\n').strip()

def restore_if_changed():
    if not os.path.exists(BACKUP_FILE):
        print(f"❌ Error: 백업 파일 '{BACKUP_FILE}'을 찾을 수 없습니다.")
        return

    print(f"📂 Reading backup file: {BACKUP_FILE}...")
    
    with open(BACKUP_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()

    current_file = None
    content_lines = []
    in_code_block = False
    
    # 정규식: "## File: 경로" 패턴 매칭
    file_pattern = re.compile(r"^## File: (.+)")
    
    updated_count = 0
    skipped_count = 0
    new_file_count = 0

    for line in lines:
        # 1. 파일 경로 헤더 찾기
        match = file_pattern.match(line)
        if match:
            current_file = match.group(1).strip()
            content_lines = []
            in_code_block = False
            continue

        # 2. 코드 블록 시작 (```extension)
        if line.strip().startswith("```") and not in_code_block:
            if current_file:
                in_code_block = True
                content_lines = [] # 버퍼 초기화
            continue

        # 3. 코드 블록 끝 (```) -> 파일 저장 및 비교 로직 수행
        if line.strip() == "```" and in_code_block:
            if current_file:
                # 현재까지 모은 내용 합치기 (마지막 줄바꿈 처리 주의)
                backup_content = "".join(content_lines)
                
                # 로컬 경로 설정
                full_path = os.path.join(".", current_file)
                dir_name = os.path.dirname(full_path)
                
                # 폴더가 없으면 생성
                if dir_name and not os.path.exists(dir_name):
                    os.makedirs(dir_name, exist_ok=True)

                # 로컬 파일 읽기 (비교용)
                local_content = None
                if os.path.exists(full_path):
                    try:
                        with open(full_path, "r", encoding="utf-8") as lf:
                            local_content = lf.read()
                    except Exception:
                        local_content = None # 바이너리거나 읽기 실패 시

                # 비교 로직 (정규화 후 비교)
                if local_content is None:
                    # 파일이 없으면 생성
                    action = "NEW"
                elif normalize_content(local_content) != normalize_content(backup_content):
                    # 내용이 다르면 덮어쓰기
                    action = "UPDATE"
                else:
                    # 내용이 같으면 스킵
                    action = "SKIP"

                # 실제 쓰기 작업
                if action in ["NEW", "UPDATE"]:
                    try:
                        with open(full_path, "w", encoding="utf-8") as out_f:
                            out_f.write(backup_content)
                        
                        if action == "NEW":
                            print(f"✨ [생성] {current_file}")
                            new_file_count += 1
                        else:
                            print(f"✏️  [변경] {current_file}")
                            updated_count += 1
                    except Exception as e:
                        print(f"❌ [실패] {current_file}: {e}")
                else:
                    # print(f"💨 [스킵] {current_file}") # 너무 많으면 주석 처리
                    skipped_count += 1
                
                # 상태 초기화
                in_code_block = False
                current_file = None 
            continue

        # 4. 코드 블록 내부 내용 수집
        if in_code_block:
            content_lines.append(line)

    print("-" * 40)
    print(f"🎉 복원 완료 요약")
    print(f"   - 새로 생성됨: {new_file_count}개")
    print(f"   - 내용 변경됨: {updated_count}개")
    print(f"   - 변경 없음 (스킵): {skipped_count}개")
    print("-" * 40)

if __name__ == "__main__":
    restore_if_changed()