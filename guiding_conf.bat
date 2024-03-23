@echo off
setlocal enabledelayedexpansion

:guiding
    set /p "guiding_folder=Do you have a guiding folder? y if yes n if no: "
    if "!guiding_folder!" == "y" (
        call :guiding_split_
        exit /b
    ) else if "!guiding_folder!" == "n" (
        exit /b
    ) else (
        echo "Error. please use either y or n"
        goto guiding
    )

:guiding_split_
    
    set /p "guiding_split=Do you want to split it? if it has files then you should. y if yes n if no: "
    
    if  "!guiding_split!" == "y" (
        call guiding_splitter.bat
        exit /b
    
    ) else if "!guiding_split!" == "n" (
        
        call guiding_duplicator.bat
        exit /b
    
    ) else (
        echo "Error. please use either y or n"
        goto guiding_split_
    )

    exit /b