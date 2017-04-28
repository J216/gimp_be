from gimpfu import gimp, pdb
from gimp_be.utils import *
import random, os
from layer import *


def addStamp(options=0, stamp_type="", opacity=90, stamp_folder="", scale=[], position=[]):
    if stamp_folder == "":
        stamp_folder = settings_data['path']['art_folder']+'stamps/'
    stamp_file = ""
    stamp_files = []
    if options == 0:
        if stamp_type == "":
            for file in os.listdir(stamp_folder):
                if os.path.isdir(stamp_folder+file):
                    for sub_file in os.listdir(stamp_folder+file+'/'):
                        if 'png' in sub_file:
                            stamp_files.append(file+'/'+sub_file)
                        if 'jpg' in sub_file:
                            stamp_files.append(file+'/'+sub_file)
                else:
                    if 'png' in file:
                        stamp_files.append(file)
                    if 'jpg' in file:
                        stamp_files.append(file)
        else:
            for file in os.listdir(stamp_folder+stamp_type):
                if 'png' in file:
                    stamp_files.append(stamp_type+file)
                if 'jpg' in file:
                    stamp_files.append(stamp_type+file)
        stamp_file = stamp_folder+random.choice(stamp_files)
    loadLayer(stamp_file)
    image = gimp.image_list()[0]
    active_layer = pdb.gimp_image_get_active_layer(image)
    pdb.gimp_layer_set_opacity(active_layer, opacity)
    if not scale==[]:
        pdb.gimp_layer_scale(active_layer, scale[0], scale[1], 0)
    if position == []:
        pdb.gimp_layer_set_offsets(active_layer, image.width/2-100, image.height/2-100)
    else:
        pdb.gimp_layer_set_offsets(active_layer, position[0], position[1])


def addSticker(options=0, sticker_type="", opacity=90, sticker_folder="", scale=[], position=[]):
    if sticker_folder == "":
        sticker_folder = settings_data['path']['art_folder']+'stickers/'
    addStamp(options, sticker_type, opacity, sticker_folder, scale, position)


def addFractal(options=0, fractal_type="", opacity=90, fractal_folder="", scale=[], position=[]):
    image = gimp.image_list()[0]
    if fractal_folder == "":
        fractal_folder = settings_data['path']['art_folder']+'fractals/'
    if position == []:
        position = [0,0]
    if scale == []:
        scale=[image.width, image.height]
    addStamp(options, fractal_type, opacity, fractal_folder, scale, position)
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
    addStamp(options, photo_type, opacity, photo_folder, scale, position)
    active_layer = pdb.gimp_image_get_active_layer(image)
    pdb.gimp_layer_set_mode(active_layer, random.choice([17,6,15,0,0,0,0,0,0]))

