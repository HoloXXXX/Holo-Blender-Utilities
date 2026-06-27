bl_info = {
        'name':'Holo Utilities',
        'author': 'Holo',
        'version': (0,1,0), # Update data.py version string when updating version #
        'blender': (5,0,0),
        'location': '3dView',
        'category': 'Pipeline',
        'description': 'A set of convenience functions for Blender',
        }

if 'bpy' in locals():
    import importlib
    importlib.reload(general_functions)
    print('Holo Utilities successfully reloaded!')
else:
    import bpy
    from . import (
        general_functions,
    )

def register():
    general_functions.register()

def unregister():
    general_functions.unregister()

if __name__ == '__main__':
    register()