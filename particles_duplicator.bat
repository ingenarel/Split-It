@echo off

setlocal enabledelayedexpansion

set "source_folder=%folder_name%\config"

echo Please wait till I make the Particles folders... ^>.^<

set count=0

set folder_count=1

mkdir "Destination\!folder_count!\%folder_name%\config" >nul 2>nul


for %%F in ("%source_folder%\*") do (
    set /a count+=1 
    
    rem Create a folder called "particles" in the current destination folder
    mkdir "Destination\!folder_count!\%folder_name%\particles" >nul 2>nul

    
    rem If specified number of folders are created, reset the folder counter and move to the next destination folder
    if !count! equ %file_count% (
        set count=0
        set /a folder_count+=1
        mkdir "Destination\!folder_count!\%folder_name%\" >nul 2>nul
    )
)

echo "Particles" folders created successfully.

exit /b