@echo off
setlocal disabledelayedexpansion

CHCP 65001 >NUL

echo  ________       ________    ___           ___      _________                ___      _________    ___
echo ^|\   ____\     ^|\   __  \  ^|\  \         ^|\  \    ^|\___   ___\             ^|\  \    ^|\___   ___\ ^|\  \
echo \ \  \___^|_    \ \  \^|\  \ \ \  \        \ \  \   \^|___ \  \_^|             \ \  \   \^|___ \  \_^| \ \  \
echo  \ \_____  \    \ \   ____\ \ \  \        \ \  \       \ \  \               \ \  \       \ \  \   \ \  \
echo   \^|____^|\  \    \ \  \___^|  \ \  \____    \ \  \       \ \  \               \ \  \       \ \  \   \ \__\
echo     ____\_\  \    \ \__\      \ \_______\   \ \__\       \ \__\               \ \__\       \ \__\   \^|__^|
echo    ^|\_________\    \^|__^|       \^|_______^|    \^|__^|        \^|__^|                \^|__^|        \^|__^|       ___ 
echo    \^|_________^|                                                                                        ^|\__\
echo                                                                                                        \^|__
echo.
echo     _                           _                              _                    _         _    _
echo    / \         ___  _   _  ___ ^| ^|_  ___   _ __ ___       ___ (_) _ __ ___   _   _ ^| ^|  __ _ ^| ^|_ (_)  ___   _ __
echo   / _ \       / __^|^| ^| ^| ^|/ __^|^| __^|/ _ \ ^| '_ ` _ \     / __^|^| ^|^| '_ ` _ \ ^| ^| ^| ^|^| ^| / _` ^|^| __^|^| ^| / _ \ ^| '_ \
echo  / ___ \     ^| (__ ^| ^|_^| ^|\__ \^| ^|_^| (_) ^|^| ^| ^| ^| ^| ^|    \__ \^| ^|^| ^| ^| ^| ^| ^|^| ^|_^| ^|^| ^|^| (_^| ^|^| ^|_ ^| ^|^| (_) ^|^| ^| ^| ^|
echo /_/   \_\     \___^| \__,_^|^|___/ \__^|\___/ ^|_^| ^|_^| ^|_^|    ^|___/^|_^|^|_^| ^|_^| ^|_^| \__,_^|^|_^| \__,_^| \__^|^|_^| \___/ ^|_^| ^|_^|
echo                    _                            _  _  _    _                    __                   ____   _                        ___  _        _
echo   ___  __ _   ___ ^| ^|__    ___      ___  _ __  ^| ^|(_)^| ^|_ ^| ^|_  ___  _ __      / _^|  ___   _ __     / ___^| ^| ^|__    ___   ___  _ __ ^|_ _^|^| ^|_     ^| ^|
echo  / __^|/ _` ^| / __^|^| '_ \  / _ \    / __^|^| '_ \ ^| ^|^| ^|^| __^|^| __^|/ _ \^| '__^|    ^| ^|_  / _ \ ^| '__^|    \___ \ ^| '_ \  / _ \ / _ \^| '_ \ ^| ^| ^| __^|    ^| ^|
echo ^| (__^| (_^| ^|^| (__ ^| ^| ^| ^|^|  __/    \__ \^| ^|_) ^|^| ^|^| ^|^| ^|_ ^| ^|_^|  __/^| ^|       ^|  _^|^| (_) ^|^| ^|        ___) ^|^| ^| ^| ^|^|  __/^|  __/^| ^|_) ^|^| ^| ^| ^|_     ^|_^|
echo  \___^|\__,_^| \___^|^|_^| ^|_^| \___^|    ^|___/^| .__/ ^|_^|^|_^| \__^| \__^|\___^|^|_^|       ^|_^|   \___/ ^|_^|       ^|____/ ^|_^| ^|_^| \___^| \___^|^| .__/^|___^| \__^|    (_)
echo                                         ^|_^|                                                                                   ^|_^|
echo.
echo.
echo  __  __               _            ____
echo ^|  \/  ^|   __ _    __^| ^|   ___    ^| __ )   _   _
echo ^| ^|\/^| ^|  / _` ^|  / _` ^|  / _ \   ^|  _ \  ^| ^| ^| ^|
echo ^| ^|  ^| ^| ^| (_^| ^| ^| (_^| ^| ^|  __/   ^| ^|_) ^| ^| ^|_^| ^|
echo ^|_^|  ^|_^|  \__,_^|  \__,_^|  \___^|   ^|____/   \__, ^|
echo                                            ^|___/
echo  ___   _   _    ____   _____   _   _      _      ____    _____   _
echo ^|_ _^| ^| \ ^| ^|  / ___^| ^| ____^| ^| \ ^| ^|    / \    ^|  _ \  ^| ____^| ^| ^|
echo  ^| ^|  ^|  \^| ^| ^| ^|  _  ^|  _^|   ^|  \^| ^|   / _ \   ^| ^|_) ^| ^|  _^|   ^| ^|
echo  ^| ^|  ^| ^|\  ^| ^| ^|_^| ^| ^| ^|___  ^| ^|\  ^|  / ___ \  ^|  _ ^<  ^| ^|___  ^| ^|___
echo ^|___^| ^|_^| \_^|  \____^| ^|_____^| ^|_^| \_^| /_/   \_\ ^|_^| \_\ ^|_____^| ^|_____^|
echo.
echo.
echo ________________________________________________________________________________________________________________________________________________
echo ^|:‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾:^|
echo ^|:   Wanna support me?                                                                                                                        :^|
echo ^|:                                                                                                                                            :^|
echo ^|:   SUPPORT THE SHEEPIT DEVS!!!! -                                                 https://www.sheepit-renderfarm.com/donation               :^|
echo ^|:                                                                                                                                            :^|
echo ^|:   Follow me on Instagram -                                                       https://www.instagram.com/saad_abdullah999666/            :^|
echo ^|:   Reddit account -                                                               https://reddit.com/user/INGENAREL                         :^|
echo ^|:   Discord -                                                                      ingenarel#2846                                            :^|
echo ^|:   My youtube channel -                                                           https://www.youtube.com/channel/UC90Tar8Bpx3Q8UqpM8qxWZw  :^|
echo ^|:   Sponsor me on SheepIt -                                                        https://www.sheepit-renderfarm.com/user/ingenarel/profile :^|
echo ^|:   Here's my public renderkey if you wanna connect a device to my account -       XQVDMUjdOKt7LBldxjuF0YERqLoGnExbeh8yUrce                  :^|
echo ^|:                                                                                                                                            :^|
echo ^|:____________________________________________________________________________________________________________________________________________:^|
echo ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
echo.
echo ________________________________________________________________________________________________________________________________________________________________________________
echo ^|:‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾:^|
echo ^|: ██████╗ ██╗███████╗ ██████╗██╗      █████╗ ██╗███╗   ███╗███████╗██████╗ ██╗██╗██╗                                                                                         :^|
echo ^|: ██╔══██╗██║██╔════╝██╔════╝██║     ██╔══██╗██║████╗ ████║██╔════╝██╔══██╗██║██║██║                                                                                         :^|
echo ^|: ██║  ██║██║███████╗██║     ██║     ███████║██║██╔████╔██║█████╗  ██████╔╝██║██║██║                                                                                         :^|
echo ^|: ██║  ██║██║╚════██║██║     ██║     ██╔══██║██║██║╚██╔╝██║██╔══╝  ██╔══██╗╚═╝╚═╝╚═╝                                                                                         :^|
echo ^|: ██████╔╝██║███████║╚██████╗███████╗██║  ██║██║██║ ╚═╝ ██║███████╗██║  ██║██╗██╗██╗                                                                                         :^|
echo ^|: ╚═════╝ ╚═╝╚══════╝ ╚═════╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝╚═╝                                                                                         :^|
echo ^|:                                                                                                                                                                            :^|
echo ^|: THIS IS JUST A TEST PROJECT! I'M JUST AN AMATEUR PROGRAMMER! I LEARNED TO CODE THIS WHILE I WAS ALSO CODING IT SO THERE MAY BE STILL SOME BUGS LEFT!!!                     :^|
echo ^|: THIS WILL ONLY WORK FOR FLUID CACHES ONLY! (As far as I know.. Haven't tested with others yet....)                                                                         :^|
echo ^|: This is because I only know how fluid cache files works and i haven't really worked it other simulations yet such as smoke and fire, particle systems...                   :^|
echo ^|: I'll eventually learn them too and then i'll try to upgrade it!                                                                                                            :^|
echo ^|: I'll also try to make a smart cache splitter where it will split the files based on their sizes.                                                                           :^|
echo ^|: But for now you will have to set how many splits you want to make.                                                                                                         :^|
echo ^|: If you have any suggestions and you know how to do it, I'll appreciate the help!                                                                                           :^|
echo ^|: I'm just a member of the SheepIt community i'm not a dev so if i make any errors it's my fault not theirs!                                                                 :^|
echo ^|: I'll also try to post this on github and make it open source too altho i'm kinda a noob at that too. :(                                                                    :^|
echo ^|:                                                                                                                                                                            :^|
echo ^|:____________________________________________________________________________________________________________________________________________________________________________:^|
echo ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
echo.
echo Tip: you can type cls or clear to restart
echo.
echo BEFORE YOU START THIS MAKE SURE THAT YOU HAVE DOUBLE THE EMPTY SPACE IN YOUR DRIVE AS YOUR BLEND AND CACHE FILE COMBINED!
echo THAT MEANS IF YOUR BLEND FILE IS 100 mb AND YOUR SIMULATION CACHE FOLDER IS 900 mb, MAKE SURE THAT YOU HAVE ATLEAST 2 gb OF EMPTY SPACE IN YOUR DRIVE! 
