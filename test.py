import os

cachefolder_path = "L:\\cachesplittertest\\LiquidSim"
blendfile_path = "l:\\cachesplittertest\\kaboom.blend"

for folders in os.listdir(cachefolder_path):
    for files in os.listdir(f"{cachefolder_path}\\{folders}"):
        print(files)
