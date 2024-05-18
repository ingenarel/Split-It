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

def update_check(url):
    try:
        response=requests.get(url)
        if response.status_code == 200:
            latest_release = response.json()
            latest_version = latest_release.get('tag_name')

        else:
            if response.status_code == 400:
                print("")
                print("ERROR 400: bad request.")
                print("")
                print("his status code indicates that there's something off with the request you sent to the server.")
                print("t's like filling out a form incorrectly or forgetting to provide essential details.")
                print("he server couldn't understand or process your request due to missing or malformed data.")
                print("")

            elif response.status_code == 401:
                print("")
                print("ERROR 401: Unauthorized")
                print("")
                print("This status code means you're not allowed to access the requested resource without proper authentication.")
                print("It's like trying to enter a restricted area without showing your ID.")
                print("You need to provide valid credentials, such as a username and password or an authentication token, to gain access.")
                print("")

            elif response.status_code == 403:
                print("")
                print("ERROR 403: Forbidden.")
                print("")
                print("You're being denied access, plain and simple.")
                print("Even with valid credentials, you're not allowed to access the resource because you lack the necessary permissions.")
                print("It's like trying to enter a building without the proper authorization or access card.")
                print("You need to request permission from the appropriate authorities.")
                print("")

            elif response.status_code == 404:
                print("ERROR 404: File not found.")
                print("")
                print("This status code indicates that the server couldn't find the resource you requested.")
                print("It's like looking for a book on a library shelf only to discover it's not there.")
                print("The resource may have been moved, deleted, or simply never existed.")
                print("Double-check the URL or try searching for the resource in a different location.")
                print("")

            elif response.status_code == 422:
                print("")
                print("ERROR 422: Unprocessable Entity.")
                print("")
                print("Ah, it seems there's a problem with the data you provided. ")
                print("This status code typically occurs when the server understands your request but can't process it due to invalid data.")
                print("It's like trying to fill out a form with incorrect or incomplete information.")
                print("Review the data you submitted and ensure it meets the server's requirements.")

            elif response.status_code == 429:
                print("")
                print("ERROR 429: Too Many Requests.")
                print("")
                print("Slow down there! You've been making too many requests to the server within a short period. ")
                print("This status code indicates that you've hit a rate limit, and the server is asking you to ease up for a bit.")
                print("It's like trying to take too many slices of cake at once, and someone politely suggests you wait your turn.")
                print("")

            elif response.status_code == 500:
                print("")
                print("ERROR 500: Server Side Error.")
                print("")
                print("Uh-oh, something went wrong on the server's end, and it's not your fault.")
                print("This status code indicates an unexpected problem occurred while the server was trying to process your request.")
                print("It's like ordering food at a restaurant and having the kitchen catch fire.")
                print("The server is apologizing for the inconvenience and asking for your patience while they sort things out.")
                print("")

            elif response.status_code == 503:
                print("")
                print("ERROR 503: Server was not ready")
                print("")
                print("Hold your horses! The server is currently unavailable to handle your request.")
                print("This status code typically occurs due to maintenance or overload.")
                print("It's like calling a store outside of business hours and getting a message saying they're closed for the day.")
                print("You'll need to try again later when the server is back up and running.")
                print("")

            else:
                print(f"I Don't know what the fuck are you doing but I can't find an error code for you.\n")
    except requests.exceptions.RequestException:
        print("")
        print("Failed to retrieve the latest version from GitHub.")
        print("Please check your internet connection.")
        print("")
        return

    if latest_version:
        print(f"Current version: {variables.local_version}.")
        print(f"Latest version: {latest_version}.")

        if variables.local_version>latest_version:
            print("You're using a version that is newer than the latest stable built.")

        elif variables.local_version == latest_version:
            print("You are already using the latest version.")

        else:
            while True:
                print("A new version is available. Do you want to download it?")
                print("You if you want to use the latest version, you need to start it from the downloaded version though.")
                print("It creates a folder called latest_build and stores the zip there.")
                choice = input("press y to download and n to cancel: ").strip()

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
