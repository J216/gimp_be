from string import letters
from gimpfu import pdb, CLIP_TO_IMAGE, gimp
import datetime
import re
import os
import random


def saveJPG(fn, comment=""):
    time_stamp = datetime.datetime.now()
    image = gimp.image_list()[0]
    new_image = pdb.gimp_image_duplicate(image)
    layer = pdb.gimp_image_merge_visible_layers(new_image, CLIP_TO_IMAGE)
    if comment=="":
        comment = "Digital Art - " + str(time_stamp)
    try:
        pdb.file_jpeg_save(new_image, layer, fn, fn, .65, 0, 0, 0, comment, 2, 1, 0, 0)
        pdb.gimp_image_delete(new_image)
        return (True, fn,comment)
    except:
        return (False, fn,comment)

def saveXCFProject(fn):
    # save project file of current image
    image = gimp.image_list()[0]
    drawable = pdb.gimp_image_active_drawable(image)
    try:
        pdb.gimp_xcf_save(1, image, drawable, fn, fn)
        return (True, fn)
    except:
        return (False, fn)

def savePNG(fn,comment=""):
    image = gimp.image_list()[0]
    drawable = pdb.gimp_image_active_drawable(image)
    #replace slash with forward
    fn=fn.replace('\\','/')
    if comment == "":
        comment="NACHO Comment Activated !!!"
    #SAVE FILE WITH UNIQUE NAME
    new_image = pdb.gimp_image_duplicate(image)
    layer = pdb.gimp_image_merge_visible_layers(new_image, CLIP_TO_IMAGE)
    export_fn = fn
    pdb.file_png_save2(image, drawable, fn, fn, 0, 7, 0, 0, 0, 0, 0, 0, 0)
    pdb.gimp_image_delete(new_image)

def saveGIF(fn,delay=100):
    image = gimp.image_list()[0]
    drawable = pdb.gimp_image_active_drawable(image)
    fn=fn.replace('\\','/')
    export_fn = fn
    try:
        pdb.gimp_convert_indexed(image, 2, 2, 256, 1, 0, "Computer Jones' Magic Palette")
    except:
        print "already indexed"
    try:
        pdb.file_gif_save(image, drawable, fn, fn, 0, 1, delay, 0)
        return (True,fn,comment)
    except:
        return (False,fn)

