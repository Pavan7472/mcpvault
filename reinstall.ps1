Stop-Process -Name "python" -Force -ErrorAction SilentlyContinue
Stop-Process -Name "mcpv" -Force -ErrorAction SilentlyContinue

# 1. 패키지 재설치 (라이브러리 업데이트)
uv pip install . --system --reinstall


# python -m mcpv install --force
