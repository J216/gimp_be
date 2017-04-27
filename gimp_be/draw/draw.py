from gimpfu import gimp, pdb, SELECT_CRITERION_COMPOSITE
import random, math
from gimp_be.settings.brush_settings import *
from gimp_be.image.layer import editLayerMask


def drawRays(rays=32, rayLength=100, centerX=50, centerY=75):
    """"
    draw N rays from center in active drawable with current brush
    """
    image = gimp.image_list()[0]
    drawable = pdb.gimp_image_active_drawable(image)
    ray_gap = int(360/rays)
    for ray in range(0,rays):
        ctrlPoints = centerX, centerY, centerX + rayLength * math.sin(math.radians(ray*ray_gap)), centerY + rayLength * math.cos(math.radians(ray*ray_gap))
        pdb.gimp_paintbrush_default(drawable, len(ctrlPoints), ctrlPoints)


def randomStrokes(num = 4, opt = 1):
    """
    Draw random strokes of random size and random position
    """
    image = gimp.image_list()[0]
    drawable = pdb.gimp_image_active_drawable(image)
    r = random.randrange
    for loopNum in range(0, num):
        if opt == 1:
            brushSize(35)
        ctrlPoints = [r(-200, image.width+200), r(-200, image.height+200),r(-200, image.width+200),r(-200, image.height+200)]
        pdb.gimp_paintbrush_default(drawable, len(ctrlPoints), ctrlPoints)


# draw random color bars, opt 3 uses random blend
def drawBars(barNum=10, opt=3):
    image = gimp.image_list()[0]
    drawable = pdb.gimp_image_active_drawable(image)
    barWidth =image.width/ barNum
    barLeft = 0
    color = -1
    for loopNum in range(0, barNum):
        pdb.gimp_image_select_rectangle(image, 2, barLeft, 0, barWidth, image.height)
        barLeft = barLeft + barWidth
        if opt == 3:
            randomBlend()
        elif opt == 2:
            color = brushColor()
            pdb.gimp_edit_bucket_fill_full(drawable, 0, 0, 100, 0, 1, 0, SELECT_CRITERION_COMPOSITE, 0, 0)
        else:
            pdb.gimp_edit_bucket_fill_full(drawable, 0, 0, 100, 0, 1, 0, SELECT_CRITERION_COMPOSITE, 0, 0)
    pdb.gimp_selection_none(image)
    return (barNum, opt, color)


# draw carbon nano tube
def drawCNT():
    image = gimp.image_list()[0]
    drawable = pdb.gimp_image_active_drawable(image)
    drawSinWave(1, 4, image.height * .42, 0, image.height / 2)
    pdb.gimp_paintbrush(drawable, 0, 4, (0, (image.height - 80),image.width, (image.height - 80)), 0, 0)
    pdb.gimp_paintbrush(drawable, 0, 4, (0, 80,image.width, 80), 0, 0)


# draw sine wave
def drawSinWave(bar_space=32, bar_length=-1, mag=70, x_offset=-1, y_offset=-1):
    image = gimp.image_list()[0]
    drawable = pdb.gimp_image_active_drawable(image)
    if y_offset == -1:
        y_offset = image.height/2
    if x_offset == -1:
        x_offset = 0
    if bar_length == -1:
        bar_length = image.height/6
    steps = image.width / bar_space
    x = 0
    for cStep in range(0, steps):
        x = cStep * bar_space + x_offset
        y = int(round(math.sin(x) * mag) + y_offset)
        ctrlPoints = x, int(y - round(bar_length / 2)), x, int(y + round(bar_length / 2))
        pdb.gimp_paintbrush_default(drawable, len(ctrlPoints), ctrlPoints)


# draw sine wave
def drawSinWaveDouble(barSpace, barLen, mag):
    image = gimp.image_list()[0]
    drawable = pdb.gimp_image_active_drawable(image)
    steps =image.width/ barSpace
    x = 0
    for cStep in range(1, steps):
        x = cStep * barSpace
        y = int(abs(round(math.sin(x) * mag + image.height / 2)))
        ctrlPoints = x, int(y - round(barLen / 2)), x, int(y + round(barLen / 2))
        pdb.gimp_paintbrush_default(drawable, len(ctrlPoints), ctrlPoints)


# draw a single brush point
def drawBrush(x1, y1):
    image = gimp.image_list()[0]
    drawable = pdb.gimp_image_active_drawable(image)
    ctrlPoints = (x1, y1, x1, y1)
    pdb.gimp_paintbrush_default(drawable, len(ctrlPoints), ctrlPoints)
    return ctrlPoints


# draw multiple brush points
def drawMultiBrush(brush_strokes, options):
    image = gimp.image_list()[0]
    drawable = pdb.gimp_image_active_drawable(image)
    grid_width =image.width/ int(math.sqrt(brush_strokes))
    grid_height = image.height / int(math.sqrt(brush_strokes))
    brush_size = pdb.gimp_context_get_brush_size()
    option_list = {'Opacity': 0, 'Size': 0, 'Color': 0, 'Brush': 0, 'Pattern': 0}
    coord_set = (0, 0)
    # option_list = (0,0,0,0)
    if "randopgr" in options:
        option_list['Opacity'] = 1
    elif "randopind" in options:
        option_list['Opacity'] = 2
    if "randsizegr" in options:
        option_list['Size'] = 1
    elif "randsizeind" in options:
        option_list['Size'] = 2
    if "randcolgr" in options:
        option_list['Color'] = 1
    elif "randcolind" in options:
        option_list['Color'] = 2
    coord_x = 0
    coord_y = 0
    for i in range(0, int(math.sqrt(brush_strokes))):
        coord_x = coord_x + grid_width
        for x in range(0, int(math.sqrt(brush_strokes))):
            coord_y = coord_y + grid_height
            drawBrush(coord_x, coord_y)
        coord_y = 0


#draw grid of dots, this is for remainder mapping, this incomplete and temp. ####====DONT FORGET
def dotGrid():
    image = gimp.image_list()[0]
    drawable = pdb.gimp_image_active_drawable(image)
    for i in range(10,image.width-10,20):
        for x in range(10, image.height-10,20):
            grayColor(abs(i^3-x^3)%256)
            drawBrush(i+10,x+10)


# draws random dots, opt  does random color
def randomCircleFill(num=20, size=100, opt=3, sq=1):
    image = gimp.image_list()[0]
    drawable = pdb.gimp_image_active_drawable(image)
    for loopNum in range(0, num):
        cirPar = [random.randrange(0,image.width), random.randrange(0, image.height), random.randrange(10, size),
                  random.randrange(10, size)]
        if opt % 2 == 0:
            brushColor()
        if sq:
            pdb.gimp_ellipse_select(image, cirPar[0], cirPar[1], cirPar[2], cirPar[2], 2, 1, 0, 0)
        else:
            pdb.gimp_ellipse_select(image, cirPar[0], cirPar[1], cirPar[2], cirPar[3], 2, 1, 0, 0)
        if opt % 3 == 3:
            randomBlend()
        else:
            pdb.gimp_edit_bucket_fill_full(drawable, 0, 0, 100, 0, 1, 0, SELECT_CRITERION_COMPOSITE, 0, 0)
    pdb.gimp_selection_none(image)


# draws square, opt  does random color
def randomRectFill(num=20, size=100, opt=3, sq=0):
    image = gimp.image_list()[0]
    drawable = pdb.gimp_image_active_drawable(image)
    selectMode = 2
    if opt % 5 == 0:
        selectMode = 0
    for loopNum in range(0, num):
        if opt % 2 == 0:
            brushColor()
        rectPar = [random.randrange(0,image.width), random.randrange(0, image.height), random.randrange(10, size),
                   random.randrange(10, size)]
        if sq:
            pdb.gimp_image_select_rectangle(image, 2, rectPar[0], rectPar[1], rectPar[2], rectPar[2])
        else:
            pdb.gimp_image_select_rectangle(image, 2, rectPar[0], rectPar[1], rectPar[2], rectPar[3])
        if opt % 3 == 0:
            randomBlend()
        else:
            pdb.gimp_edit_bucket_fill_full(drawable, 0, 0, 100, 0, 1, 0, SELECT_CRITERION_COMPOSITE, 0, 0)
    pdb.gimp_selection_none(image)


# Random Blend tool test
def randomBlend():
    blend_mode = 0
    paint_mode = 0
    gradient_type = random.randrange(0, 10)
    opacity = random.randrange(20, 100)
    offset = 0
    repeat = random.randrange(0, 2)
    reverse = 0
    supersample = 0
    max_depth = random.randrange(1, 9)
    threshold = 0
    threshold = random.randrange(0, 1)
    dither = 0
    image = gimp.image_list()[0]
    drawable = pdb.gimp_image_active_drawable(image)
    brushColor()
    x1 = random.randrange(0,image.width)
    y1 = random.randrange(0, image.height)
    x2 = random.randrange(0,image.width)
    y2 = random.randrange(0, image.height)
    settings = (
    drawable, blend_mode, paint_mode, gradient_type, opacity, offset, repeat, reverse, supersample, max_depth,
    threshold, dither, x1, y1, x2, y2)
    pdb.gimp_blend(drawable, blend_mode, paint_mode, gradient_type, opacity, offset, repeat, reverse, supersample,
                   max_depth, threshold, dither, x1, y1, x2, y2)


def randomPoints(num=12):
    d = []
    for x in range(num):
        d.append(choice(range(boarder,image.width-boarder)))
        d.append(choice(range(boarder,image.height-boarder)))
    return d


def drawInkBlot(option=''):
    image=gimp.image_list()[0]
    layer=pdb.gimp_image_get_active_layer(image)
    if 'trippy' in option:
        layer_copy = pdb.gimp_layer_copy(layer, 0)
        pdb.gimp_image_add_layer(image, layer_copy,1)
        randomBlend()
        mask = pdb.gimp_layer_create_mask(layer,5)
        pdb.gimp_image_add_layer_mask(image, layer,mask)
        editLayerMask(1)
    randomCircleFill(num=15,size=800)
    brushColor(255,255,255)
    randomCircleFill(num=50,size=100)
    randomCircleFill(num=5,size=300)
    brushColor(0)
    randomCircleFill(num=20,size=600)
    randomCircleFill(num=50,size=400)
    randomCircleFill(num=100,size=100)
    brushColor(255,255,255)
    randomCircleFill(num=50,size=100)
    brushColor(0)
    drawable = pdb.gimp_image_active_drawable(image)
    brushSize()
    strokes=[random.randrange(0,image.width/2),random.randrange(0,image.height),random.randrange(0,image.width/2),random.randrange(0,image.height)]
    pdb.gimp_smudge(drawable, random.choice([1,5,10,50,100]), len(strokes), strokes)
    brushSize()
    strokes=[random.randrange(0,image.width/2),random.randrange(0,image.height),random.randrange(0,image.width/2),random.randrange(0,image.height)]
    pdb.gimp_smudge(drawable, random.choice([1,5,10,50,100]), len(strokes), strokes)
    pdb.gimp_image_select_rectangle(image, 0, 0, 0, image.width/2, image.height)
    non_empty = pdb.gimp_edit_copy(drawable)
    pdb.gimp_edit_paste(drawable, 1)
    floating_sel = pdb.gimp_image_floating_selection(image)
    pdb.gimp_item_transform_flip_simple(floating_sel, 0, 1, image.height/2)
    floating_sel = pdb.gimp_image_floating_selection(image)
    pdb.gimp_layer_translate(floating_sel, image.width/2, 0)
    pdb.gimp_floating_sel_anchor(floating_sel)
    if 'trippy' in option and random.choice([0,1]):
        drawable = pdb.gimp_image_active_drawable(image)
        pdb.gimp_invert(drawable)
        editLayerMask(0)


def gridCenters(grid=[]):
    if grid==[]:
        grid=[4,3]
    image = gimp.image_list()[0]
    row_width = image.width/(grid[0])
    columb_height = image.height/(grid[1])
    tile_centers = [] 
    for row in range(0,grid[0]):
        for columb in range(0,grid[1]):
            tile_centers.append([row_width*row+row_width/2,columb_height*columb+columb_height/2])
    return tile_centers


def tileMask(grid=[]):
    image=gimp.image_list()[0]
    layer=pdb.gimp_image_get_active_layer(image)
    if grid==[]:
        if image.height == image.width:
            grid=[4,4]
        elif image.height < image.width:
            grid=[3,4]
        else:
            grid=[4,3]
    mask = pdb.gimp_layer_create_mask(layer,0)
    pdb.gimp_image_add_layer_mask(image, layer,mask)
    editLayerMask(1)
    drawable = pdb.gimp_image_active_drawable(image)
    tile_centers=gridCenters(grid)
    randomBrush()
    randomDynamics()
    for tile in tile_centers:
        brushSize(image.width/grid[0])
        brushColor(0,0,0)
        editLayerMask(1)
        pdb.gimp_paintbrush_default(drawable, len(tile), tile)
    pdb.gimp_invert(drawable)
    editLayerMask(0)


def drawAkuTree(branches=6,tree_height=0, position=0):
    from random import choice, randrange
    image = gimp.image_list()[0]
    drawable = pdb.gimp_image_active_drawable(image)
    if position==0:
        position=[]
        position.append(randrange(image.width))
        position.append(randrange(4*tree_height/3, 3*image.height/4))
    if tree_height == 0:
        tree_height=randrange(position[1]/3, position[1]-position[1]/25)
    print 'position:' + str(position)
    #draw trunk
    trunk=[position[0],position[1],position[0],position[1]-tree_height]
    trunk_size=tree_height/40+3
    print str(trunk)
    print 'tree_height: ' + str(tree_height)
    print 'trunk size: ' + str(trunk_size)
    brushSize(trunk_size)
    pdb.gimp_paintbrush_default(drawable, len(trunk), trunk)
    for node in range(branches):
        node_base=[position[0],position[1]-((node*tree_height+1)/branches+tree_height/25+randrange(-1*tree_height/12,tree_height/12))]
        base_length=tree_height/25
        node_end=[]
        if node%2==0:
            node_end=[node_base[0]+base_length/2,node_base[1]-base_length/2]
            brushSize(2*trunk_size/3)
            pdb.gimp_paintbrush_default(drawable, 4, [node_base[0],node_base[1],node_end[0],node_end[1]])
            brushSize(trunk_size/3)
            pdb.gimp_paintbrush_default(drawable, 4, [node_end[0],node_end[1],node_end[0],node_end[1]-tree_height/12-(tree_height/48)])
        else:
            node_end=[node_base[0]-base_length/2,node_base[1]-base_length/2]
            brushSize(2*trunk_size/3)
            pdb.gimp_paintbrush_default(drawable, 4, [node_base[0],node_base[1],node_end[0],node_end[1]])
            brushSize(trunk_size/3)
            pdb.gimp_paintbrush_default(drawable, 4, [node_end[0],node_end[1],node_end[0],node_end[1]-(tree_height/12)])


def drawAkuForest(num=25):
    for x in range(num):
        drawAkuTree()



