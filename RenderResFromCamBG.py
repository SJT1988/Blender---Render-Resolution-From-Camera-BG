bl_info = {
    "name": "Set Render Resolution from Camera BG Image Dimensions",
    "author": "Spencer Trumbore",
    "version": (1,0,1),
    "blender": (4,4,0),
    "location": "Scene Properties > Render",
    "description": "Automatically matches render resolution to camera background image dimensions",
    "category": "Render",
}

import bpy
from bpy.app.handlers import persistent

@persistent
def camera_handler(scene):
    if not scene.camera or not scene.camera.data:
        return
        
    cam_data = scene.camera.data
    if cam_data.background_images:
        bg_img = cam_data.background_images[0].image
        if bg_img:
            scene.render.resolution_x = bg_img.size[0]
            scene.render.resolution_y = bg_img.size[1]

def register():
    bpy.app.handlers.depsgraph_update_post.append(camera_handler)

def unregister():
    if camera_handler in bpy.app.handlers.depsgraph_update_post:
        bpy.app.handlers.depsgraph_update_post.remove(camera_handler)
