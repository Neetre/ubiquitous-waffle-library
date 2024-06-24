@ECHO OFF

CALL ./setup/setup_Windows.bat

REM Change directory to 'bin' and run the application
CD /d bin
IF ERRORLEVEL 1 (
    ECHO Failed to change directory to 'bin'
    PAUSE
    EXIT /B 1
)


SET /P UserInput=LAN IP? (y/n):
IF /I "%UserInput%" EQU "y" GOTO AskIP
IF /I "%UserInput%" EQU "n" GOTO RunApp

:AskIP
python webpage.py --ip
IF ERRORLEVEL 1 (
    ECHO Failed to run webpage.py
    PAUSE
    EXIT /B 1
)
GOTO End

:RunApp
python webpage.py --local
IF ERRORLEVEL 1 (
    ECHO Failed to run webpage.py
    PAUSE
    EXIT /B 1
)

:End
PAUSE
EXIT /B 0