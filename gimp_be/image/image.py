from gimpfu import gimp, pdb, RGB, SELECT_CRITERION_COMPOSITE
from gimp_be.utils.string_tools import *


def imageSetup(w=2560, h=1920):
    """
    #Create new image from height and width
    :param w:
    :param h:
    :return:
    """
    global settings_data
    global export_file_name
    global export_path
    global pureName
    global x_center
    global y_center
    global title
    global exported
    global project_saved
    project_saved=False
    exported=False

    title = imageTitle(2)
    image = gimp.Image(w, h, RGB)
    width = image.width
    height = image.height
    gridSpacing = max(width, height) / 24
    pdb.gimp_image_grid_set_offset(image, x_center, y_center)
    pdb.gimp_image_grid_set_spacing(image, gridSpacing, gridSpacing)
    pdb.gimp_image_grid_set_style(image, 1)
    x_center = width / 2
    y_center = height / 2
    export_file_name = default_save_path + 'script-draw.png'
    new_layer = gimp.Layer(image, "Background", width, height, 0, 100, 0)
    pdb.gimp_image_add_layer(image, new_layer, 0)
    drawable = pdb.gimp_image_active_drawable(image)
    pdb.gimp_context_set_foreground((255, 255, 255))
    pdb.gimp_edit_bucket_fill_full(drawable, 0, 0, 100, 0, 1, 0, SELECT_CRITERION_COMPOSITE, 0, 0)
    pdb.gimp_context_set_foreground((0, 0, 0))
    pdb.gimp_context_set_background((255, 255, 255))
    gimp.Display(image)


# update active image sets global var to current draw area, can't set image to active as of now...
def updateImage():
    pdb.gimp_displays_flush()



# Close all - working but just guesses displays
def closeAll():
    for x in range(0, 500):
        gimp.delete(gimp._id2display(x))
