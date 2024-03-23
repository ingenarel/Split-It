@echo off
setlocal enabledelayedexpansion

:particles
    set /p "particles_folder=Do you have a Particles folder? y if yes n if no: "
    if "!particles_folder!" == "y" (
        call :particles_split_
        exit /b
    ) else if "!particles_folder!" == "n" (
        exit /b
    ) else (
        echo "Error. please use either y or n"
        goto particles
    )

:particles_split_
    
    set /p "particles_split=Do you want to split it? if it has files then you should. y if yes n if no: "
    
    if  "!particles_split!" == "y" (
        call particles_splitter.bat
        exit /b
    
    ) else if "!particles_split!" == "n" (
        
        call particles_duplicator.bat
        exit /b
    
    ) else (
        echo "Error. please use either y or n"
        goto particles_split_
    )

    exit /b