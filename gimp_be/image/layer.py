from gimpfu import gimp, pdb
from gimp_be.utils import *
import random, os

def addNewLayer(opacity=100, msk=0, opt=1):
    """
    Add new layer par image, int opacity, bool mask or no mask
    :param image:
    :param opacity:
    :param msk:
    :param opt:
    :return:
    """
    image = gimp.image_list()[0]
    new_layer = gimp.Layer(image, imageTitle(0), image.width, image.height, 0, opacity, 0)
    pdb.gimp_image_add_layer(image, new_layer, 0)
    pdb.gimp_image_set_active_layer(image, new_layer)
    drawable = pdb.gimp_image_active_drawable(image)
    if msk:
        newMask = new_layer.create_mask(0)
        pdb.gimp_image_add_layer_mask(image, new_layer, newMask)
    if opt == 0:
        pdb.plug_in_colortoalpha(image, drawable, (0, 0, 0))
    elif opt == 1:
        pdb.gimp_edit_fill(drawable, 1)


def loadLayer(image_file):
    """
    load image to layer
    :param image_file:
    :return:
    """
    image = gimp.image_list()[0]
    try:
        new_layer = pdb.gimp_file_load_layer(image, image_file)
        pdb.gimp_image_add_layer(image, new_layer, 0)
        return 1
    except:
        return 0


def loadDirLayer(image_folder, opt=0):
    """
    load images as layers from folder multiply options 11-random pick 7-scale layer 3-random mode 2-random opacity
    :param image_folder:
    :param opt:
    :return:
    """
    image = gimp.image_list()[0]
    drawable = pdb.gimp_image_active_drawable(image)
    results = []
    image_files =[]
    random_opt=True
    if opt%19==0:
        random_opt=random.choice((True,False,False))
    for file in os.listdir(image_folder):
        if '.jpg' in file or '.JPG' in file:
            image_files.append(file)
    if (len(image_files) < 2):
        # 'folder not found'
        return False
    elif  len(image_files) > 8:
        # opt 5 pick random file from fold
        for x in range(0,4):
            if opt%11==0:
                results.append(loadLayer(image_folder + random.choice(image_files)))
            else:
                results.append(loadLayer(image_folder + image_files[x]))
            if opt%7==0:
                pdb.gimp_layer_scale(pdb.gimp_image_get_active_layer(image), image.width, image.height, 0)
            if opt%3==0:
                pdb.gimp_layer_set_mode(pdb.gimp_image_get_active_layer(image), random.randrange(0,25))
            if opt%2==0:
                pdb.gimp_layer_set_opacity(pdb.gimp_image_get_active_layer(image), random.randrange(25,85))
            if opt%17==0 and random_opt:
                loadImageMask(image_folder + random.choice(image_files))
                if opt%19==0:
                    random_opt=random.choice((True,False,False))
            if opt%13==0 and random_opt:
                active_layer=pdb.gimp_image_get_active_layer(image)
                if opt%17==0:
                    pdb.gimp_image_remove_layer_mask(image, active_layer, 0)
                layer = pdb.gimp_image_get_active_layer(image)
                mask = pdb.gimp_layer_create_mask(layer, 0)
                pdb.gimp_layer_add_mask(layer, mask)
                editLayerMask(1)
                plasma_par = {'Image': image, 'Draw': drawable, 'Seed': random.randrange(1, 1000), 'Turbulence': random.choice((0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 1.0, 1.5, 1.1, 1.4, 1.8, 2.0, 2.7))}
                pdb.plug_in_plasma(plasma_par['Image'], plasma_par['Draw'], plasma_par['Seed'], plasma_par['Turbulence'])
                editLayerMask(0)
                if opt%19==0:
                    random_opt=random.choice((True,False,False))
        return True
    else:
        for file in image_files:
            results.append(loadLayer(image_folder + file))
            if opt%7==0:
                pdb.gimp_layer_scale(pdb.gimp_image_get_active_layer(image), image.width, image.height, 0)
            if opt%3==0:
                pdb.gimp_layer_set_mode(pdb.gimp_image_get_active_layer(image), random.randrange(0,25))
            if opt%2==0:
                pdb.gimp_layer_set_opacity(pdb.gimp_image_get_active_layer(image), random.randrange(25,85))
            if opt%17==0 and random_opt:
                loadImageMask(image_folder + random.choice(image_files))
                if opt%19==0:
                    random_opt=random.choice((True,False,False))
            if opt%13==0 and random_opt:
                active_layer=pdb.gimp_image_get_active_layer(image)
                if opt%17==0:
                    pdb.gimp_image_remove_layer_mask(image, active_layer, 0)
                layer = pdb.gimp_image_get_active_layer(image)
                mask = pdb.gimp_layer_create_mask(layer, 0)
                pdb.gimp_layer_add_mask(layer, mask)
                editLayerMask(1)
                plasma_par = {'Image': image, 'Draw': drawable, 'Seed': random.randrange(1, 1000), 'Turbulence': random.choice((0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 1.0, 1.5, 1.1, 1.4, 1.8, 2.0, 2.7))}
                pdb.plug_in_plasma(plasma_par['Image'], plasma_par['Draw'], plasma_par['Seed'], plasma_par['Turbulence'])
                editLayerMask(0)
                if opt%19==0:
                    random_opt=random.choice((True,False,False))
        return True


def layerScaleAll():
    """
    scale all layers to canvas size
    :return:
    """
    image = gimp.image_list()[0]
    drawable = pdb.gimp_image_active_drawable(image)
    all_layers = image.layers
    for l in all_layers:
        pdb.gimp_layer_scale(l, image.width, image.height, 0)


def flatten(image):
    """
    flatten image
    :param image:
    :return:
    """
    image = gimp.image_list()[0]
    pdb.gimp_image_flatten(image)


def editLayerMask(edit):
    """
    set current layer editable
    :param edit:
    :return:
    """
    image = gimp.image_list()[0]
    edit_layer = 0
    pdb.gimp_image_set_active_layer(image, image.layers[edit_layer])
    pdb.gimp_layer_set_edit_mask(image.layers[edit_layer], edit)


def loadImageMask(file_name):
    """
    load image as mask layer
    :param file_name:
    :return:
    """
    image = gimp.image_list()[0]
    active_layer=pdb.gimp_image_get_active_layer(image)
    layer = pdb.gimp_file_load_layer(image, file_name)
    pdb.gimp_image_add_layer(image, layer, 0)
    pdb.gimp_layer_scale(layer, image.width, image.height,0)
    mask = pdb.gimp_layer_create_mask(layer, 5)
    pdb.gimp_layer_add_mask(active_layer, mask)
    pdb.gimp_image_remove_layer(image, layer)
    editLayerMask(0)


def clearLayer():
    """
    clear active layer
    :return:
    """
    image = gimp.image_list()[0]
    drawable = pdb.gimp_image_active_drawable(image)
    pdb.gimp_selection_all(image)
    pdb.gimp_edit_clear(drawable)
