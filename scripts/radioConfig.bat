
@echo off
setlocal

if "%~1"=="" (
    echo Usage: %~nx0 suffix key
    exit /b 1
)

if "%~2"=="" (
    echo Usage: %~nx0 suffix key
    exit /b 1
)

set "suffix=%~1"
set "key=%~2"

curl -X POST "http://192.168.69.1/configuration" ^
  -H "Content-Type: application/json" ^
  -d "{\"mode\":\"TEAM_ROBOT_RADIO\",\"teamNumber\":4561,\"wpaKey6\":\"%key%\",\"wpaKey24\":\"%key%\"}"

endlocal