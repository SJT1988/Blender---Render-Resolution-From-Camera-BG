# Blender---Render-Resolution-From-Camera-BG
Blender add-on that automatically sets the render resolution to the active camera's bg image dimensions (if it has one)

## Use Case
Suppose you are trying build a scene based on reference images, such as from photographs used as camera background images with the [fspy-addon](https://github.com/stuffmatic/fSpy-Blender). The imported cameras may have background images that are different sizes. When you switch between these cameras, the bounds of the cameras may not fit the background image dimensions because the Render Resolution does not change when you switch cameras. You have to manually inspect the active camera's background image dimensions and change the render resolution yourself each time.

This addon will automatically set the Render Resolution to match the dimensions of hte active camera's background image, if it has one.

## Instructions
1. Download the python file attached to this repository.
2. Open Blender and go to
Edit -> Preferences -> Add-ons -> (top-right dropdown menu) -> Install from Disk
3. Choose the python file you downloaded.
4. Activate the addon by checking the box next to **Set Render Resolution from Camera BG Image Dimensions**.

This addon has no UI, it works automatcially.

You can test it by creating two cameras with background images that have different dimensions.
Open the Output Properties panel and look at Format -> Resolution. The X and Y dimensions will update automatically when you switch the active camera.
Nothing will happen if you set a camera without a background image as the active camera.
