import gimp
from gimp import pdb

from settings import *
from network import *
from image import *
from utils import *
from draw import *
from paint import *

from collections import Counter
import TwitterAPI
from random import randrange, choice, shuffle
from string import letters
import datetime as dt
from time import sleep

def setTwitterAPIKeys(ACCESS_TOKEN_KEY="NOT_SET",CONSUMER_KEY="NOT_SET",CONSUMER_SECRET="NOT_SET",ACCESS_TOKEN_SECRET="NOT_SET"):
    global settings_data
    if not ACCESS_TOKEN_KEY == "NOT_SET":
        settings_data['twitter']['ACCESS_TOKEN_KEY']=ACCESS_TOKEN_KEY
        settings_data['twitter']['CONSUMER_KEY']=CONSUMER_KEY
        settings_data['twitter']['CONSUMER_SECRET']=CONSUMER_SECRET
        settings_data['twitter']['ACCESS_TOKEN_SECRET']=ACCESS_TOKEN_SECRET
        saveSettings()

def addHashtag(tag):
    #add hashtag to settings
    global settings_data
    settings_data['twitter']['hashtags']=settings_data['twitter']['hashtags']+u' #'+unicode(tag, "utf-8")
    saveSettings()

def removeHashtag(tag):
    #return string of hashtags filling given character space
    global settings_data
    hashtags=map(str, settings_data['twitter']['hashtags'].split('#')[1:])
    hashtags=map(str.strip, hashtags)
    if tag in hashtags:
        hashtags.remove(tag)
        rt=''
        for hashtag in hashtags:
            rt=rt+'#'+hashtag + ' '
        rt.strip()
        settings_data['twitter']['hashtags']=rt
        saveSettings()
        return True
    else:
        return False

def hashtagString(length=140,mode=0):
    #return string of hashtags filling given character space
    global settings_data
    hashtags=settings_data['twitter']['hashtags'].split('#')[1:]
    hs=''
    ll=[]
    for item in hashtags:
        if len(item)+2<=length:
            ll.append(item)
    ll.sort(key=len)
    while length > len(ll[0]) and len(ll) > 0:
        il=[]
        for item in ll:
            if len(item)+2<=length:
                il.append(item)
        shuffle(il)
        if not len(il)==0:
            nh=il.pop()
            if len(nh)+2<=length:
                length=length-len(nh)-2
                hs=hs+'#'+nh.strip()+' '
                if nh in ll:
                    ll.remove(nh)
            if len(ll)<1:
                return str(hs).strip()
    return str(hs).strip()

def setDefaultTweet(default_tweet='GIMP-Python tweet!'):
    global settings_data
    settings_data['twitter']['default_tweet']=unicode(default_tweet, "utf-8")
    saveSettings()

def tweetText(opt=0):
    global settings_data
    now = dt.datetime.now()
    updateLocationData()
    title = imageTitle(2)
    city = settings_data["location"]["city"]
    state = settings_data["location"]["state"]
    host_name = settings_data["network"]["host_name"]
    tempf = settings_data["location"]["tempf"]
    weather = settings_data["location"]["weather"]
    hashtags = settings_data["twitter"]["hashtags"]
    time_stamp = str(dt.datetime.now())
    tweet_text = ''
    if opt == 0:
        tweet_text = title + '\nby ' + settings_data['user']['author'] + '\n' + city + ' ' + state + ' | ' + host_name + '\n' + tempf + 'F ' + weather + '\n' + now.strftime("%A %B %d - %I:%M%p")
    elif opt == 1:
        tweet_text = title + '\nby ' + settings_data['user']['author'] + ' ' + time_stamp[:4] + '\n'
    else:
        tweet_text = title + '\nby ' + settings_data['user']['author'] + ' ' + time_stamp[:4]
    tweet_text = tweet_text + '\n'+hashtagString(139-len(tweet_text))
    return tweet_text

def tweetImage(message,image_file):
    global settings_data
    CONSUMER_KEY = settings_data['twitter']['consumer_key']
    CONSUMER_SECRET = settings_data['twitter']['consumer_secret']
    ACCESS_TOKEN_KEY = settings_data['twitter']['access_token_key']
    ACCESS_TOKEN_SECRET = settings_data['twitter']['access_token_secret']
    api = TwitterAPI.TwitterAPI(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
    file = open(image_file, 'rb')
    data = file.read()
    r = api.request('statuses/update_with_media', {'status':message}, {'media[]':data})
    return str(str(r.status_code))

def qS():
    # quick set up of default size image
    imageSetup()

def qXJ(comment=""):
    # quick export jpg default with unique file name
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
    global settings_data
    tweet = tweetText(0)
    exported=qX(comment=tweet)
    sleep(5)
    return (tweetImage(tweet, exported[1]) == '200', tweet)

def qTG():
    # generate tweet then qX() then send tweet return results
    global settings_data
    tweet = tweetText(0)
    exported=qG()
    return (tweetImage(tweet, exported[1]) == '200', tweet)

def qXDT(fn,comment=""):
    global settings_data
    setEXIFTags(fn,{"Copyright":settings_data['user']['author']+" "+dt.datetime.now().strftime('%Y'),
                    "License":settings_data['image']['license'],
                    "Comment":comment,
                    "XPComment":comment,
                    "Description":comment,
                    "ImageDescription":comment,
                    "SEMInfo":comment,
                    "Artist":settings_data['user']['author'],
                    "Author":settings_data['user']['author'],
                    "Software":"GIMP 2.8 Python 2.7 EXIFTool",
                    "Title":comment[:comment.find('\n')],
                    "XPTitle":comment[:comment.find('\n')],
                    "Make":"GIMP",
                    "Model":"Python",
                    "Rating":"5"})

def paint():
    # Full auto painting
    global settings_data
    image = gimp.image_list()[0]
    height = image.height
    width = image.width
    x_center = width/2
    y_center = height/2
    image.height
    image.width
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
        flatten()
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
    if random.choice([0,0,0,0,1,1,1]):
        flatten()
        mirror()

def fractalMasking():
    # fractal layered wtih tile masks
    if random.choice([0,0,0,0,1,1,1]):
        image=gimp.image_list()[0]
        drawable = pdb.gimp_image_active_drawable(image)
        pdb.gimp_invert(drawable)
    for x in range(random.choice([3,6,7,8,9,10])):
        addFractal()
        tile([random.choice([1,2,3,4,5,6,7,8,12]),random.choice([1,2,3,4,5,6,7,8,12])])
    if random.choice([0,0,0,0,1,1,1]):
        flatten()
        mirror()

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
    if random.choice([0,0,0,0,1,1,1]):
        flatten()
        mirror()

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
    if random.choice([0,0,0,0,1,1,1]):
        flatten()
        mirror()

def spikeDif():
    # draw spike ball or random rays
    spikeBallStack(depth=random.choice([3,3,4,5,6,8,10,12,16,20]))
    applyEffect()
    if random.choice([0,0,0,0,1,1,1]):
        flatten()
        mirror()

def inkBlot():
    # draq basic ink blot
    inkBlotStack()
    applyEffect()
    if random.choice([0,0,0,0,1,1,1]):
        flatten()
        mirror()

def skeleton(type="",num=10,delay=10,tweet=1,study_name="Multifunctional Study"):
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
            automation_pick = random.choice(automations.keys())
            print(automation_pick)
            automations[automation_pick]()
        else:
            automations[type]()
        if tweet:
            signImage()
            flatten()
            tweet=imageTitle(2)+'\n by Jared Haer\n'+study_name+'\n'
            tweetImage(tweet+hashtagString(len(tweet)),qX()[1])
            print(tweet)
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

def addResource(options=0, resource_type="rock", opacity=90, resource_folder="", scale=[], position=[]):
    avoid_folders=['brushes','fonts','gradients','mask','overlays','paths','scraps','signature','stamps','stickers','stock-image','templates','tiles']
    if resource_type == "random":
        cl=dict(Counter(os.listdir(settings_data['path']['art_folder']+'/resources/'))-Counter(avoid_folders)).keys()
        resource_type = random.choice(cl)
    if resource_folder == "":
        resource_folder = settings_data['path']['art_folder']+'/resources/'+resource_type+'/'
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
        sticker_folder = settings_data['path']['art_folder']+'/resources/'+resource_type+'/'
    addResource(options, sticker_type, opacity, sticker_folder, scale, position)

def addSticker(options=0, sticker_type="", opacity=90, sticker_folder="", scale=[], position=[]):
    if sticker_folder == "":
        sticker_folder = settings_data['path']['art_folder']+'/resources/stickers/'
    addResource(options, sticker_type, opacity, sticker_folder, scale, position)

def addFractal(options=0, fractal_type="", opacity=90, fractal_folder="", scale=[], position=[]):
    image = gimp.image_list()[0]
    if fractal_folder == "":
        fractal_folder = settings_data['path']['art_folder']+'/resources/fractals/'
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
        photo_folder = settings_data['path']['art_folder']+'/resources/photos/'
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
        space_folder = settings_data['path']['art_folder']+'/resources/space/'
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
        script_folder = settings_data['path']['art_folder']+'/resources/script_drawings/'
    if position == []:
        position = [0,0]
    if scale == []:
        scale=[image.width, image.height]
    addResource(options, type, opacity, script_folder, scale, position)
    active_layer = pdb.gimp_image_get_active_layer(image)
    pdb.gimp_layer_set_mode(active_layer, random.choice([17,6,15,0,0,0,0,0,0]))


