from gimpfu import gimp, pdb
from random import randrange, choice, uniform
from gimp_be.image.image import gFlush


def mirror(direction=''):
    image=gimp.image_list()[0]
    drawable=""
    drawable = pdb.gimp_image_active_drawable(image)
    while not pdb.gimp_item_is_drawable(drawable):
        drawable = pdb.gimp_image_active_drawable(image)
    if 'h' in direction:
        pdb.gimp_image_select_rectangle(image, 0, 0, 0, image.width/2, image.height)
        non_empty = pdb.gimp_edit_copy(drawable)
        pdb.gimp_edit_paste(drawable, 1)
        floating_sel = pdb.gimp_image_floating_selection(image)
        pdb.gimp_item_transform_flip_simple(floating_sel, 0, 1, image.height/2)
        floating_sel = pdb.gimp_image_floating_selection(image)
        pdb.gimp_layer_translate(floating_sel, image.width/2, 0)
        pdb.gimp_floating_sel_anchor(floating_sel)
    elif 'v' in direction:
        pdb.gimp_image_select_rectangle(image, 0, 0, 0, image.width, image.height/2)
        non_empty = pdb.gimp_edit_copy(drawable)
        pdb.gimp_edit_paste(drawable, 1)
        floating_sel = pdb.gimp_image_floating_selection(image)
        pdb.gimp_item_transform_flip_simple(floating_sel, 1, 1, image.width/2)
        floating_sel = pdb.gimp_image_floating_selection(image)
        pdb.gimp_layer_translate(floating_sel, 0, image.height/2)
        pdb.gimp_floating_sel_anchor(floating_sel)
    else:
        pdb.gimp_image_select_rectangle(image, 0, 0, 0, image.width/2, image.height)
        non_empty = pdb.gimp_edit_copy(drawable)
        pdb.gimp_edit_paste(drawable, 1)
        floating_sel = pdb.gimp_image_floating_selection(image)
        pdb.gimp_item_transform_flip_simple(floating_sel, 0, 1, image.height/2)
        floating_sel = pdb.gimp_image_floating_selection(image)
        pdb.gimp_layer_translate(floating_sel, image.width/2, 0)
        pdb.gimp_floating_sel_anchor(floating_sel)
        drawable = pdb.gimp_image_active_drawable(image)
        pdb.gimp_image_select_rectangle(image, 0, 0, 0, image.width, image.height/2)
        non_empty = pdb.gimp_edit_copy(drawable)
        pdb.gimp_edit_paste(drawable, 1)
        floating_sel = pdb.gimp_image_floating_selection(image)
        pdb.gimp_item_transform_flip_simple(floating_sel, 1, 1, image.width/2)
        floating_sel = pdb.gimp_image_floating_selection(image)
        pdb.gimp_layer_translate(floating_sel, 0, image.height/2)
        pdb.gimp_floating_sel_anchor(floating_sel)
    return True

def wirlPinch():
    gFlush()
    image=gimp.image_list()[0]
    drawable = pdb.gimp_image_active_drawable(image)
    while not pdb.gimp_item_is_drawable(drawable):
        drawable = pdb.gimp_image_active_drawable(image)
    pdb.plug_in_whirl_pinch(image, drawable, randrange(-720.00,720.00), randrange(-1.0,1.0), randrange(0.0,2.0))


def gBlur():
    gFlush()
    image=gimp.image_list()[0]
    drawable = pdb.gimp_image_active_drawable(image)
    while not pdb.gimp_item_is_drawable(drawable):
        drawable = pdb.gimp_image_active_drawable(image)
    pdb.plug_in_gauss(image, drawable, uniform(1.0, image.height/9.0), uniform(1.0,image.width/9.0),0)

def invertColor():
    gFlush()
    image=gimp.image_list()[0]
    drawable = pdb.gimp_image_active_drawable(image)
    while not pdb.gimp_item_is_drawable(drawable):
        drawable = pdb.gimp_image_active_drawable(image)
    pdb.gimp_invert(drawable)


def glassTile():
    gFlush()
    image=gimp.image_list()[0]
    drawable = pdb.gimp_image_active_drawable(image)
    while not pdb.gimp_item_is_drawable(drawable):
        drawable = pdb.gimp_image_active_drawable(image)
    pdb.plug_in_glasstile(image, drawable, randrange(10,50), randrange(10,50))


def neonTrace():
    gFlush()
    image=gimp.image_list()[0]
    drawable = pdb.gimp_image_active_drawable(image)
    while not pdb.gimp_item_is_drawable(drawable):
        drawable = pdb.gimp_image_active_drawable(image)
    pdb.plug_in_neon(image, drawable, randrange(0.0,64.0), randrange(0.00,1.00))


def emboss():
    gFlush()
    image=gimp.image_list()[0]
    drawable = pdb.gimp_image_active_drawable(image)
    while not pdb.gimp_item_is_drawable(drawable):
        drawable = pdb.gimp_image_active_drawable(image)
    pdb.plug_in_emboss(image, drawable, randrange(360.0), randrange(180.0), randrange(1,100), choice([0,1]))


def oilify():
    gFlush()
    image=gimp.image_list()[0]
    drawable = pdb.gimp_image_active_drawable(image)
    while not pdb.gimp_item_is_drawable(drawable):
        drawable = pdb.gimp_image_active_drawable(image)
    pdb.plug_in_oilify(image, drawable, randrange(3,32), 0)


def hueSat():
    gFlush()
    image=gimp.image_list()[0]
    drawable = pdb.gimp_image_active_drawable(image)
    while not pdb.gimp_item_is_drawable(drawable):
        drawable = pdb.gimp_image_active_drawable(image)
    pdb.gimp_hue_saturation(drawable, randrange(0,6), randrange(-180,180), randrange(-100,100), randrange(-100,100))


def fractalTrace():
    gFlush()
    image=gimp.image_list()[0]
    drawable = pdb.gimp_image_active_drawable(image)
    while not pdb.gimp_item_is_drawable(drawable):
        drawable = pdb.gimp_image_active_drawable(image)
    pdb.plug_in_fractal_trace(image, drawable, uniform(-8.70,0.00), uniform(-1.00,15.00), uniform(0.00,6.00), randrange(-5,5), randrange(1,4), randrange(0,3))


def colorFlipper(num=100):
    from time import sleep
    for x in range(num):
        invertColor()
        pdb.gimp_displays_flush()
        sleep(1)


def applyEffect(option='gownfitheR',r=1):
    gFlush()
    image=gimp.image_list()[0]
    drawable = pdb.gimp_image_active_drawable(image)
    while not pdb.gimp_item_is_drawable(drawable):
        drawable = pdb.gimp_image_active_drawable(image)
    rare=[0,0,0,0,0,0,0,0,0,1]
    prob=[0,0,0,0,0,0,0,1,1,1]
    often=[0,0,0,0,1,1,1,1,1,1]
    #blur
    if 'R' in option:
        r=choice(rare)
    if "g" in option and r:
        gBlur()
    #color glass tile
    if 'R' in option:
        r=choice(rare)
    if "t" in option and r :
        glassTile()
    #wirl
    if 'R' in option:
        r=choice(rare)
    if "w" in option and r:
        wirlPinch()
    #color invert
    if 'R' in option:
        r=choice(rare)
    if "i" in option and r :
        invertColor()
    #neon trace
    if 'R' in option:
        r=choice(rare)
    if "n" in option and r :
        neonTrace()
    #emboss
    if 'R' in option:
        r=choice(rare)
    if "e" in option and r :
        emboss()
    #oilify
    if 'R' in option:
        r=choice(rare)
    if "o" in option and r :
        oilify()
    #hue saturation
    if 'R' in option:
        r=choice(rare)
    if "h" in option and r :
        hueSat()
    #fractal trace
    if 'R' in option:
        r=choice(rare)
    if "f" in option and r :
        fractalTrace()
    