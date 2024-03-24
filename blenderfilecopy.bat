@echo off

:ask_for_filename

setlocal enabledelayedexpansion

set /p "filename=Enter the name of the blend file that you want to copy (with extension): "
set "source_file=%cd%\%filename%"
set "destination_folder=.\destination"

set "fileExists="
for %%F in ("%cd%\*") do (
    if "%%~nxF" equ "%filename%" (
        set "fileExists=true"
        goto :found
    )
)

:found
if defined fileExists (
    echo Please wait till I copy the blend files... ^>.^<

    for /D %%G in ("%destination_folder%\*") do (
        xcopy "%source_file%" "%%G\"
    )
    echo all blend files copied.
    pause
) else (
    call error_msg.bat
    goto ask_for_filename
)