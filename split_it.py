try:
    from __asciiarts import grettings, end, helpsite, credits
except ModuleNotFoundError:
    exit("You're missing __asciiarts.py")
import os, sys

class Variables:
    local_version="v1.2"
    title=f"Split It! version {local_version}"
    repo_owner = "ingenarel"
    repo_name = "Split-It"

def cls_():
    """
    usage:\n
    cls_()

    description:\n
    this clears the terminal screen based on the os.
    """
    if os.name == "nt":
        os.system("cls")
        print(grettings())
    elif os.name == "posix":
        print(grettings())
        os.system("clear")
    else:
        print("I didn't implement the command for this os sadly. please report this issue in the github repo")

def read_license():
    try:
        with open("LICENSE", "r") as file:
            return f"\n\n\n{file.read()}\n\n"
    except FileNotFoundError:
        exit("The license file is missing")

def asking():
    while True:
        try:
            i = input("What do you want to do?\n=> ").strip().lower()
            if i in ["s", "start"]:
                break
            elif i in ["ver", "version"]:
                ...
            elif i in ["cls", "clear"]:
                cls_()
            elif i in ["esc", "exit", "close"]:
                exit(end())
            elif i in ["license", "l"]:
                print(read_license())
            elif i in ["credits", "c"]:
                print(credits())
            elif i in ["help", "h"]:
                print(helpsite())
            else:
                print("")
                print("Invalid input.")
                print("")
        except (EOFError, KeyboardInterrupt):
            exit(end())

def main():
    if len(sys.argv) == 1:
        print(grettings())
        asking()
        exit(end())
    elif len(sys.argv) > 1:
        commands = set()
        for argument in sys.argv[1:]:
            argument = argument.lower()
            if argument in ["license", "l"]:
                commands.add("license")
            elif argument in ["help", "h"]:
                commands.add("help")
            elif argument in ["credits", "c"]:
                commands.add("credits")
            else:
                print(f"\"{argument}\" isn't a valid command. skipping it.")
        for command in commands:
            if command == "license":
                print(read_license())
            elif command == "help":
                print(helpsite())
            elif command == "credits":
                print(credits())


if __name__ == "__main__":
    main()
