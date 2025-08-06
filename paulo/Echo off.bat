@echo off
setlocal
set PATH=%CD%;%PATH%
set LIBGL_ALWAYS_SOFTWARE=1
python "apptaludes - 16_07.py"
endlocal