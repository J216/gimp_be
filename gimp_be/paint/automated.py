from gimpfu import gimp, pdb
from gimp_be.utils import *
from gimp_be.draw import *
from gimp_be.image import *
from time import sleep
import random


# Full auto painting
def doPainting(paint_string='a'):
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
        qX()
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
                            'depth': random.randrange(7, 12)}
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
        qX()
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
            drawForest(random.randrange(15, 128), 0)
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
    qX()


#do batch of paintings 10 is the default
def doPaintings(option="",num=10,delay=240,tweet=0):
    for x in range(0, num):
        doPainting()
        qX()
        if tweet:
            signImage()
            qT()
            closeAll()
            sleep(delay)
        closeAll()


#automated creation of dimensionality study piece
def autoDimensionality(folder='',tweet=0):
    if folder == '':
        folder = settings_data['path']['art_folder']
    qS()
    loadDirLayer(folder,9699690)
    if tweet:
        signImage()
        qT()
    else:
        qX()


#do batch of dimensionality paintings
def multiDimensionality(folder,num=50,opt=0,img_target=0):
    if opt == 0 and img_target == 0:
        for x in range(0,num):
            tweet_opt=random.choice(range(1,50))
            if tweet_opt == 42:
                tweet_opt=1
            autoDimensionality(folder,tweet_opt)
            closeAll()
        return True
    else:
        return False


def doInkBlots(option="",num=10,delay=600,tweet=0):
    for x in range(num):
        qS()
        drawInkBlot(option)
        qX()
        if tweet:
            signImage()
            tweetImage('"What do you see?"\n"It looks like '+imageTitle(2)+' to me."',qX()[1])
            closeAll()
            sleep(delay)
        else:
            closeAll()


def doFractalMasking(option="",num=12,delay=300,tweet=0):
    for x in range(num):
        qS()
        if random.choice([0,0,0,0,1,1,1]):
            image=gimp.image_list()[0]
            drawable = pdb.gimp_image_active_drawable(image)
            pdb.gimp_invert(drawable)
        for x in range(random.choice([3,6,7,8,9,10])):
            addFractal()
            tileMask([random.choice([1,2,3,4,5,6,7,8,12]),random.choice([1,2,3,4,5,6,7,8,12])])
        if tweet:
            signImage()
            tweetImage('"Is it really self similar?"\n"Even '+imageTitle(2)+' will be '+imageTitle(2)+' someday."\n#fractals #python #GIMP',qX()[1])
            closeAll()
            sleep(delay)
        else:
            closeAll()


def doPhotoMasking(option="",num=12,delay=300,tweet=0):
    for x in range(num):
        qS()
        if random.choice([0,0,0,0,1,1,1]):
            image=gimp.image_list()[0]
            drawable = pdb.gimp_image_active_drawable(image)
            pdb.gimp_invert(drawable)
        for x in range(random.choice([3,6,7,8,9,10])):
            addPhoto()
            tileMask([random.choice([1,2,3,4,5,6,7,8,12]),random.choice([1,2,3,4,5,6,7,8,12])])
        if tweet:
            signImage()
            tweetImage('Photo Masking Mix\n'+imageTitle(2)+'\n by Jared Haer\n#photocomposite #python #gimp #digitalart',qX()[1])
            closeAll()
            sleep(delay)
        else:
            closeAll()


def doHybridMasking(option="",num=12,delay=300,tweet=0):
    for x in range(num):
        qS()
        drawInkBlot()
        if random.choice([0,0,0,0,1,1,1]):
            image=gimp.image_list()[0]
            drawable = pdb.gimp_image_active_drawable(image)
            pdb.gimp_invert(drawable)
        for x in range(random.choice([3,6,7,8,9,10])):
            addPhoto()
            tileMask([random.choice([1,2,3,4,5,6,7,8,12]),random.choice([1,2,3,4,5,6,7,8,12])])
            addFractal()
            tileMask([random.choice([1,2,3,4,5,6,7,8,12]),random.choice([1,2,3,4,5,6,7,8,12])])
        if tweet:
            signImage()
            tweetImage('Fractal-Photo Masking Mix\n'+imageTitle(2)+'\n by Jared Haer\n#fractals #python #gimp #digitalart',qX()[1])
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