@echo off

setlocal enabledelayedexpansion

echo Please wait till i zip the files... ^>.^<

rem Set the path to the destination folder (relative to the script location)
set "destination_folder=.\Destination"

rem Change directory to the destination folder
cd /d "%~dp0%destination_folder%"

rem Loop through each folder in the destination folder
for /d %%i in (*) do (
    rem Get the name of the current folder
    set "folder_name=%%~nxi"
    
    rem Create a zip file with the same name as the folder using PowerShell
    powershell -Command "& {Add-Type -AssemblyName System.IO.Compression.FileSystem; [System.IO.Compression.ZipFile]::CreateFromDirectory('.\!folder_name!', '.\!folder_name!.zip');}"
    echo A folder was just zipped...
    echo Please wait till I zip the next folder...
    rem i don't know what the fuck chatgpt did to actually generate the upper line but it seemed to work on the first try. however because i'm an idiot and i only know batch scripts and not powershell i can't quite figure it out. would be nice if somebody explained this whole shit to me.
)

echo All folders zipped successfully.
