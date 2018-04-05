import random, math
import gimp_be
#from gimp_be.utils.quick import qL
from gimp_be.image.layer import editLayerMask
from effects import mirror
import numpy as np
import UndrawnTurtle as turtle

def brushSize(size=-1):
    """"
    Set brush size
    """
    image = gimp_be.gimp.image_list()[0]
    drawable = gimp_be.pdb.gimp_image_active_drawable(image)
    if size < 1:
        size = random.randrange(2, ((image.height + image.width) / 8))
    gimp_be.pdb.gimp_context_set_brush_size(size)

# Set brush opacity
def brushOpacity(op=-1):
    if op == -1:
        op = random.randrange(15, 100)
    gimp_be.pdb.gimp_brushes_set_opacity(op)
    return op

# Set random brush color no parameters set random
def brushColor(r1=-1, g1=-1, b1=-1, r2=-1, g2=-1, b2=-1):
    if not r1 == -1:
        gimp_be.pdb.gimp_context_set_foreground((r1, g1, b1))
    if not r2 == -1:
        gimp_be.pdb.gimp_context_set_background((r2, g2, b2))
    elif r1 == -1:
        r1 = random.randrange(0, 255)
        g1 = random.randrange(0, 255)
        b1 = random.randrange(0, 255)
        r2 = random.randrange(0, 255)
        g2 = random.randrange(0, 255)
        b2 = random.randrange(0, 255)
        gimp_be.pdb.gimp_context_set_foreground((r1, g1, b1))
        gimp_be.pdb.gimp_context_set_background((r2, g2, b2))
    return (r1, g1, b1, r2, g2, b2)

#set gray scale color
def grayColor(gray_color):
    gimp_be.pdb.gimp_context_set_foreground((gray_color, gray_color, gray_color))

# Set random brush
def randomBrush():
    num_brushes, brush_list = gimp_be.pdb.gimp_brushes_get_list('')
    brush_pick = brush_list[random.randrange(0, len(brush_list))]
    gimp_be.pdb.gimp_brushes_set_brush(brush_pick)
    return brush_pick

# Set random brush dynamics
def randomDynamics():
    dynamics_pick = random.choice(gimp_be.pdb.gimp_dynamics_get_list('')[1])
    gimp_be.pdb.gimp_context_set_dynamics(dynamics_pick)
    return dynamics_pick

def qL():
    # quick new layer
    gimp_be.addNewLayer()
    image = gimp_be.gimp.image_list()[0]
    drawable = gimp_be.pdb.gimp_image_active_drawable(image)
    gimp_be.pdb.gimp_edit_fill(drawable, 1)

def drawLine(points):
    image = gimp_be.gimp.image_list()[0]
    drawable = gimp_be.pdb.gimp_image_active_drawable(image)
    gimp_be.pdb.gimp_paintbrush_default(drawable, len(points), points)

def drawSpiral(n=140, angle=61, step=10, center=[]):
    coord=[]
    nt=turtle.Turtle()
    if center == []:
        image = gimp_be.gimp.image_list()[0]
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
    image = gimp_be.gimp.image_list()[0]
    drawable = gimp_be.pdb.gimp_image_active_drawable(image)
    if centerX == 0:
        centerX = image.width/2
    if centerY == 0:
        centerY = image.height/2
    ray_gap = int(360.0/rays)
    for ray in range(0,rays):
        ctrlPoints = centerX, centerY, centerX + rayLength * math.sin(math.radians(ray*ray_gap)), centerY + rayLength * math.cos(math.radians(ray*ray_gap))
        drawLine(ctrlPoints)

def drawRandomRays(rays=32, length=100, centerX=0, centerY=0,noise=0.3):
    image = gimp_be.gimp.image_list()[0]
    drawable = gimp_be.pdb.gimp_image_active_drawable(image)
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
        image = gimp_be.gimp.image_list()[0]
        drawable = gimp_be.pdb.gimp_image_active_drawable(image)
        qL()
        gimp_be.pdb.gimp_layer_set_mode(gimp_be.pdb.gimp_image_get_active_layer(image), layer_mode)
        drawRandomRays(rays=random.choice([32,64,128,4]), length=(image.height/2-image.height/12), centerX=image.width/2, centerY=image.height/2,noise=random.choice([0.3,0.1,0.8]))
        if flatten:
            if not x%flatten:
                gimp_be.pdb.gimp_image_flatten(image)

def randomStrokes(num = 4, opt = 1):
    """
    Draw random strokes of random size and random position
    """
    image = gimp_be.gimp.image_list()[0]
    drawable = gimp_be.pdb.gimp_image_active_drawable(image)
    r = random.randrange
    for loopNum in range(0, num):
        if opt == 1:
            brushSize(35)
        drawLine(ctrlPoints)

# draw random color bars, opt 3 uses random blend
def drawBars(barNum=10, opt=3):
    image = gimp_be.gimp.image_list()[0]
    drawable = gimp_be.pdb.gimp_image_active_drawable(image)
    barWidth =image.width/ barNum
    barLeft = 0
    color = -1
    for loopNum in range(0, barNum):
        gimp_be.pdb.gimp_image_select_rectangle(image, 2, barLeft, 0, barWidth, image.height)
        barLeft = barLeft + barWidth
        if opt == 3:
            randomBlend()
        elif opt == 2:
            color = brushColor()
            gimp_be.pdb.gimp_edit_bucket_fill_full(drawable, 0, 0, 100, 0, 1, 0, gimp_be.SELECT_CRITERION_COMPOSITE, 0, 0)
        else:
            gimp_be.pdb.gimp_edit_bucket_fill_full(drawable, 0, 0, 100, 0, 1, 0, gimp_be.SELECT_CRITERION_COMPOSITE, 0, 0)
    gimp_be.pdb.gimp_selection_none(image)
    return (barNum, opt, color)

# draw carbon nano tube
def drawCNT():
    image = gimp_be.gimp.image_list()[0]
    drawable = gimp_be.pdb.gimp_image_active_drawable(image)
    drawSinWave(1, 4, image.height * .42, 0, image.height / 2)
    gimp_be.pdb.gimp_paintbrush(drawable, 0, 4, (0, (image.height - 80),image.width, (image.height - 80)), 0, 0)
    gimp_be.pdb.gimp_paintbrush(drawable, 0, 4, (0, 80,image.width, 80), 0, 0)

# draw sine wave
def drawSinWave(bar_space=32, bar_length=-1, mag=70, x_offset=-1, y_offset=-1):
    image = gimp_be.gimp.image_list()[0]
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
    image = gimp_be.gimp.image_list()[0]
    steps =image.width/ barSpace
    x = 0
    for cStep in range(1, steps):
        x = cStep * barSpace
        y = int(abs(round(math.sin(x) * mag + image.height / 2)))
        ctrlPoints = x, int(y - round(barLen / 2)), x, int(y + round(barLen / 2))
        drawLine(ctrlPoints)

# draw a single brush point
def drawBrush(x1, y1):
    image = gimp_be.gimp.image_list()[0]
    drawable = gimp_be.pdb.gimp_image_active_drawable(image)
    ctrlPoints = (x1, y1, x1, y1)
    drawLine(ctrlPoints)

# draw multiple brush points
def drawMultiBrush(brush_strokes=24):
    image = gimp_be.gimp.image_list()[0]
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
    image = gimp_be.gimp.image_list()[0]
    drawable = gimp_be.pdb.gimp_image_active_drawable(image)
    for i in range(10,image.width-10,20):
        for x in range(10, image.height-10,20):
            grayColor(abs(i^3-x^3)%256)
            drawBrush(i+10,x+10)

# draws random dots, opt  does random color
def randomCircleFill(num=20, size=100, opt=3, sq=1):
    image = gimp_be.gimp.image_list()[0]
    drawable = gimp_be.pdb.gimp_image_active_drawable(image)
    for loopNum in range(0, num):
        cirPar = [random.randrange(0,image.width), random.randrange(0, image.height), random.randrange(10, size),
                  random.randrange(10, size)]
        if opt % 2 == 0:
            brushColor()
        if sq:
            gimp_be.pdb.gimp_ellipse_select(image, cirPar[0], cirPar[1], cirPar[2], cirPar[2], 2, 1, 0, 0)
        else:
            gimp_be.pdb.gimp_ellipse_select(image, cirPar[0], cirPar[1], cirPar[2], cirPar[3], 2, 1, 0, 0)
        if opt % 3 == 3:
            randomBlend()
        else:
            gimp_be.pdb.gimp_edit_bucket_fill_full(drawable, 0, 0, 100, 0, 1, 0, gimp_be.SELECT_CRITERION_COMPOSITE, 0, 0)
    gimp_be.pdb.gimp_selection_none(image)

def randomRectFill(num=20, size=100, opt=3, sq=0):
    # draws square, opt  does random color
    image = gimp_be.gimp.image_list()[0]
    drawable = gimp_be.pdb.gimp_image_active_drawable(image)
    selectMode = 2
    if opt % 5 == 0:
        selectMode = 0
    for loopNum in range(0, num):
        if opt % 2 == 0:
            brushColor()
        rectPar = [random.randrange(0,image.width), random.randrange(0, image.height), random.randrange(10, size),
                   random.randrange(10, size)]
        if sq:
            gimp_be.pdb.gimp_image_select_rectangle(image, 2, rectPar[0], rectPar[1], rectPar[2], rectPar[2])
        else:
            gimp_be.pdb.gimp_image_select_rectangle(image, 2, rectPar[0], rectPar[1], rectPar[2], rectPar[3])
        if opt % 3 == 0:
            randomBlend()
        else:
            gimp_be.pdb.gimp_edit_bucket_fill_full(drawable, 0, 0, 100, 0, 1, 0, gimp_be.SELECT_CRITERION_COMPOSITE, 0, 0)
    gimp_be.pdb.gimp_selection_none(image)

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
    image = gimp_be.gimp.image_list()[0]
    drawable = gimp_be.pdb.gimp_image_active_drawable(image)
    brushColor()
    x1 = random.randrange(0,image.width)
    y1 = random.randrange(0, image.height)
    x2 = random.randrange(0,image.width)
    y2 = random.randrange(0, image.height)
    gimp_be.pdb.gimp_blend(drawable, blend_mode, paint_mode, gradient_type, opacity, offset, repeat, reverse, supersample, max_depth, threshold, dither, x1, y1, x2, y2)

def randomPoints(num=12):
    d = []
    for x in range(num):
        d.append(choice(range(boarder,image.width-boarder)))
        d.append(choice(range(boarder,image.height-boarder)))
    return d

def drawInkBlot(option=''):
    image=gimp_be.gimp.image_list()[0]
    layer=gimp_be.pdb.gimp_image_get_active_layer(image)
    if 'trippy' in option:
        layer_copy = gimp_be.pdb.gimp_layer_copy(layer, 0)
        gimp_be.pdb.gimp_image_add_layer(image, layer_copy,1)
        randomBlend()
        mask = gimp_be.pdb.gimp_layer_create_mask(layer,5)
        gimp_be.pdb.gimp_image_add_layer_mask(image, layer,mask)
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
    drawable = gimp_be.pdb.gimp_image_active_drawable(image)
    brushSize()
    strokes=[random.randrange(0,image.width/2),random.randrange(0,image.height),random.randrange(0,image.width/2),random.randrange(0,image.height)]
    gimp_be.pdb.gimp_smudge(drawable, random.choice([1,5,10,50,100]), len(strokes), strokes)
    brushSize()
    strokes=[random.randrange(0,image.width/2),random.randrange(0,image.height),random.randrange(0,image.width/2),random.randrange(0,image.height)]
    gimp_be.pdb.gimp_smudge(drawable, random.choice([1,5,10,50,100]), len(strokes), strokes)
    mirror('h')
    if 'trippy' in option and random.choice([0,1]):
        drawable = gimp_be.pdb.gimp_image_active_drawable(image)
        gimp_be.pdb.gimp_invert(drawable)
        editLayerMask(0)

def inkBlotStack(depth=16,layer_mode=6, flatten=0):
    for x in range(1,depth):
        image = gimp_be.gimp.image_list()[0]
        drawable = gimp_be.pdb.gimp_image_active_drawable(image)
        qL()
        gimp_be.pdb.gimp_layer_set_mode(gimp_be.pdb.gimp_image_get_active_layer(image), layer_mode)
        drawInkBlot()
        if flatten:
            if not x%flatten:
                flatten()

def gridCenters(grid=[]):
    if grid==[]:
        grid=[4,3]
    image = gimp_be.gimp.image_list()[0]
    row_width = image.width/(grid[0])
    columb_height = image.height/(grid[1])
    tile_centers = [] 
    for row in range(0,grid[0]):
        for columb in range(0,grid[1]):
            tile_centers.append([row_width*row+row_width/2,columb_height*columb+columb_height/2])
    return tile_centers

def tile(grid=[],option="mibd",irregularity=0.3):
    image=gimp_be.gimp.image_list()[0]
    layer=gimp_be.pdb.gimp_image_get_active_layer(image)
    if grid==[]:
        if image.height == image.width:
            grid=[4,4]
        elif image.height < image.width:
            grid=[3,4]
        else:
            grid=[4,3]
    if "m" in option:
        mask = gimp_be.pdb.gimp_layer_create_mask(layer,0)
        gimp_be.pdb.gimp_image_add_layer_mask(image, layer,mask)
        editLayerMask(1)
    drawable = gimp_be.pdb.gimp_image_active_drawable(image)
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
            gimp_be.pdb.gimp_paintbrush_default(drawable, len(tile), tile)
        elif random.randrange(50.0*irregularity)+random.randrange(50.0*irregularity)>50.0:
            randomDynamics()
        else:
            gimp_be.pdb.gimp_paintbrush_default(drawable, len(tile), tile)
    if "g" in option:
        gimp_be.pdb.plug_in_gauss(image, drawable, 20.0, 20.0, 0)
    if "w" in option:
        gimp_be.pdb.plug_in_whirl_pinch(image, drawable, 90, 0.0, 1.0)
    if "i" in option:
        gimp_be.pdb.gimp_invert(drawable)
    if "m" in option:
        editLayerMask(0)

def drawAkuTree(branches=6,tree_height=0, position=0):
    image = gimp_be.gimp.image_list()[0]
    drawable = gimp_be.pdb.gimp_image_active_drawable(image)
    if position==0:
        position=[]
        position.append(random.randrange(image.width))
        position.append(random.randrange(4*tree_height/3, 3*image.height/4))
    if tree_height == 0:
        tree_height=random.randrange(position[1]/3, position[1]-position[1]/25)
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
        node_base=[position[0],position[1]-((node*tree_height+1)/branches+tree_height/25+random.randrange(-1*tree_height/12,tree_height/12))]
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

# draw a tree
def drawTree(x1=-1, y1=-1, angle=270, depth=9, recursiondepth=0):
    image = gimp_be.gimp.image_list()[0]
    drawable = gimp_be.pdb.gimp_image_active_drawable(image)
    if x1 == -1:
        x1 = image.width/2
    if y1 == -1:
        y1 = image.height/2
    x2 = x1 + int(math.cos(math.radians(angle)) * depth * 10.0)
    y2 = y1 + int(math.sin(math.radians(angle)) * depth * 10.0)
    ctrlPoints = (x1, y1, x2, y2)
    if recursiondepth <= 2:
        brushColor(87, 53, 12)
    elif depth == 1:
        brushColor(152, 90, 17)
    elif depth <= 3:
        brushColor(7, 145, 2)
    brushSize(depth * 4 + 5)
    gimp_be.pdb.gimp_paintbrush_default(drawable, len(ctrlPoints), ctrlPoints)
    if depth > 0:
        drawTree(x2, y2, angle - 20, depth - 1, recursiondepth + 1)
        drawTree(x2, y2, angle + 20, depth - 1, recursiondepth + 1)

# draw a tree with 3 branches per node
def drawTriTree(x1=-1, y1=-1, angle=270, depth=6, recursiondepth=0, size=10):
    image = gimp_be.gimp.image_list()[0]
    drawable = gimp_be.pdb.gimp_image_active_drawable(image)
    if x1 == -1:
        x1 = image.width/2
    if y1 == -1:
        y1 = image.height/2
    if depth:
        x2 = x1 + int(math.cos(math.radians(angle)) * depth * size) + random.randrange(-12, 12)
        y2 = y1 + int(math.sin(math.radians(angle)) * depth * size) + random.randrange(-12, 12)
        ctrlPoints = (x1, y1, x2, y2)
        brushSize(depth + int(size/10))
        brushColor()
        gimp_be.pdb.gimp_paintbrush_default(drawable, len(ctrlPoints), ctrlPoints)
        drawTriTree(x2, y2, angle - 30, depth - 1, recursiondepth + 1,size)
        drawTriTree(x2, y2, angle, depth - 1, recursiondepth + 1,size)
        drawTriTree(x2, y2, angle + 30, depth - 1, recursiondepth + 1,size)

# draw random color tri-tree
def drawColorTriTree(x1=-1, y1=-1, angle=270, depth=9, recursiondepth=0):
    image = gimp_be.gimp.image_list()[0]
    drawable = gimp_be.pdb.gimp_image_active_drawable(image)
    if x1 == -1:
        x1 = image.width/2
    if y1 == -1:
        y1 = image.height/2
    brushSize(depth + 1)
    if depth:
        x2 = x1 + int(math.cos(math.radians(angle)) * depth * 10.0) + random.randrange(-12, 12)
        y2 = y1 + int(math.sin(math.radians(angle)) * depth * 10.0) + random.randrange(-12, 12)
        ctrlPoints = (x1, y1, x2, y2)
        gimp_be.pdb.gimp_paintbrush_default(drawable, len(ctrlPoints), ctrlPoints)
        drawColorTriTree(x2, y2, angle - 20 + random.choice(-10, -5, 0, 5, 10), depth - 1, recursiondepth + 1)
        drawColorTriTree(x2, y2, angle + random.choice(-10, -5, 0, 5, 10), depth - 1, recursiondepth + 1)
        drawColorTriTree(x2, y2, angle + 20 + random.choice(-10, -5, 0, 5, 10), depth - 1, recursiondepth + 1)

# draw a tree
def drawOddTree(x1=-1, y1=-1, angle=270, depth=9, recursiondepth=0):
    image = gimp_be.gimp.image_list()[0]
    drawable = gimp_be.pdb.gimp_image_active_drawable(image)
    if x1 == -1:
        x1 = image.width/2
    if y1 == -1:
        y1 = image.height/2
    brushSize((depth * 8 + 30))
    if depth:
        x2 = x1 + int(math.cos(math.radians(angle)) * depth * 10.0)
        y2 = y1 + int(math.sin(math.radians(angle)) * depth * 10.0)
        ctrlPoints = (x1, y1, x2, y2)
        gimp_be.pdb.gimp_paintbrush_default(drawable, len(ctrlPoints), ctrlPoints)
        if not random.randrange(0, 23) == 23:
            drawTree(x2, y2, angle - 20, depth - 1, recursiondepth + 1)
            if depth % 2 == 0:
                drawTree(x2, y2, angle + 20, depth - 1, recursiondepth + 1)
            if (depth + 1) % 4 == 0:
                drawTree(x2, y2, angle + 20, depth - 1, recursiondepth + 1)
            if depth == 5:
                drawTree(x2, y2, angle - 45, depth - 1, recursiondepth + 1)
                drawTree(x2, y2, angle + 45, depth - 1, recursiondepth + 1)

# draw a tree
def drawForestTree(x1=-1, y1=-1, angle=270, depth=7, size=10, recursiondepth=0):
    image = gimp_be.gimp.image_list()[0]
    drawable = gimp_be.pdb.gimp_image_active_drawable(image)
    if x1 == -1:
        x1 = image.width/2
    if y1 == -1:
        y1 = image.height/2
    if depth:
        x2 = x1 + int(math.cos(math.radians(angle)) * depth * 10.0)
        y2 = y1 + int(math.sin(math.radians(angle)) * depth * 10.0)
        ctrlPoints = (x1, y1, x2, y2)
        brushSize(depth * depth * (int(size / ((image.height - y1)) / image.height)) + 4)
        gimp_be.pdb.gimp_paintbrush_default(drawable, len(ctrlPoints), ctrlPoints)
        if not random.randrange(0, 23) == 23:
            drawForestTree(x2, y2, angle - 20, depth - 1, size, recursiondepth + 1)
            if random.randrange(0, 23) == 23:
                drawForestTree(x2, y2, angle - random.randrange(-30, 30), depth - 1, size, recursiondepth + 1)
                drawForestTree(x2, y2, angle - random.randrange(-30, 30), depth - 1, size, recursiondepth + 1)
                drawForestTree(x2, y2, angle - random.randrange(-30, 30), depth - 1, size, recursiondepth + 1)
            else:
                drawForestTree(x2, y2, angle - random.randrange(15, 50), depth - 1, size, recursiondepth + 1)
                if depth % 2 == 0:
                    drawForestTree(x2, y2, angle + 20, depth - 1, size, recursiondepth + 1)
                if (depth + 1) % 4 == 0:
                    drawForestTree(x2, y2, angle + 20, depth - 1, size, recursiondepth + 1)
                if depth == 5:
                    drawForestTree(x2, y2, angle - 45, depth - 1, size, recursiondepth + 1)
                    drawForestTree(x2, y2, angle + 45, depth - 1, size, recursiondepth + 1)

# draw a series of trees with a y position based on depth
def drawForest(trees, options):
    image = gimp_be.gimp.image_list()[0]
    for tree in range(0, trees):
        y1 = 2 * (image.height / 3) + random.randrange(-1 * (image.height / 5), image.height / 5)
        x1 = random.randrange(image.width / 20, 19 * (image.width / 20))
        angle = random.randrange(250, 290)
        size = (y1 / (2.0 * (image.height / 3.0) + (image.height / 5.0))) + 4
        depth = random.randrange(3, 7)
        drawForestTree(x1, y1, angle, depth, size)

#draws polygon of N sides at a x-y location
def drawPolygon(sides=5,size=300,x_pos=0,y_pos=0, angle_offset=0):
    image = gimp_be.gimp.image_list()[0]
    drawable = gimp_be.pdb.gimp_image_active_drawable(image)
    if y_pos==0:
        y_pos=image.height/2
        if x_pos==0:
            x_pos=image.width/2
    degree_between_points=360/sides
    points_list=[]
    for x in range(0,sides+1):
        point_degree=degree_between_points*x+angle_offset
        points_list.append(int(round(math.sin(math.radians(point_degree))*size))+x_pos)
        points_list.append(int(round(math.cos(math.radians(point_degree))*size))+y_pos)
    fade_out=0
    method=0
    gradient_length=0
    gimp_be.pdb.gimp_paintbrush(drawable, fade_out, len(points_list), points_list, method, gradient_length)

#draw a grid of polygons of N sides
def drawPolygonGrid(size=60,sides=3, angle_offset=0):
    image = gimp_be.gimp.image_list()[0]
    drawable = gimp_be.pdb.gimp_image_active_drawable(image)
    if sides%2 == 1 or sides>4:
        for y in range(0-image.height/10,image.height+image.height/10, size):
            x_loop=0
            for x in range(0-image.width/10, image.width+image.width/10, size):
                if x_loop%2==1:
                    drawPolygon(sides,size-size/2,x-(size/2),y,360/sides)
                else:
                    drawPolygon(sides,size-size/2,x,y,0)
                x_loop=x_loop+1
    else:
        for x in range(0-image.height/10,image.height+image.height/10, size):
            for y in range(0-image.width/10, image.width+image.width/10, size):
                drawPolygon(sides,size/3,x,y,0)
    degree_between_points=360/sides
    points_list=[]
    for x in range(0,sides+1):
        point_degree=math.radians(degree_between_points*x+angle_offset)
        points_list.append(int(round(math.sin(point_degree)*size)))
        points_list.append(int(round(math.cos(point_degree)*size)))
    fade_out=0
    method=0
    gradient_length=0
    gimp_be.pdb.gimp_paintbrush(drawable, fade_out, len(points_list), points_list, method, gradient_length)

def drawFrygon(sides=5,size=300,x_pos=0,y_pos=0, angle_offset=0):
    image = gimp_be.gimp.image_list()[0]
    drawable = gimp_be.pdb.gimp_image_active_drawable(image)
    if y_pos==0:
        y_pos=image.height/2
        if x_pos==0:
            x_pos=image.width/2
    degree_between_points=360/sides
    points_list=[]
    for x in range(0,sides+1):
        point_degree=degree_between_points*x+angle_offset
        points_list.append(int(round(math.sin(point_degree)*size))+y_pos)
        points_list.append(int(round(math.cos(point_degree)*size))+x_pos)
    fade_out=0
    method=0
    gradient_length=0
    gimp_be.pdb.gimp_paintbrush(drawable, fade_out, len(points_list), points_list, method, gradient_length)

def drawFrygonGrid(size=120,sides=13):
    global height, width
    if sides%2 == 1:
        for x in range(0,height,size):
            x_deep=0
            for y in range(0, width,size):
                if x_deep%2==1:
                    drawFrygon(sides,size,x,y-(size/2),0)
                else:
                    drawFrygon(sides,size,x,y,0)
                x_deep=x_deep+1
    else:
        for x in range(0,height, size):
            for y in range(0, width, size):
                drawFrygon(sides,size,x,y,0)
