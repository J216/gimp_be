from gimpfu import gimp, pdb
from gimp_be.utils import *
from gimp_be.draw import *
from gimp_be.network import *
from gimp_be.image import *
from time import sleep
from gimp_be.network.twitter import tweetText, tweetImage
import random
from random import randrange



def paint():
    # Full auto painting
    global settings_data
    width = int(settings_data['image']['width'])
    height = int(settings_data['image']['height'])
    x_center = width/2
    y_center = height/2
    qS()
    image = gimp.image_list()[0]
    randomBlend()
    loop_range = range(0, random.choice((3, 4, 5, 6)))
    loop_range.reverse()
    title = imageTitle(2)
    for x in loop_range:
        # 1. add layer
        layer_add_par = {'opacity': 100, 'msk': 1}
        addNewLayer(**layer_add_par)
        layer_mode_par = {'layer': pdb.gimp_image_get_active_layer(image), 'mode': random.randrange(0, 25)}
        pdb.gimp_layer_set_mode(layer_mode_par['layer'], layer_mode_par['mode'])
        editLayerMask(0)
        drawable = pdb.gimp_image_active_drawable(image)
        # 1. paint layer
        if random.choice((0, 1, 1, 1)):
            plasma_par = {'Image': image, 'Draw': drawable, 'Seed': random.randrange(1, 1000),
                          'Turbulence': random.choice(
                                  (0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 1.0, 1.5, 1.1, 1.4, 1.8, 2.0, 2.7))}
            pdb.plug_in_plasma(plasma_par['Image'], plasma_par['Draw'], plasma_par['Seed'], plasma_par['Turbulence'])
        if random.choice((0, 1, 1, 1, 1)):
            drawRays_par = {'Number': random.choice((5, 10, 50, 100, 300)),
                            'Length': random.choice((80, 160, 240, 400, height / 4, height / 3, height / 2)),
                            'X': random.choice((width / 2, width / 3, width / 4)),
                            'Y': random.choice((height / 4, height / 3, height / 2))}
            drawRays(drawRays_par['Number'], drawRays_par['Length'], drawRays_par['X'], drawRays_par['Y'])
        # 1. mask edit
        editLayerMask(1)
        drawable = pdb.gimp_image_active_drawable(image)
        plasma_par = {'Image': image, 'Draw': drawable, 'Seed': random.randrange(1, 1000), 'Turbulence': random.choice(
                (0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 1.0, 1.5, 1.1, 1.4, 1.8, 2.0, 2.7))}
        pdb.plug_in_plasma(plasma_par['Image'], plasma_par['Draw'], plasma_par['Seed'], plasma_par['Turbulence'])
        if random.choice((0, 1, 1, 1, 1)):
            drawRays_par = {'Number': random.choice((5, 10, 50, 100, 300)),
                            'Length': random.choice((80, 160, 240, 400, height / 4, height / 3, height / 2)),
                            'X': random.choice((width / 2, width / 3, width / 4)),
                            'Y': random.choice((height / 4, height / 3, height / 2))}
            drawRays(drawRays_par['Number'], drawRays_par['Length'], drawRays_par['X'], drawRays_par['Y'])
        editLayerMask(0)
        qX()
        # 2. add layer
        layer_add_par = {'opacity': random.randrange(70, 100), 'msk': 1}
        addNewLayer(**layer_add_par)
        layer_mode_par = {'layer': pdb.gimp_image_get_active_layer(image), 'mode': random.randrange(0, 25)}
        pdb.gimp_layer_set_mode(layer_mode_par['layer'], layer_mode_par['mode'])
        editLayerMask(0)
        # 2. paint layer
        if x % 4 == 0:
            drawBars_par = {'Number': random.choice((2, 3, 4, 5, 6, 7, 8, 12, 16, 32, 64, 128)),
                            'Mode': random.choice((0, 0, 3))}
            drawBars(drawBars_par['Number'], drawBars_par['Mode'])
        randomBlend()
        # 2. mask edit
        editLayerMask(1)
        image = gimp.image_list()[0]
        drawable = pdb.gimp_image_active_drawable(image)
        plasma_par = {'Image': image, 'Draw': drawable, 'Seed': random.randrange(1, 1000), 'Turbulence': random.choice(
                (0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 1.0, 1.5, 1.1, 1.4, 1.8, 2.0, 2.7))}
        pdb.plug_in_plasma(plasma_par['Image'], plasma_par['Draw'], plasma_par['Seed'], plasma_par['Turbulence'])
        randomBlend()
        editLayerMask(0)
        image = gimp.image_list()[0]
        # 3. add layer
        layer_add_par = {'opacity': random.randrange(55, 100), 'msk': 1}
        addNewLayer(**layer_add_par)
        layer_mode_par = {'layer': pdb.gimp_image_get_active_layer(image), 'mode': random.randrange(0, 25)}
        pdb.gimp_layer_set_mode(layer_mode_par['layer'], layer_mode_par['mode'])
        if random.choice((0, 1)):
            fill_par = {'num': random.choice((1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 3, 3, 3, 4, 5, 8, 9, 12, 24, 64, 128, 512)),
                        'size': random.randrange(15, height), 'opt': 3, 'sq': random.choice((0, 1))}
            randomCircleFill(**fill_par)
        if random.choice((0, 1)):
            fill_par = {'num': random.choice((1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 3, 3, 3, 4, 5, 8, 9, 12, 24, 64, 128, 512)),
                        'size': random.randrange(15, height), 'opt': 3, 'sq': random.choice((0, 1))}
            randomRectFill(**fill_par)
        editLayerMask(0)
        # 3. paint layer
        if random.choice((0, 1, 1, 1, 1)):
            drawRays_par = {'rays': random.choice((3, 5, 10, 15, 30, 45)), 'rayLength': random.choice(
                    (width / 4, width / 3, width / 2, 4 * (width / 5), 3 * (width / 4), 2 * (width / 3))),
                            'centerX': random.choice((width / 4, width / 3, width / 2, 4 * (width / 5), 3 * (width / 4),
                                                      2 * (width / 3))), 'centerY': random.choice(
                        (height / 4, height / 3, height / 2, 4 * (height / 5), 3 * (height / 4), 2 * (height / 3)))}
            drawRays(**drawRays_par)
        if random.choice((0, 1)):
            fill_par = {'num': random.choice((1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 3, 3, 3, 4, 5, 8, 9, 12, 24, 64, 128, 512)),
                        'size': random.randrange(15, height), 'opt': 3, 'sq': random.choice((0, 1))}
            randomCircleFill(**fill_par)
        if random.choice((0, 1)):
            fill_par = {'num': random.choice((1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 3, 3, 3, 4, 5, 8, 9, 12, 24, 64, 128, 512)),
                        'size': random.randrange(15, height), 'opt': 3, 'sq': random.choice((0, 1))}
            randomRectFill(**fill_par)
        if random.choice((0, 1)):
            randomBrush()
        if random.choice((0, 1)):
            randomDynamics()
        if random.choice((0, 1, 1, 1, 1)):
            brushSize(50)
            drawTree_par = {'x1': random.randrange(width / 4, 3 * (width / 4)),
                            'y1': random.randrange(height / 4, 3 * (height / 4)), 'angle': random.randrange(0, 360),
                            'depth': random.randrange(5, 7)}
            drawOddTree(**drawTree_par)  # x1, y1, angle, depth
        if random.choice((0, 1, 1, 1, 1)):
            if random.choice((0, 1, 1, 1, 1)):
                brushSize(random.randrange(20, (height / 3)))
            if random.choice((0, 1, 1, 1, 1)):
                brushColor()
            drawRays_par = {'rays': random.choice((10, 50, 100)),
                            'rayLength': random.choice((80, 160, 240, 400, height / 4, height / 3, height / 2)),
                            'centerX': random.choice(
                                    ((x_center + x_center / 2), x_center, x_center / 2, x_center / 3, x_center / 4)),
                            'centerY': random.choice(
                                    ((x_center + x_center / 2), x_center, x_center / 2, x_center / 3, x_center / 4))}
            drawRays(**drawRays_par)
        # 3. mask edit
        editLayerMask(1)
        image = gimp.image_list()[0]
        drawable = pdb.gimp_image_active_drawable(image)
        plasma_par = {'Image': image, 'Draw': drawable, 'Seed': random.randrange(1, 1000), 'Turbulence': random.choice(
                (0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 1.0, 1.5, 1.1, 1.4, 1.8, 2.0, 2.7))}
        pdb.plug_in_plasma(plasma_par['Image'], plasma_par['Draw'], plasma_par['Seed'], plasma_par['Turbulence'])
        # 4. add layer
        layer_add_par = {'opacity': random.randrange(55, 100), 'msk': 1}
        addNewLayer(**layer_add_par)
        layer_mode_par = {'layer': pdb.gimp_image_get_active_layer(image), 'mode': random.randrange(0, 25)}
        pdb.gimp_layer_set_mode(layer_mode_par['layer'], layer_mode_par['mode'])
        brushSize(-1)
        editLayerMask(0)
        # 4. paint layer
        if random.choice((0, 1, 1, 1, 1)):
            drawSin_par = {
                'bar_space': random.choice((16, 18, 19, 20, 21, 51, 52, 53, 54, 56, 55, 57, 58, 59)),
                'bar_length': random.choice((10, 100, height / 3)),
                'mag': random.choice((40, 69, 120, 200, 300, 400, height / 2)),
                'x_offset': 0,
                'y_offset': random.randrange(height / 12, height)
            }
            drawSinWave(**drawSin_par)
        if random.choice((0, 1, 1, 1, 1)):
            drawForest(random.randrange(15, 64), 0)
        if random.choice((0, 1, 1, 1, 1)):
            # 5. mask edit
            editLayerMask(1)
            image = gimp.image_list()[0]
            drawable = pdb.gimp_image_active_drawable(image)
            plasma_par = {'Image': image, 'Draw': drawable, 'Seed': random.randrange(1, 1000),
                          'Turbulence': random.choice(
                                  (0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 1.0, 1.5, 1.1, 1.4, 1.8, 2.0, 2.7))}
            pdb.plug_in_plasma(plasma_par['Image'], plasma_par['Draw'], plasma_par['Seed'], plasma_par['Turbulence'])
            if random.choice((0, 1)):
                fill_par = {
                    'num': random.choice((1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 3, 3, 3, 4, 5, 8, 9, 12, 24, 64, 128, 512)),
                    'size': random.randrange(15, height), 'opt': 3, 'sq': random.choice((0, 1))}
                randomCircleFill(**fill_par)
            if random.choice((0, 1)):
                fill_par = {
                    'num': random.choice((1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 3, 3, 3, 4, 5, 8, 9, 12, 24, 64, 128, 512)),
                    'size': random.randrange(15, height), 'opt': 3, 'sq': random.choice((0, 1))}
                randomRectFill(**fill_par)
        flatten(image)
    image = gimp.image_list()[0]
    drawable = pdb.gimp_image_active_drawable(image)
    canvas_par = {'Image': image, 'Draw': drawable, 'Direction': 1, 'Depth': 1}
    pdb.plug_in_apply_canvas(canvas_par['Image'], canvas_par['Draw'], canvas_par['Direction'], canvas_par['Depth'])

def dimensionality(folder='',tweet=0):
    # automated creation of dimensionality study piece
    global settings_data
    if folder == '':
        folder = settings_data['path']['art_folder']+"resources/"+random.choice(["photos","fractals","plants","rock"])+"/"
    loadDirLayer(folder,9699690)

def fractalMasking():
    # fractal layered wtih tile masks
    if random.choice([0,0,0,0,1,1,1]):
        image=gimp.image_list()[0]
        drawable = pdb.gimp_image_active_drawable(image)
        pdb.gimp_invert(drawable)
    for x in range(random.choice([3,6,7,8,9,10])):
        addFractal()
        tile([random.choice([1,2,3,4,5,6,7,8,12]),random.choice([1,2,3,4,5,6,7,8,12])])

def randomMasking():
    # tile mask from random resources
    image=gimp.image_list()[0]
    drawable = pdb.gimp_image_active_drawable(image)
    if random.choice([0,0,0,0,1,1,1]):
        pdb.gimp_invert(drawable)
    for x in range(random.choice([13,6,7,8,9,10])):
        qRes(opacity=random.choice([13,25,33,50,66,75,85]))
        layer_mode_par = {'layer': pdb.gimp_image_get_active_layer(image), 'mode': random.randrange(0, 25)}
        pdb.gimp_layer_set_mode(layer_mode_par['layer'], layer_mode_par['mode'])
        if 25 > random.randrange(0,100):
            tile([random.randrange(1,12),random.randrange(1,12)])

def hybridMasking(option="SpBGsp", noise=0.3):
    # masking resources with lots of options
    drawInkBlot()
    if 'SpBG' in option:
        addSpacePhoto(opacity=50)
    if "Re" in option:
        applyEffect()
    for x in range(4,(10+random.randrange(int(noise*5*-1),int(noise*10)))):
        if 'ph'in option:
            qRes()
            if "Re" in option:
                applyEffect()
            tile([random.randrange(1,12),random.randrange(1,12)])
            if "Re" in option:
                editLayerMask(1)
                applyEffect()
                editLayerMask(0)
        if 'sc' in option:
            qRes()
            if "Re" in option:
                applyEffect()
            tile([random.randrange(1,12),random.randrange(1,12)])
            if "Re" in option:
                editLayerMask(1)
                applyEffect()
                editLayerMask(0)
        if 'sp' in option:
            qRes()
            if "Re" in option:
                applyEffect()
            tile([random.randrange(1,12),random.randrange(1,12)])
            if "Re" in option:
                editLayerMask(1)
                applyEffect()
                editLayerMask(0)
        if 'fr' in option:
            qRes()
            if "Re" in option:
                applyEffect()
            tile([random.randrange(1,12),random.randrange(1,12)])
            if "Re" in option:
                editLayerMask(1)
                applyEffect()
                editLayerMask(0)

def spikeDif():
    # draw spike ball or random rays
    spikeBallStack(depth=20)
    if random.choice([0,0,0,0,0,1,1,1,1]):
        applyEffect()

def inkBlot():
    # draq basic ink blot
    inkBlotStack()
    applyEffect()

def skeleton(type="",num=10,delay=10,options={"tweet":1, "study_name":"Multifunctional Study"}):
    # function to take care of exporting and tweet all images produces
    automations = {"spikeDif" : spikeDif,
                    "inkBlot" : inkBlot,
                    "hybridMasking" : hybridMasking,
                    "paint" : paint,
                    "fractalMasking" : fractalMasking,
                    "randomMasking" : randomMasking}
    for i in range(0,num):
        qS()
        # ################## #
        # This is the nugget #
        # ################## #
        if type == "":
            automations[random.choice(automations.keys())]()
        else:
            automations[type]()
        if options["tweet"]:
            signImage()
            tweet=imageTitle(2)+'\n by Jared Haer\n'+options["study_name"]+'\n'
            tweetImage(tweet+hashtagString(len(tweet)),qX()[1])
            closeAll()
            sleep(delay)
        else:
            qX()
            closeAll()

def doWeatherPainting():
    # draw day
    # -draw sun
    # -draw clouds
    # draw night
    # -draw sun
    # -draw clouds
    print('weather painting?')