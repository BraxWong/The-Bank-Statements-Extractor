@echo off
setlocal

set VENV_DIR=%USERPROFILE%\myenv

python -m venv "%VENV_DIR%"

powershell -NoProfile -Command "$PSVersionTable.PSEdition" > "%TEMP%\ps_check.tmp" 2>&1

findstr /I /C:"Core" /C:"Desktop" "%TEMP%\ps_check.tmp" >nul 2>&1

if %errorlevel% equ 0 (
    powershell -ExecutionPolicy Bypass -File "%VENV_DIR%\Scripts\Activate.ps1"
) else (
    call "%VENV_DIR%\Scripts\activate.bat"
)

python ../src/main.py