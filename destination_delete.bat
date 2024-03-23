@echo off

set folder_name=Destination

if exist "%folder_name%" (
    rmdir /s /q "%folder_name%" >nul 2>&1
    echo Folder "%folder_name%" and its contents deleted successfully.
) else (
    exit /b
)