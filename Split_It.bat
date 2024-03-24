@echo off

title Split It! version 0.2 (beta testing)

:start
    call start.bat

:please_enter_your_simulation_folder_name

    echo  ____   _                                        _
    echo ^|  _ \ ^| ^|  ___   __ _  ___   ___    ___  _ __  ^| ^|_  ___  _ __   _   _   ___   _   _  _ __
    echo ^| ^|_) ^|^| ^| / _ \ / _` ^|/ __^| / _ \  / _ \^| '_ \ ^| __^|/ _ \^| '__^| ^| ^| ^| ^| / _ \ ^| ^| ^| ^|^| '__^|
    echo ^|  __/ ^| ^|^|  __/^| (_^| ^|\__ \^|  __/ ^|  __/^| ^| ^| ^|^| ^|_^|  __/^| ^|    ^| ^|_^| ^|^| (_) ^|^| ^|_^| ^|^| ^|
    echo ^|_^|    ^|_^| \___^| \__,_^|^|___/ \___^|  \___^|^|_^| ^|_^| \__^|\___^|^|_^|     \__, ^| \___/  \__,_^|^|_^|
    echo       _                    _         _    _                  __   ^|___/ _      _
    echo  ___ (_) _ __ ___   _   _ ^| ^|  __ _ ^| ^|_ (_)  ___   _ __    / _^|  ___  ^| ^|  __^| ^|  ___  _ __   _ __    __ _  _ __ ___    ___
    echo / __^|^| ^|^| '_ ` _ \ ^| ^| ^| ^|^| ^| / _` ^|^| __^|^| ^| / _ \ ^| '_ \  ^| ^|_  / _ \ ^| ^| / _` ^| / _ \^| '__^| ^| '_ \  / _` ^|^| '_ ` _ \  / _ \
    echo \__ \^| ^|^| ^| ^| ^| ^| ^|^| ^|_^| ^|^| ^|^| (_^| ^|^| ^|_ ^| ^|^| (_) ^|^| ^| ^| ^| ^|  _^|^| (_) ^|^| ^|^| (_^| ^|^|  __/^| ^|    ^| ^| ^| ^|^| (_^| ^|^| ^| ^| ^| ^| ^|^|  __/
    echo ^|___/^|_^|^|_^| ^|_^| ^|_^| \__,_^|^|_^| \__,_^| \__^|^|_^| \___/ ^|_^| ^|_^| ^|_^|   \___/ ^|_^| \__,_^| \___^|^|_^|    ^|_^| ^|_^| \__,_^|^|_^| ^|_^| ^|_^| \___^|

:get_folder_name
    setlocal enabledelayedexpansion

    set /p "folder_name=REMEMBER I MADE IT CASE SENSITIVE: "

    for /f "delims=" %%A in ('dir /ad /b') do (
        
        if "%%A"=="!folder_name!" (
        
            call success_msg.bat
            set /p "file_count=Enter the number of files to copy into each folder (use numerical values only or it won't work): "
            call config_splitter.bat
            call data_splitter.bat
            call mesh_splitter.bat
            call guiding_conf.bat
            call noise_conf.bat
            call particles_conf.bat
            call end.bat
            exit /b
        
        ) else if "!folder_name!" == "cls" (
        
            cls
            goto start
        
        ) else if "!folder_name!" == "clear" (
        
            cls
            goto start
        
        )
    )

    call error_msg.bat
    goto get_folder_name

    :end
    exit /b
