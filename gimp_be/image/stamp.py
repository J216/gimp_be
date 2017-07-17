from gimpfu import gimp, pdb
from gimp_be.utils import *
import random, os
from layer import *
from collections import Counter


def addResource(options=0, resource_type="rock", opacity=90, resource_folder="", scale=[], position=[]):
    avoid_folders=['brushes','fonts','gradients','mask','overlays','paths','scraps','signature','stamps','stickers','stock-image','templates','tiles']
    if resource_type == "random":
        cl=dict(Counter(os.listdir(settings_data['path']['art_folder']+'resources/'))-Counter(avoid_folders)).keys()
        resource_type = random.choice(cl)
    if resource_folder == "":
        resource_folder = settings_data['path']['art_folder']+'resources/'+resource_type+'/'
    resource_file = ""
    resource_files = []
    if options == 0:
        if resource_type == "":
            for file in os.listdir(resource_folder):
                if os.path.isdir(resource_folder+file):
                    for sub_file in os.listdir(resource_folder+file+'/'):
                        if 'png' in sub_file:
                            resource_files.append(file+'/'+sub_file)
                        if 'jpg' in sub_file:
                            resource_files.append(file+'/'+sub_file)
                else:
                    if 'png' in file:
                        resource_files.append(file)
                    if 'jpg' in file:
                        resource_files.append(file)
        else:
            for file in os.listdir(resource_folder):
                if 'png' in file:
                    resource_files.append(file)
                if 'jpg' in file:
                    resource_files.append(file)
        resource_file = resource_folder+random.choice(resource_files)
    loadLayer(resource_file)
    image = gimp.image_list()[0]
    active_layer = pdb.gimp_image_get_active_layer(image)
    pdb.gimp_layer_set_opacity(active_layer, opacity)
    if scale==[]:
        pdb.gimp_layer_scale(active_layer, image.width, image.height, 0)
    else:
        pdb.gimp_layer_scale(active_layer, scale[0], scale[1], 0)
    if position == []:
        pdb.gimp_layer_set_offsets(active_layer, 0, 0)
    else:
        pdb.gimp_layer_set_offsets(active_layer, position[0], position[1])


def qRes(options=0, sticker_type="random", opacity=90, sticker_folder="", scale=[], position=[]):
    if sticker_folder == "" and not sticker_type == 'random':
        sticker_folder = settings_data['path']['art_folder']+'resources/'+resource_type+'/'
    addResource(options, sticker_type, opacity, sticker_folder, scale, position)


def addSticker(options=0, sticker_type="", opacity=90, sticker_folder="", scale=[], position=[]):
    if sticker_folder == "":
        sticker_folder = settings_data['path']['art_folder']+'stickers/'
    addResource(options, sticker_type, opacity, sticker_folder, scale, position)


def addFractal(options=0, fractal_type="", opacity=90, fractal_folder="", scale=[], position=[]):
    image = gimp.image_list()[0]
    if fractal_folder == "":
        fractal_folder = settings_data['path']['art_folder']+'fractals/'
    if position == []:
        position = [0,0]
    if scale == []:
        scale=[image.width, image.height]
    addResource(options, fractal_type, opacity, fractal_folder, scale, position)
    active_layer = pdb.gimp_image_get_active_layer(image)
    pdb.gimp_layer_set_mode(active_layer, random.choice([17,6,15,0,0,0,0,0,0]))


def addPhoto(options=0, photo_type="", opacity=90, photo_folder="", scale=[], position=[]):
    image = gimp.image_list()[0]
    if photo_folder == "":
        photo_folder = settings_data['path']['art_folder']+'photos/'
    if position == []:
        position = [0,0]
    if scale == []:
        scale=[image.width, image.height]
    addResource(options, photo_type, opacity, photo_folder, scale, position)
    active_layer = pdb.gimp_image_get_active_layer(image)
    pdb.gimp_layer_set_mode(active_layer, random.choice([17,6,15,0,0,0,0,0,0]))


def addSpacePhoto(options=0, type="", opacity=90, space_folder="", scale=[], position=[]):
    image = gimp.image_list()[0]
    if space_folder == "":
        space_folder = settings_data['path']['art_folder']+'space/'
    if position == []:
        position = [0,0]
    if scale == []:
        scale=[image.width, image.height]
    addResource(options, type, opacity, space_folder, scale, position)
    active_layer = pdb.gimp_image_get_active_layer(image)
    pdb.gimp_layer_set_mode(active_layer, random.choice([17,6,15,0,0,0,0,0,0]))


def addScriptDrawing(options=0, type="", opacity=90, script_folder="", scale=[], position=[]):
    image = gimp.image_list()[0]
    if script_folder == "":
        script_folder = settings_data['path']['art_folder']+'script_drawings/'
    if position == []:
        position = [0,0]
    if scale == []:
        scale=[image.width, image.height]
    addResource(options, type, opacity, script_folder, scale, position)
    active_layer = pdb.gimp_image_get_active_layer(image)
    pdb.gimp_layer_set_mode(active_layer, random.choice([17,6,15,0,0,0,0,0,0]))





