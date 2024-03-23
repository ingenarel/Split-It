@echo off

setlocal enabledelayedexpansion

set "source_folder=%folder_name%\noise"

echo Please wait till i split the Noise files... ^>.^<

set count=0
set folder_count=1

mkdir "Destination\!folder_count!\%folder_name%\noise"

for %%F in ("%source_folder%\*") do (
    set /a count+=1
    
    rem Copy files to the current destination folder
    xcopy "%%F" "Destination\!folder_count!\%folder_name%\noise" >nul
    
    rem If specified number of files are copied, reset the file counter and move to the next destination folder
    if !count! equ %file_count% (
        set count=0
        set /a folder_count+=1
        mkdir "Destination\!folder_count!\%folder_name%\noise" >nul
    )
)

echo Noise files copy pasted successfully.
