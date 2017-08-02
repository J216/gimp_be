from gimpfu import gimp, pdb, RGB, SELECT_CRITERION_COMPOSITE
from gimp_be.utils.string_tools import *


def imageSetup(w=0, h=0,file_name=""):
    #Create new image from height and width
    global settings_data
    if file_name == "":
        file_name='art.png'
    if w == 0:
        w=int(settings_data['image']['width'])
    if h == 0:
        h=int(settings_data['image']['height'])
    settings_data['image']['title'] = imageTitle(2)
    image = gimp.Image(w, h, RGB)
    gridSpacing = max(image.width, image.height) / 12
    pdb.gimp_image_grid_set_offset(image, image.width/2, image.height/2)
    pdb.gimp_image_grid_set_spacing(image, gridSpacing, gridSpacing)
    pdb.gimp_image_grid_set_style(image, 1)
    settings_data['path']['export_file_name'] = str(settings_data['path']['default_save_path']) + file_name
    new_layer = gimp.Layer(image, "Background", image.width, image.height, 0, 100, 0)
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

