from gimpfu import pdb, gimp
from random import randrange, choice
from string import letters
from gimp_be.image.save import saveJPG, savePNG, saveXCFProject
from gimp_be.network import *
from gimp_be.image.image import imageSetup
from gimp_be.image.layer import addNewLayer
from gimp_be.settings import *
import datetime as dt
from gimp_be import settings_data
from gimp_be.image.exif import *
from time import sleep
from gimp_be.image.exif import qXDT

def qS():
    # quick set up of default size image
    imageSetup()

def qL():
    # quick new layer
    addNewLayer()
    image = gimp.image_list()[0]
    drawable = pdb.gimp_image_active_drawable(image)
    pdb.gimp_edit_fill(drawable, 1)

def qXJ(comment=""):
    # quick export jpg default with unique file name
    from gimp_be.network.twitter import tweetText
    global settings_data
    settings_data['path']['export_name'] =  str(settings_data['path']['default_save_path'])+'art-'+dt.datetime.now().strftime('%Y%m%d%H%M%S')+'-'+choice(letters)+choice(letters)+choice(letters)+'.jpg'
    if comment=="":
        comment=tweetText(0)
    saved=saveJPG(settings_data['path']['export_name'],comment)
    qXDT(saved[1],comment)
    sleep(1)
    return saved

def qXP(comment=""):
    # quick export png default with unique file name
    global settings_data
    settings_data['path']['export_name'] =  str(settings_data['path']['default_save_path'])+'art-'+dt.datetime.now().strftime('%Y%m%d%H%M%S')+'-'+choice(letters)+choice(letters)+choice(letters)+'.png'
    from gimp_be.network.twitter import tweetText
    image = gimp.image_list()[0]
    if comment=="":
        comment=tweetText(0)
    saved = savePNG(settings_data['path']['export_name'])
    qXDT(saved[1],comment)
    return saved

def qG(comment="",delay=100):
    # quick export png default with unique file name
    global settings_data
    settings_data['path']['export_name'] =  str(settings_data['path']['default_save_path'])+'animation-'+dt.datetime.now().strftime('%Y%m%d%H%M%S')+'-'+choice(letters)+choice(letters)+choice(letters)+'.gif'
    from gimp_be.network.twitter import tweetText
    image = gimp.image_list()[0]
    if comment=="":
        comment=tweetText(0)
    saved = saveGIF(settings_data['path']['export_name'],delay)
    qXDT(saved[1],comment)
    return saved

def qP(fn=""):
    # quick save project
    global settings_data
    if fn=="":
        fn =  str(settings_data['path']['project_folder'])+'project-'+dt.datetime.now().strftime('%Y%m%d%H%M%S')+'-'+choice(letters)+choice(letters)+choice(letters)+'.xcf'
    saveXCFProject(fn)

def qX(comment=""):
    # quick export to prefered file type
    global settings_data
    export_modes = {"qXJ" : qXJ,
                    "qXP" : qXP,
                    "qG" : qG}
    try:
        mode=str(settings_data['image']['export_mode'])
        return export_modes[mode](comment)
    except:
        mode='qXJ'
        return export_modes[mode](comment)

def qT():
    # generate tweet then qX() then send tweet return results
    from gimp_be.network.twitter import tweetText, tweetImage
    global settings_data
    tweet = tweetText(0)
    exported=qX(comment=tweet)
    sleep(5)
    return (tweetImage(tweet, exported[1]) == '200', tweet)

def qTG():
    # generate tweet then qX() then send tweet return results
    from gimp_be.network.twitter import tweetText, tweetImage
    global settings_data
    tweet = tweetText(0)
    exported=qG()
    return (tweetImage(tweet, exported[1]) == '200', tweet)

