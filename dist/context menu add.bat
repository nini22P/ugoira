@echo off&(cd/d "%~dp0")&(cacls "%SystemDrive%\System Volume Information" >nul 2>&1)||(start "" mshta vbscript:CreateObject^("Shell.Application"^).ShellExecute^("%~snx0"," %*","","runas",1^)^(window.close^)&exit /b)

REG ADD "HKEY_CLASSES_ROOT\*\shell\PixivUgoiraToWebm" /v MUIVerb /t REG_SZ /d "Pixiv Ugoira To Webm" /f

REG ADD "HKEY_CLASSES_ROOT\*\shell\PixivUgoiraToWebm" /v SubCommands /t REG_SZ /d "PixivUgoiraToWebm.0;PixivUgoiraToWebm(IfEndsJump).1" /f

REG ADD "HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Explorer\CommandStore\shell\PixivUgoiraToWebm.0" /t REG_SZ /d "Pixiv Ugoira To Webm" /f

REG ADD "HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Explorer\CommandStore\shell\PixivUgoiraToWebm.0\command" /t REG_SZ /d ""%~dp0\"Pixiv Ugoira To Webm.bat %%1" /f

REG ADD "HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Explorer\CommandStore\shell\PixivUgoiraToWebm(IfEndsJump).1" /t REG_SZ /d "Pixiv Ugoira To Webm (If Ends Jump)" /f

REG ADD "HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Explorer\CommandStore\shell\PixivUgoiraToWebm(IfEndsJump).1\command" /t REG_SZ /d ""%~dp0\"Pixiv Ugoira To Webm(If Ends Jump).bat %%1" /f

PAUSE
exit