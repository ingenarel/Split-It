from grettings import grettings
from os import system as OSsystem
from os import name as OSname

def cls_():
    """
    usage:\n
    cls_()

    description:\n
    this clears the terminal screen based on the os.
    """
    if OSname == "nt":
        OSsystem("cls")
    elif OSsystem == "posix":
        OSsystem("clear")
    else:
        print("This os is not supported for this command")

def asking():
    while True:
        try:
            i = input("What do you want to do?\n=> ").strip().lower()
            if i in ["license", "l"]:
                return "license"
            elif i in ["s", "start"]:
                return "start"
            elif i in ["ver", "version"]:
                return "version"
            elif i in ["cls", "clear"]:
                cls_()
                print(grettings())
            elif i in ["esc", "exit", "close"]:
                exit()
            elif i in ["license", "l"]:
                return "license"
            elif i in ["credits", "c"]:
                return "credits"
            elif i == "help":
                return "helpsite"
            else:
                print("")
                print("Invalid input.")
                print("")
        except EOFError:
            exit()

def main():
    print(grettings())
    print(asking())

if __name__ == "__main__":
    main()
