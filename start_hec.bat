@echo off
echo Stopping all Python processes...
taskkill /F /IM python.exe 2>nul
timeout /t 2 >nul

echo.
echo Starting HEC System Services...
echo.

echo [1/3] Starting API Server...
start "HEC API" cmd /k "cd hec-core && python -m uvicorn api.main:app --port 8000"
timeout /t 3 >nul

echo [2/3] Starting Simulation Driver...
start "HEC Simulation" cmd /k "set PYTHONIOENCODING=utf-8 && python hec-core/genesis_driver.py"
timeout /t 2 >nul

echo [3/3] Starting Dashboard...
start "HEC Dashboard" cmd /k "cd hec-dashboard && npm run dev"

echo.
echo ===================================
echo All services started!
echo ===================================
echo.
echo Dashboard: http://localhost:5173
echo API: http://127.0.0.1:8000
echo.
pause
