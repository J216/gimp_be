
def qX():
    """
    quick export png default with unique file name
    :return:
    """
    from gimp_be.image.save import saveJPG
    from random import randrange, choice
    from string import letters
    global settings_data
    settings_data['path']['export_name'] = str(settings_data['path']['default_save_path'])+'quick_save_'+choice(letters)+choice(letters)+choice(letters)+'-'+str(randrange(0,9))+str(randrange(0,9))+str(randrange(0,9))+str(randrange(0,9))+'.jpg'
    try:
        saveJPG(str(settings_data['path']['export_name']))
        return (True, settings_data['path']['export_name'])
    except:
        return (False, settings_data['path']['export_name'])


def qT():
    from gimp_be.settings.settings import loadSettings, settings_data
    from gimp_be.network.twitter import tweetText, tweetImage
    loadSettings()
    exported=qX()
    if exported[0]:
        tweet = tweetText(0)
        return tweetImage(tweet, exported[1]) == '200'
    else:
        return False


# quick export jpg default with unique file name
def qXJ():
    from gimp_be.image.save import saveJPG
    global export_file_name
    saveJPG(export_file_name)


# quick export png default with unique file name
def qXP():
    from gimpfu import gimp
    from gimp_be.image.save import savePNG
    image = gimp.image_list()[0]
    global export_file_name
    savePNG(export_file_name, image, 0, 0)


def qP(save_file):
    from gimp_be.image.save import saveXCFProject
    saveXCFProject(save_file)


# quick set up of default size image
def qS():
    from gimp_be.image.image import imageSetup
    imageSetup()


#quick new layer
def qL():
    from gimpfu import pdb, gimp
    from gimp_be.image.layer import addNewLayer
    image = gimp.image_list()[0]
    drawable = pdb.gimp_image_active_drawable(image)
    addNewLayer()
    pdb.gimp_edit_fill(drawable, 1)

