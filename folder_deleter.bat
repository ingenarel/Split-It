@echo off

set "folder=Destination"

rem Navigate to the Destination folder
cd /d "%~dp0%folder%" || exit /b

rem Prompt the user for confirmation

:folder_delete

    echo Do you want to delete delete the folders that were created when you split the project?
    echo The zip files wont be deleted just the folders and files that were created in order to make those zips.

    set /p choice=y if yes n if no: 

    rem Check the user's choice
    if /i "%choice%"=="y" (
        rem Loop through all items in the folder and delete them
        for /d %%i in (*) do (
            echo Deleting folder: "%%i"
            rd /s /q "%%i"
        )
        echo.
        echo All split cache folders deleted successfully.
        echo Don't worry chill the zips aren't deleted.

    ) else if "%choice%"=="n" (
        
        echo Operation cancelled. No folders have been deleted.
        exit /b

    ) else (

        echo "Error. please use either y or n"
        goto folder_delete

    )
