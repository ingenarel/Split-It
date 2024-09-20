import backend
# import bpy

def main():
    # cache_directory = "/mnt/D/System files(D)/windows files/cachesplittertest/LiquidSim"
    # destination_directory = "/mnt/D/System files(D)/windows files/cachesplittertest/test"
    cache_folder_size = 2147483648
    splitted_data = backend.split_parser(
        backend.split_func(
            backend.partition_data(
                backend.data_maker_function(
                    cache_directory
                )
            ),
            cache_folder_size
        )
    )

    backend.move(splitted_data, cache_directory, destination_directory)

if __name__ == "__main__":
    main()
    print("all files copied successfully!")
    # 1 gb  = 1000000000 bytes
    # 1 gib = 1073741824 bytes

