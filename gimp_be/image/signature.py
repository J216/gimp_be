from gimpfu import gimp, pdb
from gimp_be.utils import *
import random, os
from layer import *


def addSignature(options=0, location="", opacity=40, signature_folder=""):
    if signature_folder == "":
        signature_folder = settings_data['path']['art_folder']+'signature/'
    signature_files = []
    for file in os.listdir(signature_folder):
        if 'png' in file:
            if not 'year' in file:
                signature_files.append(file)
    loadLayer(signature_folder+random.choice(signature_files))
    image = gimp.image_list()[0]
    active_layer = pdb.gimp_image_get_active_layer(image)
    pdb.gimp_layer_set_mode(active_layer, 14)
    pdb.gimp_layer_set_opacity(active_layer, opacity)
    pdb.gimp_layer_scale(active_layer, 120, 120, 0)
    pdb.gimp_layer_set_offsets(active_layer, image.width-130, image.height-215)


def addYear(options=0, location="", opacity=40, signature_folder=""):
    if signature_folder == "":
        signature_folder = settings_data['path']['art_folder']+'signature/'
    year_files = []
    for file in os.listdir(signature_folder):
        if 'png' in file:
            if 'year' in file:
                year_files.append(file)
    loadLayer(signature_folder+random.choice(year_files))
    image = gimp.image_list()[0]
    active_layer = pdb.gimp_image_get_active_layer(image)
    pdb.gimp_layer_set_mode(active_layer, 14)
    pdb.gimp_layer_set_opacity(active_layer, opacity)
    pdb.gimp_layer_scale(active_layer, 90, 90, 0)
    pdb.gimp_layer_set_offsets(active_layer, image.width-100, image.height-100)


def signImage(sign_folder=""):
    addSignature()
    addYear()
