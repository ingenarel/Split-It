import os

cachefolder_path = "L:\\cachesplittertest\\LiquidSim"
blendfile_path = "l:\\cachesplittertest\\kaboom.blend"

for folders in os.listdir(cachefolder_path):
    try:
        last_shit = 0
        counter = 0
        while counter < 3:
            if counter == 3:
                counter = 0
                break
            print(os.listdir(f"{cachefolder_path}\\{folders}")[last_shit])
            counter += 1
            last_shit += 1
    except IndexError:
        pass
    # for files in os.listdir(f"{cachefolder_path}\\{folders}"):
    #     print(f"{folders}=>{files}")
