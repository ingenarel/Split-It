try:
    from __asciiarts import grettings, end, helpsite
except ModuleNotFoundError:
    exit("You're missing __asciiarts.py")
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

def read_license():
    try:
        with open("LICENSE", "r") as file:
            return f"\n\n\n{file.read()}\n\n"
    except FileNotFoundError:
        exit("The license file is missing")


def main():
    print(grettings())
    while True:
        try:
            i = input("What do you want to do?\n=> ").strip().lower()
            if i in ["s", "start"]:
                ...
            elif i in ["ver", "version"]:
                ...
            elif i in ["cls", "clear"]:
                cls_()
                print(grettings())
            elif i in ["esc", "exit", "close"]:
                exit(end())
            elif i in ["license", "l"]:
                print(read_license())
            elif i in ["credits", "c"]:
                ...
            elif i == "help":
                print(helpsite())
            else:
                print("")
                print("Invalid input.")
                print("")
        except (EOFError, KeyboardInterrupt):
            exit(end())

if __name__ == "__main__":
    main()
