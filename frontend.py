# the following lines of code was written by chatgpt, life sucks, and i don't have the patience to
# learn blender ui atm. if someone wants to help, go ahead.

bl_info = {
    "name": "Cache Directory Splitter",
    "blender": (3, 0, 0),
    "category": "Object",
    "description": "Splits cache data and moves it to the destination directory.",
}

import bpy, backend
from bpy.props import StringProperty

class CacheSplitterOperator(bpy.types.Operator):
    bl_idname = "object.cache_splitter"
    bl_label = "Split and Move Cache"
    bl_description = "Splits cache data and moves it to the destination directory."

    cache_directory: StringProperty(
        name="Cache Directory",
        description="Directory containing cache data",
        subtype='DIR_PATH'
    )

    destination_directory: StringProperty(
        name="Destination Directory",
        description="Directory to move the split data",
        subtype='DIR_PATH'
    )

    def execute(self, context):
        # Call the main logic using the provided paths.
        try:
            # This follows your main function structure, adapt according to your actual backend setup.
            splitted_data = backend.split_parser(
                backend.split_func(
                    backend.partition_data(
                        backend.data_maker_function(
                            self.cache_directory
                        )
                    )
                )
            )

            backend.move(splitted_data, self.cache_directory, self.destination_directory)

            self.report({'INFO'}, "Cache data split and moved successfully!")
        except Exception as e:
            self.report({'ERROR'}, f"An error occurred: {str(e)}")
            return {'CANCELLED'}

        return {'FINISHED'}


class CacheSplitterPanel(bpy.types.Panel):
    bl_label = "Cache Splitter"
    bl_idname = "OBJECT_PT_cache_splitter"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Cache Splitter'

    def draw(self, context):
        layout = self.layout
        layout.label(text="Cache Directory Splitter")

        # Draw the operator with its properties
        layout.operator("object.cache_splitter", text="Split and Move Cache")


def register():
    bpy.utils.register_class(CacheSplitterOperator)
    bpy.utils.register_class(CacheSplitterPanel)


def unregister():
    bpy.utils.unregister_class(CacheSplitterOperator)
    bpy.utils.unregister_class(CacheSplitterPanel)


if __name__ == "__main__":
    register()
