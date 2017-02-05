from gimpfu import pdb, gimp
from gimp_be.image.save import saveJPG, savePNG, saveXCFProject
from gimp_be.network.twitter import tweetText, tweetImage
from gimp_be.image.image import imageSetup
from gimp_be.image.layer import addNewLayer
from random import randrange, choice
from string import letters
from gimp_be.settings import *
settings_data = loadSettings()

def qX():
    """
    quick export png default with unique file name
    :return:
    """
    global settings_data
    settings_data['path']['export_name'] =  str(settings_data['path']['default_save_path'])+'quick_save_'+choice(letters)+choice(letters)+choice(letters)+'-'+str(randrange(0,9))+str(randrange(0,9))+str(randrange(0,9))+str(randrange(0,9))+'.jpg'
    try:
        saveJPG(str(settings_data['path']['export_name']))
        return (True, settings_data['path']['export_name'])
    except:
        return (False, settings_data['path']['export_name'])


def qT():
    global settings_data
    exported=qX()
    if exported[0]:
        tweet = tweetText(0)
    return (tweetImage(tweet, exported[1]) == '200', tweet)



# quick export jpg default with unique file name
def qXJ():
    global settings_data
    saveJPG(settings_data['path']['export_name'])


# quick export png default with unique file name
def qXP():
    image = gimp.image_list()[0]
    global settings_data
    savePNG(settings_data['path']['export_name'], image, 0, 0)


def qP(save_file):
    saveXCFProject(save_file)


# quick set up of default size image
def qS():
    imageSetup()


#quick new layer
def qL():
    image = gimp.image_list()[0]
    drawable = pdb.gimp_image_active_drawable(image)
    addNewLayer()
    pdb.gimp_edit_fill(drawable, 1)

