import os

cachefolder_path = "L:\\cachesplittertest\\LiquidSim"
blendfile_path = "l:\\cachesplittertest\\kaboom.blend"

last_shit = 0
for folders in os.listdir(cachefolder_path):
    try:
        counter = 0
        while counter < 3:
            last_shit = counter
            print(os.listdir(f"{cachefolder_path}\\{folders}")[last_shit])
            counter += 1

    except IndexError:
        pass
    # for files in os.listdir(f"{cachefolder_path}\\{folders}"):
    #     print(f"{folders}=>{files}")
