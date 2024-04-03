import ctypes, os, shutil, zipfile, requests

#The Software startup and telling what is needed.
def start(**kwargs):
    ctypes.windll.kernel32.SetConsoleTitleW(kwargs["title"])
    print("""
________       ________    ___           ___      _________                ___      _________    ___
|\\   ____\\     |\\   __  \\  |\\  \\         |\\  \\    |\\___   ___\\             |\\  \\    |\\___   ___\\ |\\  \\
\\ \\  \\___|_    \\ \\  \\|\\  \\ \\ \\  \\        \\ \\  \\   \\|___ \\  \\_|             \\ \\  \\   \\|___ \\  \\_| \\ \\  \\
 \\ \\_____  \\    \\ \\   ____\\ \\ \\  \\        \\ \\  \\       \\ \\  \\               \\ \\  \\       \\ \\  \\   \\ \\  \\
  \\|____|\\  \\    \\ \\  \\___|  \\ \\  \\____    \\ \\  \\       \\ \\  \\               \\ \\  \\       \\ \\  \\   \\ \\__\\
    ____\\_\\  \\    \\ \\__\\      \\ \\_______\\   \\ \\__\\       \\ \\__\\               \\ \\__\\       \\ \\__\\   \\|__|
   |\\_________\\    \\|__|       \\|_______|    \\|__|        \\|__|                \\|__|        \\|__|       ___ 
   \\|_________|                                                                                        |\\__\\
                                                                                                       \\|__

    _                           _                              _                    _         _    _
   / \\         ___  _   _  ___ | |_  ___   _ __ ___       ___ (_) _ __ ___   _   _ | |  __ _ | |_ (_)  ___   _ __
  / _ \\       / __|| | | |/ __|| __|/ _ \\ | '_ ` _ \\     / __|| || '_ ` _ \\ | | | || | / _` || __|| | / _ \\ | '_ \\
 / ___ \\     | (__ | |_| |\\__ \\| |_| (_) || | | | | |    \\__ \\| || | | | | || |_| || || (_| || |_ | || (_) || | | |
/_/   \\_\\     \\___| \\__,_||___/ \\__|\\___/ |_| |_| |_|    |___/|_||_| |_| |_| \\__,_||_| \\__,_| \\__||_| \\___/ |_| |_|
                   _                            _  _  _    _                    __                   ____   _                        ___  _        _
  ___  __ _   ___ | |__    ___      ___  _ __  | |(_)| |_ | |_  ___  _ __      / _|  ___   _ __     / ___| | |__    ___   ___  _ __ |_ _|| |_     | |
 / __|/ _` | / __|| '_ \\  / _ \\    / __|| '_ \\ | || || __|| __|/ _ \\| '__|    | |_  / _ \\ | '__|    \\___ \\ | '_ \\  / _ \\ / _ \\| '_ \\ | | | __|    | |
| (__| (_| || (__ | | | ||  __/    \\__ \\| |_) || || || |_ | |_|  __/| |       |  _|| (_) || |        ___) || | | ||  __/|  __/| |_) || | | |_     |_|
 \\___|\\__,_| \\___||_| |_| \\___|    |___/| .__/ |_||_| \\__| \\__|\\___||_|       |_|   \\___/ |_|       |____/ |_| |_| \\___| \\___|| .__/|___| \\__|    (_)
                                        |_|                                                                                   |_|


 __  __               _            ____
|  \\/  |   __ _    __| |   ___    | __ )   _   _
| |\\/| |  / _` |  / _` |  / _ \\   |  _ \\  | | | |
| |  | | | (_| | | (_| | |  __/   | |_) | | |_| |
|_|  |_|  \\__,_|  \\__,_|  \\___|   |____/   \\__, |
                                           |___/
 ___   _   _    ____   _____   _   _      _      ____    _____   _
|_ _| | \\ | |  / ___| | ____| | \\ | |    / \\    |  _ \\  | ____| | |
 | |  |  \\| | | |  _  |  _|   |  \\| |   / _ \\   | |_) | |  _|   | |
 | |  | |\\  | | |_| | | |___  | |\\  |  / ___ \\  |  _ <  | |___  | |___
|___| |_| \\_|  \\____| |_____| |_| \\_| /_/   \\_\\ |_| \\_\\ |_____| |_____|


________________________________________________________________________________________________________________________________________________
|:‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾:|
|:   Wanna support me?                                                                                                                        :|
|:                                                                                                                                            :|
|:   SUPPORT THE SHEEPIT DEVS!!!! -                                                 https://www.sheepit-renderfarm.com/donation               :|
|:                                                                                                                                            :|
|:   Follow me on Instagram -                                                       https://www.instagram.com/saad_abdullah999666/            :|
|:   Reddit account -                                                               https://reddit.com/user/INGENAREL                         :|
|:   Discord -                                                                      ingenarel#2846                                            :|
|:   My youtube channel -                                                           https://www.youtube.com/channel/UC90Tar8Bpx3Q8UqpM8qxWZw  :|
|:   Sponsor me on SheepIt -                                                        https://www.sheepit-renderfarm.com/user/ingenarel/profile :|
|:   Here's my public renderkey if you wanna connect a device to my account -       XQVDMUjdOKt7LBldxjuF0YERqLoGnExbeh8yUrce                  :|
|:                                                                                                                                            :|
|:____________________________________________________________________________________________________________________________________________:|
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾

________________________________________________________________________________________________________________________________________________________________________________
|:‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾:|
|: ██████╗ ██╗███████╗ ██████╗██╗      █████╗ ██╗███╗   ███╗███████╗██████╗ ██╗██╗██╗                                                                                         :|
|: ██╔══██╗██║██╔════╝██╔════╝██║     ██╔══██╗██║████╗ ████║██╔════╝██╔══██╗██║██║██║                                                                                         :|
|: ██║  ██║██║███████╗██║     ██║     ███████║██║██╔████╔██║█████╗  ██████╔╝██║██║██║                                                                                         :|
|: ██║  ██║██║╚════██║██║     ██║     ██╔══██║██║██║╚██╔╝██║██╔══╝  ██╔══██╗╚═╝╚═╝╚═╝                                                                                         :|
|: ██████╔╝██║███████║╚██████╗███████╗██║  ██║██║██║ ╚═╝ ██║███████╗██║  ██║██╗██╗██╗                                                                                         :|
|: ╚═════╝ ╚═╝╚══════╝ ╚═════╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝╚═╝                                                                                         :|
|:                                                                                                                                                                            :|
|: THIS IS JUST A TEST PROJECT! I'M JUST AN AMATEUR PROGRAMMER! I LEARNED TO CODE THIS WHILE I WAS ALSO CODING IT SO THERE MAY BE STILL SOME BUGS LEFT!!!                     :|
|: THIS WILL ONLY WORK FOR FLUID CACHES ONLY! (As far as I know.. Haven't tested with others yet....)                                                                         :|
|: This is because I only know how fluid cache files works and i haven't really worked it other simulations yet such as smoke and fire, particle systems...                   :|
|: I'll eventually learn them too and then i'll try to upgrade it!                                                                                                            :|
|: I'll also try to make a smart cache splitter where it will split the files based on their sizes.                                                                           :|
|: But for now you will have to set how many splits you want to make.                                                                                                         :|
|: If you have any suggestions and you know how to do it, I'll appreciate the help!                                                                                           :|
|: I'm just a member of the SheepIt community i'm not a dev so if i make any errors it's my fault not theirs!                                                                 :|
|: I'll also try to post this on github and make it open source too altho i'm kinda a noob at that too. :(                                                                    :|
|:                                                                                                                                                                            :|
|:____________________________________________________________________________________________________________________________________________________________________________:|
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾

For the best visual experience, please Maximise the Terminal/Command Prompt.

BEFORE YOU START THIS MAKE SURE THAT YOU HAVE DOUBLE THE EMPTY SPACE IN YOUR DRIVE AS YOUR BLEND AND CACHE FILE COMBINED!
THAT MEANS IF YOUR BLEND FILE IS 100 mb AND YOUR SIMULATION CACHE FOLDER IS 900 mb, MAKE SURE THAT YOU HAVE ATLEAST 2 gb OF EMPTY SPACE IN YOUR DRIVE!""")
    please_enter_your_simulation_folder_name()
    return

#Printing the "please enter your Simulation folder name" text
def please_enter_your_simulation_folder_name():

    print(""" ____   _                                        _
|  _ \\ | |  ___   __ _  ___   ___    ___  _ __  | |_  ___  _ __   _   _   ___   _   _  _ __
| |_) || | / _ \\ / _` |/ __| / _ \\  / _ \\| '_ \\ | __|/ _ \\| '__| | | | | / _ \\ | | | || '__|
|  __/ | ||  __/| (_| |\\__ \\|  __/ |  __/| | | || |_|  __/| |    | |_| || (_) || |_| || |
|_|    |_| \\___| \\__,_||___/ \\___|  \\___||_| |_| \\__|\\___||_|     \\__, | \\___/  \\__,_||_|
      _                    _         _    _                  __   |___/ _      _
 ___ (_) _ __ ___   _   _ | |  __ _ | |_ (_)  ___   _ __    / _|  ___  | |  __| |  ___  _ __   _ __    __ _  _ __ ___    ___
/ __|| || '_ ` _ \\ | | | || | / _` || __|| | / _ \\ | '_ \\  | |_  / _ \\ | | / _` | / _ \\| '__| | '_ \\  / _` || '_ ` _ \\  / _ \\
\\__ \\| || | | | | || |_| || || (_| || |_ | || (_) || | | | |  _|| (_) || || (_| ||  __/| |    | | | || (_| || | | | | ||  __/
|___/|_||_| |_| |_| \\__,_||_| \\__,_| \\__||_| \\___/ |_| |_| |_|   \\___/ |_| \\__,_| \\___||_|    |_| |_| \\__,_||_| |_| |_| \\___|""")
    main_func()
    return

#Successfuly splitted it.
def success_msg():
    print(" ____    _   _    ____    ____   _____   ____    ____    _   _   _ ")
    print("/ ___|  | | | |  / ___|  / ___| | ____| / ___|  / ___|  | | | | | |")
    print("\\___ \\  | | | | | |     | |     |  _|   \\___ \\  \\___ \\  | | | | | |")
    print(" ___) | | |_| | | |___  | |___  | |___   ___) |  ___) | |_| |_| |_|")
    print("|____/   \\___/   \\____|  \\____| |_____| |____/  |____/  (_) (_) (_)")

#Something went wrong while splitting.
def error_msg():
    print("""        vXFAAAAAAAAAAAAAAAAAAAAAAAAAAOR2r
   p6HAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABCBBBBZy
         hYDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPw
               VAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA3
               fAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA7
                RAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAL
                dAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAV
                PAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA                 
               sAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA3                
               kAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAK                 _   _           __  _  _                        __         _      _
                mVVXYZZ36777987ZAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv               | \\ | |  ___    / _|(_)| |  ___    ___   _ __   / _|  ___  | |  __| |  ___  _ __
                                  fRAAAAAAAAAAAAAAAAAAAAXv          wbMAAAAAAAAAAAAAA8              |  \\| | / _ \\  | |_ | || | / _ \\  / _ \\ | '__| | |_  / _ \\ | | / _` | / _ \\| '__|
                                     sAAAAAAAAAD0z      tmmz            8AAAAAAAAAAAAA5             | |\\  || (_) | |  _|| || ||  __/ | (_) || |    |  _|| (_) || || (_| ||  __/| |
                                       kAAAAAAi        AAAAV      p     BAAAAAAAAAAAAAAh            |_| \\_| \\___/  |_|  |_||_| \\___|  \\___/ |_|    |_|   \\___/ |_| \\__,_| \\___||_|
                                        eAAAAAABe                   s7EAAAAAAAAAAAAAAAAAb             __                           _   _              _    _             _
          qCAAAAABX6ffbdkmjchiaht       gAAAAAAAAA     qe94567992AAAAAAAAAAAAAAAAAAAAAAAAh           / _|  ___   _   _  _ __    __| | | |__   _   _  | |_ | |__    __ _ | |_
            0AAAAAAAAAAAAAAAAAAA0       nAAAAAAAAAx   XAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA          | |_  / _ \\ | | | || '_ \\  / _` | | '_ \\ | | | | | __|| '_ \\  / _` || __|
               kcVKHAAAAAAAAAA2x         AAAAAAAAA9   hDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAV         |  _|| (_) || |_| || | | || (_| | | |_) || |_| | | |_ | | | || (_| || |_
                    kAAAAAAAAR           3AAAAAAAAX   t9UAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA         |_|   \\___/  \\__,_||_| |_| \\__,_| |_.__/  \\__, |  \\__||_| |_| \\__,_| \\__|
                      6AAAAAZ            lAAAAAAAAA       FAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA                                                   |___/
                       8AAAZ             gAAAAAAAAAAf     fAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAF                                              ____  _                  _
                                         AAAAAAAAAAAAAr    hAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAo          _ __    __ _  _ __ ___    ___      / ___|| |__    ___   ___ | | __  _   _   ___   _   _  _ __
                                         TAAAAAAAAAAAAa     zAAAAAAAAAAAAAAAAAAAAAAAAAAAAA          | '_ \\  / _` || '_ ` _ \\  / _ \\    | |    | '_ \\  / _ \\ / __|| |/ / | | | | / _ \\ | | | || '__|
                                           kEAAAAAAAAO      ZAAAAAAAAAAAANkQAAAAAAAAAAAAAh          | | | || (_| || | | | | ||  __/ _  | |___ | | | ||  __/| (__ |   <  | |_| || (_) || |_| || |   
                                              wh6WRF3     oNAAAAAAAAAAAAA9   4AAAAAAAAAAE           |_| |_| \\__,_||_| |_| |_| \\___|(_)  \\____||_| |_| \\___| \\___||_|\\_\\  \\__, | \\___/  \\__,_||_|   
                                                       vAAAAAAAAAAAAAAAAAA6   oAAAAAAAAE                               _  _  _                                      _    |___/                     
                                                      BAAAAAAAAAAAAAAAAAAAAP    2AAAAAAy             ___  _ __    ___ | || |(_) _ __    __ _    __ _   __ _   __ _ (_) _ __                        
                                            aAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAa   AAAAA7             / __|| '_ \\  / _ \\| || || || '_ \\  / _` |  / _` | / _` | / _` || || '_ \\                       
                                             8RRNAAAAAAAAAAAAAAAAAAAAAAAAAAAAA9   AAAE              \\__ \\| |_) ||  __/| || || || | | || (_| | | (_| || (_| || (_| || || | | | _                    
                                  kEAA7sy               s9221ZYXWKAAAAAAMUZ45d    AAAl              |___/| .__/  \\___||_||_||_||_| |_| \\__, |  \\__,_| \\__, | \\__,_||_||_| |_|(_)                   
                                 pGAAAAAAAAAAAAGeoz                          qu   AAp                    |_|                           |___/          |___/                                        
                                   vUAAAAAAAAAAAAAAAAAAAAAWefgeeeffffffg5AAAAAAAeHAH
                                     2AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAg
                                     XAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
                                    cDAAAAAOUHAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD
                                    5AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAz
                                     WAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
                                    ZAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA7
                                    LAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
                                    XAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD
                                     aAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAr
                                    vTAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAd
                                      cAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
                                         oBAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAX
                                           u7CAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAY
                                               mfKAAAAAAAAAAAAAAAAAAAAAAAAARw
                                                   tkeLAAAAAAAAAAAAAAABXw""")
    return

#The splitter is done
def end():
    print("""""Your splitting is finished. yayyyyyyy!!!!!

++++++++++++++++**++*%#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++@*#+###+%*#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++*%*+@+@#*#*%+**+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++*#*#@**#++#++@++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#@++#@++++++++
+++++++++++++*#**++++++++@%##++++++++++++++++++++++++++++++++++++++++++++++++++++++++#**#+##++##++++
++++++++++++++@+++*****+*#+*#+++++++++++++++++++++++++++++++++++++++++++++++++++++**+@*+#@*@*%*%++++
++++++++++++++@+++****%**++@+++++++++++++++++++++++++++++++++++++++++++++++++++++***#%++++*##+#+++++
++++++++++++++%#******+*++%++++++++++++++++++++++++++++++++++++++++++++++++++++++**+#*+*+++++#*%#%%+
+++++++++++++##+++++++++*#%*+++++++++++++++++++++++++++++++++++++++++++++++++++++**++*******+***%*++
+++++++++++++#++++++++++***#*++++++++++++++++++++++++++++++++++++++++++++++++++++*#+++*#***+++**++++
++++++++++++##+*#%%%%%%%%#*#*+++++++++++++++++++++++++++++++++++++++++++++++++++##%##***+*+++*#+++++
++++++++++++@@@@%%%###%%%%@@#+++++++++++++++++++++++++++++++++++++++++++++++++#*+++++++*###+#%++++++
++++++++++++@%*++++++++****#%++++++++++++++++++++++++++++++++++++++++++++++++**++++++++++++##+++++++
+++++++++++##+#%###***##%%%#@+++++++++++++++++++++++++++++++++++++++++++++++%*++++++++++++***%++++++
+++++++++++*%#*********###%@*+++*#%##***+++++++***##%%%%**++++++++++++++++*@@@@@@@@@@%#*****#%++++++
++++++++++++%**********###%@*%%#+++++++++++*#+*+++++++++*#%@%*++++++++++++@*+****++**%@@@%#*%+++++++
++++++++++++#**********##%%#*++++++*++++++#*#+#+++++*++++++++*#%#+++++++++%*######%%%#**#%@@#+++++++
+++++++++++#**********#%#+++++++++*+++++*#**#+#+++++*+++++++++++*#%#+++++++#%##########%%*#@++++++++
+++++++++++#********#%#++++*++*++#+++++*#***#+#+++++**+++++++*++**+*%%+++++%*******######@##++++++++
++++++++++##*******%%+++++*++**+*+++++*#***+*+#+++++**+++++++*+++***++#%+*%***********##%@%+++++++++
++++++++++@#*****#%*+++++**+*%**#*****#***++**%++++++#+++++++*++++**+++*%%#************#%+++++++++++
+++++++++*%*****##+++++++#**%#*%*****#***+++*#%#*****%**+++++**++++**+++*%************#@++++++++++++
+++++++++##****%*+++*+**#**#%*#%#%%%%**++++++##%***##%@%******#+++++#*++%*************%*++++++++++++
+++++++++%***#%++*******@**%##@****%**+++++++*#%******##**#***%******#+##************#%+++++++++++++
+++++++++#**##++*******##**##*%***##*++++++++++*******%#******#******##%*************%*+++++++++++++
++++++++##*#*+*****#**#*#*#***#+**#*+++++++++++++++*#***%******%*****#%**********#**##++++++++++++++
++++++++@%#+******#***#*++++***#*##*+++++++++++++*##***********%#****##*************#+++++++++++++++
++++++*#*+*#**#***#**#**++**##%%%%***+++++++++++**##%%%%%%%###**%****#*************##+++++++++++++++
++*%@*+**%##*********#**#%%%#****#%@*+++++++++++*%%#******#%@%***#**##*************%++++++++++++++++
++++***##*%*+#*******#%%%*++++**++++++++++++++++++++#%%%%%#+*%@%+*###*************##++++++++++++++++
+++++++%##@**%***#*+%%%*+++*#%%%%%*++++++++++++++++++*%%%%%%++#@%+*%#************#%+++++++++++++++++
+++++++%**%**#**+#**%%*+++++*%%%%%%*+++++++++++++*%###%@%%%@#++#@###*************##+++++++++++++++++
+++++++%*****#***##*@#++*@@%*****%@#+++++++++++++%#+++++**@@%++*@%%**************@*+++++++++++++++++
+++++++%*******##****+++#@*+++++++#*+++++++++++++%++++*+++*%*+++*%#*************##++++++++++++++++++
+++++++#*******##**#*+++*%*++++++**++++++++++++++*%*++++++#*+++*#%***********#**%@++++++++++++++++++
++++++*%******###*+*++++*+#*****++++++++++++++++++++****#*++++*#%##*******#######@*+++++++++++++++++
++++++*%*****#%*#*++*++*++*+++++++++++++++++++++++++++++++++**#*%********######@*@++++++++++++++++++
++++++*#*****#**#*++*++****++++++++++++++++++++++++++++++*+**#+%#******#########*%#+++++++++++++++++
++++++*%*****#+***++++++**++++++++++++++******++++++++++++++%*#%*******#######%**##+++++++++++++++++
++++++*%****%*++**++++++++++++++++*#%##*********#*++++++*++*#*@#******#########**##+++++++++++++++++
++++++*%***##++*%+++++++++++++++++####**********#*++++++++*#+#%*******#######%***##+++++++++++++++++
+++++++#***#+++*%+++++++++++++++++*#************#*++++++++%*+##*******######%#****%+++++++++++++++++
+++++++%***#+++*##+++++++++++++++++%************#++++++++##+*##*******######%*****%+++++++++++++++++
+++++++%#*#*+++**%*+++++++++++++++++***********#+++++++++#+*%#*********####%#+****%+++++++++++++++++
+++++++#%##+++****%%+++++++++++++++++*********#*++++++++#*+*@#*********####%*+++++%+++++++++++++++++
+++++++*@#*+++*****#@#*+++++++++++++++++++++*++++++++++*%+*##**********####%+++++*%+++++++++++++++++
++++++++@%+++****##%##%%#++++++++++++++++++++++++++++++#*+*##**********###%%*+++++##++++++++++++++++
++++++++*%+++****#%####%*#%#*++++++++++++++++++++++++*##+**#***********##%%#*+++++*@++++++++++++++++
+++++++++*+++***#######%#+%@**#%%%**++++++++++++**#%%#%****#***********##%%#*++++**@++++++++++++++++
++++++++**++****#%########*@#+******#**#%********#@#**@*+**#***********##%%*#++++++%#+++++++++++++++
++++++++@*++****%%#####**#*#@*++****####%********%***##+**##***********#%#*##*+++++*%+++++++++++++++
++++++++@*++****@#####****%+%@*+++**##**********#**++#*+**#*************%**#*#++++++%*++++++++++++++
++++++++@++*#**#%####******%*%@*++++*%#******##%*+++*%++**%************##***##*+++++*@++++++++++++++
++++++++@++****#%###*******##*%@*++++*#+****++#*+++*@#++**%************%*#**###++++++##+++++++++++++
++++++++@++****#%##**********###@#++++#*+++++##+++#@%#++*##***********#%*#***##%++++++%+++++++++++++


Please check your zip files before you upload your project. Because
I'm dumb
and
even if something works for someone it might not work for others.
I hope you have a great life""")

#Variables for runtime
class variables:
    #The title Variable
    title="Split It! version 0.8"
    
    starting_choice=""
    
    folder_name=""
    folders=0
    folder_lookup={"1": "config", "2": "data", "3": "mesh", "4": "guiding", "5": "noise", "6": "particles"}
    
    current_folder=1
    output_dir=""
    
    file_count=0
    source_folder=""
    folder_list=""
    source_files=""
    
    files_in_directory=""
    destination_base_folder=""
    
    count=0
    folder_count=1
    
    exist_ok=True
    
    guiding_exists=False
    noise_exists=False
    particles_exist=False

#Listing the folders
def list_folders():
    try:
        while True:
            variables.folder_name=input("Please enter your foldername. (CASE SENSITIVE!)")#.lower() #Just in case you change your mind.
            variables.folder_list=[folder for folder in os.listdir('.') if os.path.isdir(folder)]
            print(variables.folder_list)
            if variables.folder_name not in variables.folder_list:
                error_msg()
                
            else:
                return
            
    except KeyboardInterrupt:
        return

#Function for copying all the folders.
def processing_folders():
    if variables.folder_name in variables.folders:
        while True:
            while True:
                try:
                    variables.file_count=int("Enter the number of files to copy in to each folder: ")
                except TypeError:
                    print(f"Nuh uh! Numbers only!\n")
                
                if variables.file_count > 1:
                    print("Nuh uh! There has to be at least <ReplaceNumber> files. ")
                
                elif variables.file_count < 9:
                    break
            
            variables.output_dir=str(variables.folder_lookup.get(str(variables.current_folder)))
            variables.source_folder=os.path.join(variables.folder_name, variables.output_dir)
            variables.destination_base_folder="Destination"
            
            print(f"Please wait while I split the {variables.folder_lookup.get(str(variables.current_folder))} files...>.<")
            
            print

def main_func():
    while True:
        print("""
You can type "Ver" or "Version" to check if an update is there.
You can type "cls" or "clear screen" to clean the Terminal/Command Prompt.
Type "s" or "start" to use the splitter.
type "help" for a more thorough help site.""")
        
        variables.starting_choice=input("What do you want to do? ")
        
        if variables.starting_choice=="s" or variables.starting_choice=="start":
            list_folders()
            processing_folders()

if __name__=="__main__":
    start(title=variables.title)