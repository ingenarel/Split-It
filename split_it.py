try:
    from __asciiarts import __grettings, __end, __helpsite, __credits, __HTTP_statues_codes_error
except ModuleNotFoundError:
    exit("You're missing __asciiarts.py")
import os, sys, requests

class Variables:
    #The title Variable
    local_version="v1.1"
    title=f"Split It! version {local_version}"

    #URL Specific stuff
    repo_owner = "ingenarel"
    repo_name = "Split-It"

    #folder specific variables for copying/other used in and for the "processing_folders" function
    folder_name=""

    #The lookup is for processing the folders and Variables for the "processing_folders" function
    folder_lookup={"1": "config", "2": "data", "3": "mesh", "4": "guiding", "5": "noise", "6": "particles"}
    current_folder=1
    max_folders=6

    output_dir=""

    file_count=0
    source_folder=""
    folder_list=""
    source_files=""
    source_file=""

    files_in_directory=""
    destination_base_folder="Destination"
    destination_folder="Destination"

    count=0
    folder_count=1

    exist_ok=True

def cls_():
    """
    usage:\n
    cls_()

    description:\n
    this clears the terminal screen based on the os.
    """
    if os.name == "nt":
        os.system("cls")
        print(__grettings())
    elif os.name == "posix":
        print(__grettings())
        os.system("clear")
    else:
        print("I didn't implement the command for this os sadly. please report this issue in the github repo")

def read_license():
    try:
        with open("LICENSE", "r") as file:
            return f"\n\n\n{file.read()}\n\n"
    except FileNotFoundError:
        exit("The license file is missing")

def update_check(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            latest_release = response.json()
            latest_version = latest_release.get('tag_name')
        else:
            print(__HTTP_statues_codes_error(response.status_code))
    except requests.exceptions.RequestException:
        print("")
        print("Failed to retrieve the latest version from GitHub.")
        print("Please check your internet connection.")
        print("")

    else:
        if latest_version:
            print(f"Current version: {Variables.local_version}.")
            print(f"Latest version: {latest_version}.")

            if Variables.local_version>latest_version:
                print("You're using a version that is newer than the latest stable built.")

            elif Variables.local_version == latest_version:
                print("You are already using the latest version.")

            else:
                while True:
                    print("A new version is available. Do you want to download it?")
                    print("You if you want to use the latest version, you need to start it from the downloaded version though.")
                    print("It creates a folder called latest_build and stores the zip there.")
                    choice = input("press y to download and n to cancel:\n=>").strip()

                    if choice.lower() == "y":
                        # Download the latest build
                        assets = latest_release.get('assets', [])

                        if assets:
                            # Create a folder to store the downloaded files
                            download_folder = "latest_build"
                            os.makedirs(download_folder, exist_ok=True)

                            for asset in assets:
                                download_url = asset.get('browser_download_url')
                                download_response = requests.get(download_url)

                                if download_response.status_code == 200:
                                    # Save the file
                                    file_path = os.path.join(download_folder, asset.get('name'))
                                    with open(file_path, 'wb') as file:
                                        file.write(download_response.content)
                                    print(f"Downloaded: {asset.get('name')}")
                                    break

                                #There has been an issue downloading
                                else:
                                    print(f"Failed to download: {asset.get('name')}")
                                    break

                            #Downloading is done 👍
                            print(f"All assets from the latest release have been downloaded to '{download_folder}'.")
                            break

                        #no assets found
                        else:
                            print("No assets found in the latest release.")
                            break

                    #Skipped the download
                    elif choice.lower() == "n":
                        print("Skipping download.")
                        break

                    #Clearing the screen.
                    elif choice.lower() in ["cls", "clear"]:
                        cls_()
                        continue

                    #Choice was invalid...
                    else:
                        print("Invalid choice. Please enter 'yes' or 'no'.")
                        continue
        else:
            print("Failed to retrieve the latest version from GitHub. Please check your internet connection and try again.")
            input("press enter to go back to the main menu.").strip()


def asking():
    while True:
        try:
            i = input("What do you want to do?\n=> ").strip().lower()
            if i in ["s", "start"]:
                break
            elif i in ["ver", "version", "v"]:
                update_check(f"https://api.github.com/repos/{Variables.repo_owner}/{Variables.repo_name}/releases/latest")
            elif i in ["cls", "clear"]:
                cls_()
            elif i in ["esc", "exit", "close", "end", "e"]:
                exit(__end())
            elif i in ["license", "l"]:
                print(read_license())
            elif i in ["credits", "c"]:
                print(__credits())
            elif i in ["help", "h"]:
                print(__helpsite())
            else:
                print("")
                print("Invalid input.")
                print("")
        except (EOFError, KeyboardInterrupt):
            exit(__end())

def main():
    if len(sys.argv) == 1:
        print(__grettings())
        asking()
        exit(__end())
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
            elif command in ["esc", "exit", "close", "end", "e"]:
                commands.add("exit")
            else:
                print(f"\"{argument}\" isn't a valid command. skipping it.")
        for command in commands:
            if command == "license":
                print(read_license())
            elif command == "help":
                print(__helpsite())
            elif command == "credits":
                print(__credits())
            elif command == "exit":
                print(__end())


if __name__ == "__main__":
    main()
