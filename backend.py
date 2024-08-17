import os, re, time, shutil

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

def split_func(partitioned_data, sim_dir_max_size_per_buffer):
    x = []
    buffer = []
    size = 0
    for filelistwithsize in partitioned_data:
        if size+filelistwithsize[-1] < sim_dir_max_size_per_buffer:
            size += filelistwithsize[-1]
            buffer.append(filelistwithsize[:-1])
        elif size+filelistwithsize[-1] > sim_dir_max_size_per_buffer:
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
            folderdata[re.search(r"^.+/",folder[0]).group()] = folder
        data[f"{first_frame+1}-{last_frame}"] = folderdata
        first_frame = last_frame
    
    return data

def move_and_zip(parsed_bufferlist, cache_directory, destination_directory, blend_file_path):
    main_destination = time.asctime().replace(" ", "_").replace(":", "-")
    sim_dir_name = re.search(r"^.+/(.+)", cache_directory).group(1)
    blend_file_name = re.search(r"^.+/(.+)", blend_file_path).group(1)
    for buffer in parsed_bufferlist:
        for folderlist in parsed_bufferlist[buffer]:
            foldername = re.search(r"^.+/(.+)", folderlist).group(1)
            os.makedirs(f"{destination_directory}/{main_destination}/{buffer}/{sim_dir_name}/{foldername}")
            for file in parsed_bufferlist[buffer][folderlist]:
                filename = re.search(r"^.+/(.+)", file).group(1)
                print(f"copying {destination_directory}/{main_destination}/{buffer}/{sim_dir_name}/{foldername}{filename}...")
                shutil.copyfile(file, f"{destination_directory}/{main_destination}/{buffer}/{sim_dir_name}/{foldername}{filename}")
                print("Succesful!")

        print(f"copying {destination_directory}/{main_destination}/{buffer}/{blend_file_name}_{buffer}.blend...")
        shutil.copyfile(blend_file_path, f"{destination_directory}/{main_destination}/{buffer}/{blend_file_name}_{buffer}.blend")
        print("Succesful!")

        print(f"creating {destination_directory}/{main_destination}/{blend_file_name}_{buffer}.zip")
        shutil.make_archive(
                f"{destination_directory}/{main_destination}/{blend_file_name}_{buffer}",
                'zip',
                f"{destination_directory}/{main_destination}/{buffer}",
                )
        print("Succesful!")

def initialize(
        cache_directory_path:str,
        destination_directory_path:str,
        blend_file_path:str,
        other_files_and_dirs:list=None,
        ):
    maxsize = 2147483648
    maxsize = maxsize - os.path.getsize(blend_file_path)
    splitted_data = split_parser(
        split_func(
            partition_data(
                data_maker_function(
                    cache_directory_path
                )
            ),
            maxsize
        )
    )
    move_and_zip(splitted_data, cache_directory_path, destination_directory_path, blend_file_path)

def main():
    # cache_directory = "/mnt/D/System files(D)/windows files/cachesplittertest/LiquidSim"
    cache_directory = "/home/ingenarel/Blender/archfluidcache"
    destination_directory = "/home/ingenarel/Blender"
    blend_file_path = "/home/ingenarel/Blender/arch linux fluid4.blend"
    initialize(
        cache_directory,
        destination_directory,
        blend_file_path
    )
if __name__ == "__main__":
    main()
    print("done!")
    # 1 gb  = 1000000000 bytes
    # 1 gib = 1073741824 bytes

