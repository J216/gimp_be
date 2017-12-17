from gimpfu import gimp, pdb, SELECT_CRITERION_COMPOSITE
import random, math
from gimp_be.settings.brush_settings import *
from gimp_be.utils.quick import qL
from gimp_be.image.layer import editLayerMask
from effects import mirror
import numpy as np
import UndrawnTurtle as turtle

def drawLine(points):
    image = gimp.image_list()[0]
    drawable = pdb.gimp_image_active_drawable(image)
    pdb.gimp_paintbrush_default(drawable, len(points), points)

def drawSpiral(n=140, angle=61, step=10, center=[]):
    coord=[]
    nt=turtle.Turtle()
    if center == []:
        image = gimp.image_list()[0]
        center=[image.width/2,image.height/2]
    for step in range(n):
        coord.append(int(nt.position()[0]*10)+center[0])
        coord.append(int(nt.position()[1]*10)+center[1])
        nt.forward(step)
        nt.left(angle)
        coord.append(int(nt.position()[0]*10)+center[0])
        coord.append(int(nt.position()[1]*10)+center[1])
    drawLine(coord)

def drawRays(rays=32, rayLength=100, centerX=0, centerY=0):
    """"
    draw N rays from center in active drawable with current brush
    """
    image = gimp.image_list()[0]
    drawable = pdb.gimp_image_active_drawable(image)
    if centerX == 0:
        centerX = image.width/2
    if centerY == 0:
        centerY = image.height/2
    ray_gap = int(360.0/rays)
    for ray in range(0,rays):
        ctrlPoints = centerX, centerY, centerX + rayLength * math.sin(math.radians(ray*ray_gap)), centerY + rayLength * math.cos(math.radians(ray*ray_gap))
        drawLine(ctrlPoints)

def drawRandomRays(rays=32, length=100, centerX=0, centerY=0,noise=0.3):
    image = gimp.image_list()[0]
    drawable = pdb.gimp_image_active_drawable(image)
    if centerX == 0:
        centerX = image.width/2
    if centerY == 0:
        centerY = image.height/2
    ray_gap = 360.0/rays
    for ray in range(0,rays):
        rayLength=random.choice(range(int(length-length*noise),int(length+length*noise)))
        random_angle=random.choice(np.arange(0.0,360.0,0.01))
        ctrlPoints = [ centerX, centerY, centerX + int(rayLength * math.sin(math.radians(random_angle))), int(centerY + rayLength * math.cos(math.radians(random_angle)))]
        drawLine(ctrlPoints)

def spikeBallStack(depth=20, layer_mode=6, flatten=0):
    for x in range(1,depth):
        image = gimp.image_list()[0]
        drawable = pdb.gimp_image_active_drawable(image)
        qL()
        pdb.gimp_layer_set_mode(pdb.gimp_image_get_active_layer(image), layer_mode)
        drawRandomRays(rays=random.choice([32,64,128,4]), length=(image.height/2-image.height/12), centerX=image.width/2, centerY=image.height/2,noise=random.choice([0.3,0.1,0.8]))
        if flatten:
            if not x%flatten:
                pdb.gimp_image_flatten(image)

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
        drawLine(ctrlPoints)


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
        drawLine(ctrlPoints)


# draw sine wave
def drawSinWaveDouble(barSpace, barLen, mag):
    image = gimp.image_list()[0]
    steps =image.width/ barSpace
    x = 0
    for cStep in range(1, steps):
        x = cStep * barSpace
        y = int(abs(round(math.sin(x) * mag + image.height / 2)))
        ctrlPoints = x, int(y - round(barLen / 2)), x, int(y + round(barLen / 2))
        drawLine(ctrlPoints)


# draw a single brush point
def drawBrush(x1, y1):
    image = gimp.image_list()[0]
    drawable = pdb.gimp_image_active_drawable(image)
    ctrlPoints = (x1, y1, x1, y1)
    drawLine(ctrlPoints)


# draw multiple brush points
def drawMultiBrush(brush_strokes=24):
    image = gimp.image_list()[0]
    grid_width=image.width/int(math.sqrt(brush_strokes))
    grid_height=image.height/int(math.sqrt(brush_strokes))
    coord_x=0
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



def randomRectFill(num=20, size=100, opt=3, sq=0):
    # draws square, opt  does random color
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


def randomBlend():
    # Random Blend tool test
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
    pdb.gimp_blend(drawable, blend_mode, paint_mode, gradient_type, opacity, offset, repeat, reverse, supersample, max_depth, threshold, dither, x1, y1, x2, y2)


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
    mirror('h')
    if 'trippy' in option and random.choice([0,1]):
        drawable = pdb.gimp_image_active_drawable(image)
        pdb.gimp_invert(drawable)
        editLayerMask(0)


def inkBlotStack(depth=16,layer_mode=6, flatten=0):
    for x in range(1,depth):
        image = gimp.image_list()[0]
        drawable = pdb.gimp_image_active_drawable(image)
        qL()
        pdb.gimp_layer_set_mode(pdb.gimp_image_get_active_layer(image), layer_mode)
        drawInkBlot()
        if flatten:
            if not x%flatten:
                flatten()


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


def tile(grid=[],option="mibd",irregularity=0.3):
    from random import randrange
    image=gimp.image_list()[0]
    layer=pdb.gimp_image_get_active_layer(image)
    if grid==[]:
        if image.height == image.width:
            grid=[4,4]
        elif image.height < image.width:
            grid=[3,4]
        else:
            grid=[4,3]
    if "m" in option:
        mask = pdb.gimp_layer_create_mask(layer,0)
        pdb.gimp_image_add_layer_mask(image, layer,mask)
        editLayerMask(1)
    drawable = pdb.gimp_image_active_drawable(image)
    grid_spacing = image.width/grid[0]
    tile_centers=gridCenters(grid)
    if irregularity > 0.0:
        i_tiles=[]
        for tile in tile_centers:
            tile[0]=tile[0]+random.randrange((-1*int(grid_spacing*irregularity)),int(grid_spacing*irregularity))
            tile[1]=tile[1]+random.randrange((-1*int(grid_spacing*irregularity)),int(grid_spacing*irregularity))
            i_tiles.append(tile)
        tile_centers=i_tiles
    if "b" in option:
        randomBrush()
    if "d" in option:
        randomDynamics()
    brushSize(grid_spacing)
    brushColor(0,0,0)
    for tile in tile_centers:
        if "m" in option:
            editLayerMask(1)
        if irregularity == 0:
            pdb.gimp_paintbrush_default(drawable, len(tile), tile)
        elif randrange(50.0*irregularity)+randrange(50.0*irregularity)>50.0:
            randomDynamics()
        else:
            pdb.gimp_paintbrush_default(drawable, len(tile), tile)
    if "g" in option:
        pdb.plug_in_gauss(image, drawable, 20.0, 20.0, 0)
    if "w" in option:
        pdb.plug_in_whirl_pinch(image, drawable, 90, 0.0, 1.0)
    if "i" in option:
        pdb.gimp_invert(drawable)
    if "m" in option:
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
    drawLine(trunk)
    for node in range(branches):
        node_base=[position[0],position[1]-((node*tree_height+1)/branches+tree_height/25+randrange(-1*tree_height/12,tree_height/12))]
        base_length=tree_height/25
        node_end=[]
        if node%2==0:
            node_end=[node_base[0]+base_length/2,node_base[1]-base_length/2]
            brushSize(2*trunk_size/3)
            drawLine([node_base[0],node_base[1],node_end[0],node_end[1]])
            brushSize(trunk_size/3)
            drawLine([node_end[0],node_end[1],node_end[0],node_end[1]-tree_height/12-(tree_height/48)])
        else:
            node_end=[node_base[0]-base_length/2,node_base[1]-base_length/2]
            brushSize(2*trunk_size/3)
            drawLine([node_base[0],node_base[1],node_end[0],node_end[1]])
            brushSize(trunk_size/3)
            drawLine([node_end[0],node_end[1],node_end[0],node_end[1]-(tree_height/12)])


def drawAkuForest(num=25):
    for x in range(num):
        drawAkuTree()



