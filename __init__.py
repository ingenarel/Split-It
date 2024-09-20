# the following lines of code was written by chatgpt, life sucks, and i don't have the patience to
# learn blender ui atm. if someone wants to help, go ahead.

bl_info = {
    "name": "Cache Directory Splitter",
    "blender": (3, 0, 0),
    "category": "Object",
    "description": "Splits cache data and moves it to the destination directory.",
}

import bpy
from bpy.props import StringProperty
from . import backend  # Importing backend.py from the same directory

class CacheSplitterOperator(bpy.types.Operator):
    bl_idname = "object.cache_splitter"
    bl_label = "Split and Move Cache"
    bl_description = "Splits cache data and moves it to the destination directory."

    # Properties for cache and destination directories
    cache_directory: StringProperty(
        name="Cache Directory",
        description="Directory containing cache data",
        subtype='DIR_PATH',
        default=""
    )

    destination_directory: StringProperty(
        name="Destination Directory",
        description="Directory to move the split data",
        subtype='DIR_PATH',
        default=""
    )

    def execute(self, context):
        # Validate that the directories are not empty
        if not self.cache_directory or not self.destination_directory:
            self.report({'ERROR'}, "Please specify both the cache and destination directories.")
            return {'CANCELLED'}

        try:
            # Example using backend functions, replace with actual calls to your backend
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

        # Access the operator and display input fields
        layout.prop(context.scene, "cache_splitter_cache_directory")
        layout.prop(context.scene, "cache_splitter_destination_directory")

        # Draw the operator button
        op = layout.operator("object.cache_splitter", text="Split and Move Cache")
        op.cache_directory = context.scene.cache_splitter_cache_directory
        op.destination_directory = context.scene.cache_splitter_destination_directory


def register():
    bpy.utils.register_class(CacheSplitterOperator)
    bpy.utils.register_class(CacheSplitterPanel)

    # Add properties to Blender's scene to use in the UI
    bpy.types.Scene.cache_splitter_cache_directory = StringProperty(
        name="Cache Directory",
        description="Directory containing cache data",
        subtype='DIR_PATH',
        default=""
    )

    bpy.types.Scene.cache_splitter_destination_directory = StringProperty(
        name="Destination Directory",
        description="Directory to move the split data",
        subtype='DIR_PATH',
        default=""
    )


def unregister():
    bpy.utils.unregister_class(CacheSplitterOperator)
    bpy.utils.unregister_class(CacheSplitterPanel)

    # Remove custom properties
    del bpy.types.Scene.cache_splitter_cache_directory
    del bpy.types.Scene.cache_splitter_destination_directory


if __name__ == "__main__":
    register()
