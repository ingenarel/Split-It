@echo off
setlocal enabledelayedexpansion

:noise
    set /p "noise_folder=Do you have a Noise folder? y if yes n if no: "
    if "!noise_folder!" == "y" (
        call :noise_split_
        exit /b
    ) else if "!noise_folder!" == "n" (
        exit /b
    ) else (
        echo "Error. please use either y or n"
        goto noise
    )

:noise_split_
    
    set /p "noise_split=Do you want to split it? if it has files then you should. y if yes n if no: "
    
    if  "!noise_split!" == "y" (
        call noise_splitter.bat
        exit /b
    
    ) else if "!noise_split!" == "n" (
        
        call noise_duplicator.bat
        exit /b
    
    ) else (
        echo "Error. please use either y or n"
        goto noise_split_
    )

    exit /b