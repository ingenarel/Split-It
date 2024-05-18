def grettings():
    """
    This greets the user. it returns the greeting as a string.
    I used raw strings so that it's more readable in the editor.
    if someone edits this, be sure to remember to don't leave any trailing whitespaces.
    because that will mess up the rendering on the terminal if the terminal size is small.
    """
    return r"""
 ________       ________    ___           ___      __________               ___      __________   ___
|\   ____\     |\   __  \  |\  \         |\  \    |\___   ___\             |\  \    |\___   ___\ |\  \
\ \  \___|_    \ \  \|\  \ \ \  \        \ \  \   \|___ \  \_|             \ \  \   \|___ \  \_| \ \  \
 \ \_____  \    \ \   ____\ \ \  \        \ \  \       \ \  \               \ \  \       \ \  \   \ \  \
  \|____|\  \    \ \  \___|  \ \  \____    \ \  \       \ \  \               \ \  \       \ \  \   \ \__\
    ____\_\  \    \ \__\      \ \_______\   \ \__\       \ \__\               \ \__\       \ \__\   \|__|
   |\_________\    \|__|       \|_______|    \|__|        \|__|                \|__|        \|__|       ___
   \|_________|                                                                                        |\__\
                                                                                                       \|__|

    _                           _                              _                    _         _    _
   / \         ___  _   _  ___ | |_  ___   _ __ ___       ___ (_) _ __ ___   _   _ | |  __ _ | |_ (_)  ___   _ __
  / _ \       / __|| | | |/ __|| __|/ _ \ | '_ ` _ \     / __|| || '_ ` _ \ | | | || | / _` || __|| | / _ \ | '_ \
 / ___ \     | (__ | |_| |\__ \| |_| (_) || | | | | |    \__ \| || | | | | || |_| || || (_| || |_ | || (_) || | | |
/_/   \_\     \___| \__,_||___/ \__|\___/ |_| |_| |_|    |___/|_||_| |_| |_| \__,_||_| \__,_| \__||_| \___/ |_| |_|
                   _                            _  _  _    _                    __                   ____   _                        ___  _        _
  ___  __ _   ___ | |__    ___      ___  _ __  | |(_)| |_ | |_  ___  _ __      / _|  ___   _ __     / ___| | |__    ___   ___  _ __ |_ _|| |_     | |
 / __|/ _` | / __|| '_ \  / _ \    / __|| '_ \ | || || __|| __|/ _ \| '__|    | |_  / _ \ | '__|    \___ \ | '_ \  / _ \ / _ \| '_ \ | | | __|    | |
| (__| (_| || (__ | | | ||  __/    \__ \| |_) || || || |_ | |_|  __/| |       |  _|| (_) || |        ___) || | | ||  __/|  __/| |_) || | | |_     |_|
 \___|\__,_| \___||_| |_| \___|    |___/| .__/ |_||_| \__| \__|\___||_|       |_|   \___/ |_|       |____/ |_| |_| \___| \___|| .__/|___| \__|    (_)
                                        |_|                                                                                   |_|


________________________________________________________________________________________________________________________________________________________________________________
|:‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾:|
|: ██████╗ ██╗███████╗ ██████╗██╗      █████╗ ██╗███╗   ███╗███████╗██████╗ ██╗██╗██╗                                                                                         :|
|: ██╔══██╗██║██╔════╝██╔════╝██║     ██╔══██╗██║████╗ ████║██╔════╝██╔══██╗██║██║██║                                                                                         :|
|: ██║  ██║██║███████╗██║     ██║     ███████║██║██╔████╔██║█████╗  ██████╔╝██║██║██║                                                                                         :|
|: ██║  ██║██║╚════██║██║     ██║     ██╔══██║██║██║╚██╔╝██║██╔══╝  ██╔══██╗╚═╝╚═╝╚═╝                                                                                         :|
|: ██████╔╝██║███████║╚██████╗███████╗██║  ██║██║██║ ╚═╝ ██║███████╗██║  ██║██╗██╗██╗                                                                                         :|
|: ╚═════╝ ╚═╝╚══════╝ ╚═════╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝╚═╝                                                                                         :|
|:                                                                                                                                                                            :|
|: THIS WILL ONLY WORK FOR FLUID AND SMOKE CACHES ONLY! (As far as I know.. Haven't tested with others yet....)                                                               :|
|: This is because I only know how fluid cache files works and i haven't really worked it other simulations yet such as smoke and fire, particle systems...                   :|
|: I'll eventually learn them too and then i'll try to upgrade it!                                                                                                            :|
|: I'll also try to make a smart cache splitter where it will split the files based on their sizes.                                                                           :|
|: But for now you will have to set how many splits you want to make.                                                                                                         :|
|: If you have any suggestions and you know how to do it, I'll appreciate the help!                                                                                           :|
|: I'm just a member of the SheepIt community i'm not a dev so if i make any errors it's my fault not theirs!                                                                 :|
|:                                                                                                                                                                            :|
|:____________________________________________________________________________________________________________________________________________________________________________:|
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾

For the best visual experience, please Maximise the Terminal/Command Prompt.

BEFORE YOU START THIS MAKE SURE THAT YOU HAVE DOUBLE THE EMPTY SPACE IN YOUR DRIVE AS YOUR BLEND AND CACHE FILE COMBINED!
THAT MEANS IF YOUR BLEND FILE IS 100 mb AND YOUR SIMULATION CACHE FOLDER IS 900 mb, MAKE SURE THAT YOU HAVE ATLEAST 2 gb OF EMPTY SPACE IN YOUR DRIVE!
    """

if __name__ == "__main__":
    print(grettings())
