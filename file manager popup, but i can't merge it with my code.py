import tkinter as tk
from tkinter import filedialog
import os

def list_folders():
    root = tk.Tk()
    root.withdraw()  # Hide the tkinter window

    # Prompt user to select a folder using the file manager dialog
    folder_path = filedialog.askdirectory(title="Select Folder")

    # Return the folder name if a folder is selected
    if folder_path:
        folder_name = os.path.basename(folder_path)
        print("Selected folder:", folder_name)
        return folder_name
    else:
        print("No folder selected.")
        return None

# Example usage:
folder_name = list_folders()
# Do something with the selected folder name, such as further processing or saving
