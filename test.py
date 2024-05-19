shit = {
    "L:\\cachesplittertest\\LiquidSim\\config": [
        ["L:\\cachesplittertest\\LiquidSim\\config\\config_0001.uni", 70],
        ["L:\\cachesplittertest\\LiquidSim\\config\\config_0002.uni", 70],
        ["L:\\cachesplittertest\\LiquidSim\\config\\config_0003.uni", 69],
        ["L:\\cachesplittertest\\LiquidSim\\config\\config_0004.uni", 70],
        ["L:\\cachesplittertest\\LiquidSim\\config\\config_0005.uni", 70],
        ["L:\\cachesplittertest\\LiquidSim\\config\\config_0006.uni", 69],
        ["L:\\cachesplittertest\\LiquidSim\\config\\config_0007.uni", 70],
        ["L:\\cachesplittertest\\LiquidSim\\config\\config_0008.uni", 70],
        ["L:\\cachesplittertest\\LiquidSim\\config\\config_0009.uni", 70],
        ["L:\\cachesplittertest\\LiquidSim\\config\\config_0010.uni", 70],
        ["L:\\cachesplittertest\\LiquidSim\\config\\config_0011.uni", 70],
        ["L:\\cachesplittertest\\LiquidSim\\config\\config_0012.uni", 70],
        ["L:\\cachesplittertest\\LiquidSim\\config\\config_0013.uni", 70],
        ["L:\\cachesplittertest\\LiquidSim\\config\\config_0014.uni", 70],
        ["L:\\cachesplittertest\\LiquidSim\\config\\config_0015.uni", 69],
    ],
    "L:\\cachesplittertest\\LiquidSim\\data": [
        ["L:\\cachesplittertest\\LiquidSim\\data\\fluid_data_0001.vdb", 3822022],
        ["L:\\cachesplittertest\\LiquidSim\\data\\fluid_data_0002.vdb", 4141113],
        ["L:\\cachesplittertest\\LiquidSim\\data\\fluid_data_0003.vdb", 4249452],
        ["L:\\cachesplittertest\\LiquidSim\\data\\fluid_data_0004.vdb", 4464375],
        ["L:\\cachesplittertest\\LiquidSim\\data\\fluid_data_0005.vdb", 4823982],
        ["L:\\cachesplittertest\\LiquidSim\\data\\fluid_data_0006.vdb", 5391418],
        ["L:\\cachesplittertest\\LiquidSim\\data\\fluid_data_0007.vdb", 6259099],
        ["L:\\cachesplittertest\\LiquidSim\\data\\fluid_data_0008.vdb", 7414788],
        ["L:\\cachesplittertest\\LiquidSim\\data\\fluid_data_0009.vdb", 8930918],
        ["L:\\cachesplittertest\\LiquidSim\\data\\fluid_data_0010.vdb", 10851008],
        ["L:\\cachesplittertest\\LiquidSim\\data\\fluid_data_0011.vdb", 13335231],
        ["L:\\cachesplittertest\\LiquidSim\\data\\fluid_data_0012.vdb", 16396091],
        ["L:\\cachesplittertest\\LiquidSim\\data\\fluid_data_0013.vdb", 20072970],
        ["L:\\cachesplittertest\\LiquidSim\\data\\fluid_data_0014.vdb", 24481612],
        ["L:\\cachesplittertest\\LiquidSim\\data\\fluid_data_0015.vdb", 29813950],
    ],
    "L:\\cachesplittertest\\LiquidSim\\mesh": [
        ["L:\\cachesplittertest\\LiquidSim\\mesh\\fluid_mesh_0001.bobj.gz", 2053358],
        ["L:\\cachesplittertest\\LiquidSim\\mesh\\fluid_mesh_0002.bobj.gz", 2118354],
        ["L:\\cachesplittertest\\LiquidSim\\mesh\\fluid_mesh_0003.bobj.gz", 2314623],
        ["L:\\cachesplittertest\\LiquidSim\\mesh\\fluid_mesh_0004.bobj.gz", 2783906],
        ["L:\\cachesplittertest\\LiquidSim\\mesh\\fluid_mesh_0005.bobj.gz", 3639415],
        ["L:\\cachesplittertest\\LiquidSim\\mesh\\fluid_mesh_0006.bobj.gz", 4882268],
        ["L:\\cachesplittertest\\LiquidSim\\mesh\\fluid_mesh_0007.bobj.gz", 6611907],
        ["L:\\cachesplittertest\\LiquidSim\\mesh\\fluid_mesh_0008.bobj.gz", 8958085],
        ["L:\\cachesplittertest\\LiquidSim\\mesh\\fluid_mesh_0009.bobj.gz", 12043242],
        ["L:\\cachesplittertest\\LiquidSim\\mesh\\fluid_mesh_0010.bobj.gz", 15963525],
        ["L:\\cachesplittertest\\LiquidSim\\mesh\\fluid_mesh_0011.bobj.gz", 20860522],
        ["L:\\cachesplittertest\\LiquidSim\\mesh\\fluid_mesh_0012.bobj.gz", 27235618],
        ["L:\\cachesplittertest\\LiquidSim\\mesh\\fluid_mesh_0013.bobj.gz", 35265390],
        ["L:\\cachesplittertest\\LiquidSim\\mesh\\fluid_mesh_0014.bobj.gz", 45287272],
        ["L:\\cachesplittertest\\LiquidSim\\mesh\\fluid_mesh_0015.bobj.gz", 58029397],
    ],
}

blend_file_size = 1_38_016

max_file_size = 2_000_000_000

size = max_file_size - blend_file_size
for folder in shit:
    n = 0
    while size < max_file_size:
        for files in shit[folder]:
            try:
                print(files)
                print(size)
                size += shit[folder][n][1]
                n += 1
            except IndexError:
                break

