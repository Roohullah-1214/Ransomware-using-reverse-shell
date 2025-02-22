@echo off
:: Ensure the script paths are correct

:: Run transfer.bat from the same directory as this script
call "%~dp0transfer.bat"

:: Start the shell executable from the current directory
::start "%~dp0shell.exe"