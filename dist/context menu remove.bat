@echo off&(cd/d "%~dp0")&(cacls "%SystemDrive%\System Volume Information" >nul 2>&1)||(start "" mshta vbscript:CreateObject^("Shell.Application"^).ShellExecute^("%~snx0"," %*","","runas",1^)^(window.close^)&exit /b)

REG DELETE "HKEY_CLASSES_ROOT\*\shell\PixivUgoiraToWebm" /f

REG DELETE "HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Explorer\CommandStore\shell\PixivUgoiraToWebm.0" /f

REG DELETE "HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Explorer\CommandStore\shell\PixivUgoiraToWebm(IfEndsJump).1" /f

PAUSE
exit