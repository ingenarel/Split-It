from contextlib import chdir
import os, re

def data_maker_function(cache_directory_name:str):
    data = {}
    for folder in os.listdir(cache_directory_name):
        filenamelist = []
        for file in os.listdir(f"{cache_directory_name}/{folder}"):
            filenamelist.append(f"{cache_directory_name}/{folder}/{file}")
        if filenamelist != []:
            data[folder] = filenamelist
    return data

def partition_data(sim_dir_data):
    x = []
    for folder in sim_dir_data:
        x.append(sim_dir_data[folder])
    y = zip(*x)
    
    data = []
    for filelist in sorted(y):
        size = 0
        filelistwithsize = []
        for file in filelist:
            # print(file)
            filelistwithsize.append(file)
            size += os.path.getsize(file)
        filelistwithsize.append(size)
        data.append(filelistwithsize)
    return data

def split_func(partitioned_data):
    x = []
    maxsize = 2147483648
    buffer = []
    size = 0
    for filelistwithsize in partitioned_data:
        if size+filelistwithsize[-1] < maxsize:
            size += filelistwithsize[-1]
            buffer.append(filelistwithsize[:-1])
        elif size+filelistwithsize[-1] > maxsize:
            x.append(buffer)
            # print(buffer)
            buffer = []
            size = 0
            size += filelistwithsize[-1]
            buffer.append(filelistwithsize[:-1])
        else:
            print("critical error")

    if buffer:
        x.append(buffer)

    return x

def test_split(bufferlist):
    for buffer in bufferlist:
        size = 0
        for filelist in buffer:
            for file in filelist:
                size += os.path.getsize(file)
        print(size)

def split_parser(bufferlist):
    x = []
    for buffer in bufferlist:
        y = zip(*buffer)
        x.append(sorted(y))
    
    data = {}
    first_frame = 0
    for buffer in x:
        last_frame = first_frame+len(buffer[0])
        folderdata = {}
        for folder in buffer:
            # print(re.search(r"^.+/",folder[0]).group())
            folderdata[re.search(r"^.+/",folder[0]).group()] = folder
        data[f"{first_frame+1}-{last_frame}"] = folderdata
        first_frame = last_frame
    
    print(data)

def main():
    cache_directory = "/mnt/D/System files(D)/windows files/cachesplittertest/LiquidSim"
    split_parser(
        split_func(
            partition_data(
                data_maker_function(
                    cache_directory
                )
            )
        )
    )
    # print(partition_data(data_maker_function("/mnt/D/System files(D)/windows files/cachesplittertest/LiquidSim")))
    # test_split(split_func(partition_data(data_maker_function("/mnt/D/System files(D)/windows files/cachesplittertest/LiquidSim"))))
    # split_func(partition_data(data_maker_function("/mnt/D/System files(D)/windows files/cachesplittertest/LiquidSim")))

if __name__ == "__main__":
    main()
    # 1 gb  = 1000000000 bytes
    # 1 gib = 1073741824 bytes

