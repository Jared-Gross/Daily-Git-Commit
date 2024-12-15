@echo off
cd "%~dp0"

:: Check if Python is in PATH
python --version >nul 2>&1
if %errorlevel%==0 (
    set "PYTHON_EXEC=python"
) else (
    echo Python is not in the PATH. Attempting to use a default installation...
    set "PYTHON_EXEC=%LOCALAPPDATA%\Programs\Python\Python38\python.exe"
    "%PYTHON_EXEC%" --version >nul 2>&1
    if %errorlevel%==9009 (
        echo Python not found. Please ensure Python is installed and accessible.
        pause
        exit /b
    )
)

:: Check if required packages are installed
echo Checking if required Python packages are installed...
"%PYTHON_EXEC%" -m pip show GitPython >nul 2>&1
if %errorlevel% neq 0 goto INSTALL_REQUIREMENTS
"%PYTHON_EXEC%" -m pip show PyYAML >nul 2>&1
if %errorlevel% neq 0 goto INSTALL_REQUIREMENTS

goto RUN_MAIN

:INSTALL_REQUIREMENTS
echo Required packages are missing. Installing from requirements.txt...
"%PYTHON_EXEC%" -m pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo Failed to install required packages. Please check your Python and pip setup.
    pause
    exit /b
)

:RUN_MAIN
echo Running the main script...
"%PYTHON_EXEC%" main.py
