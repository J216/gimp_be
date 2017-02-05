import math, random
from gimp_be.settings.brush_settings import brushColor, brushSize
from gimpfu import pdb, gimp


# draw a tree
def drawTree(x1=-1, y1=-1, angle=270, depth=9, recursiondepth=0):
    image = gimp.image_list()[0]
    drawable = pdb.gimp_image_active_drawable(image)
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
    pdb.gimp_paintbrush_default(drawable, len(ctrlPoints), ctrlPoints)
    if depth > 0:
        drawTree(x2, y2, angle - 20, depth - 1, recursiondepth + 1)
        drawTree(x2, y2, angle + 20, depth - 1, recursiondepth + 1)


# draw a tree with 3 branches per node
def drawTriTree(x1=-1, y1=-1, angle=270, depth=6, recursiondepth=0, size=10):
    image = gimp.image_list()[0]
    drawable = pdb.gimp_image_active_drawable(image)
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
        pdb.gimp_paintbrush_default(drawable, len(ctrlPoints), ctrlPoints)
        drawTriTree(x2, y2, angle - 30, depth - 1, recursiondepth + 1,size)
        drawTriTree(x2, y2, angle, depth - 1, recursiondepth + 1,size)
        drawTriTree(x2, y2, angle + 30, depth - 1, recursiondepth + 1,size)


# draw random color tri-tree
def drawColorTriTree(x1=-1, y1=-1, angle=270, depth=9, recursiondepth=0):
    image = gimp.image_list()[0]
    drawable = pdb.gimp_image_active_drawable(image)
    if x1 == -1:
        x1 = image.width/2
    if y1 == -1:
        y1 = image.height/2
    brushSize(depth + 1)
    if depth:
        x2 = x1 + int(math.cos(math.radians(angle)) * depth * 10.0) + random.randrange(-12, 12)
        y2 = y1 + int(math.sin(math.radians(angle)) * depth * 10.0) + random.randrange(-12, 12)
        ctrlPoints = (x1, y1, x2, y2)
        pdb.gimp_paintbrush_default(drawable, len(ctrlPoints), ctrlPoints)
        drawColorTriTree(x2, y2, angle - 20 + random.choice(-10, -5, 0, 5, 10), depth - 1, recursiondepth + 1)
        drawColorTriTree(x2, y2, angle + random.choice(-10, -5, 0, 5, 10), depth - 1, recursiondepth + 1)
        drawColorTriTree(x2, y2, angle + 20 + random.choice(-10, -5, 0, 5, 10), depth - 1, recursiondepth + 1)


# draw a tree
def drawOddTree(x1=-1, y1=-1, angle=270, depth=9, recursiondepth=0):
    image = gimp.image_list()[0]
    drawable = pdb.gimp_image_active_drawable(image)
    if x1 == -1:
        x1 = image.width/2
    if y1 == -1:
        y1 = image.height/2
    brushSize((depth * 8 + 30))
    if depth:
        x2 = x1 + int(math.cos(math.radians(angle)) * depth * 10.0)
        y2 = y1 + int(math.sin(math.radians(angle)) * depth * 10.0)
        ctrlPoints = (x1, y1, x2, y2)
        pdb.gimp_paintbrush_default(drawable, len(ctrlPoints), ctrlPoints)
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
def drawForestTree(x1=-1, y1=-1, angle=270, depth=9, size=10, recursiondepth=0):
    image = gimp.image_list()[0]
    drawable = pdb.gimp_image_active_drawable(image)
    if x1 == -1:
        x1 = image.width/2
    if y1 == -1:
        y1 = image.height/2
    if depth:
        x2 = x1 + int(math.cos(math.radians(angle)) * depth * 10.0)
        y2 = y1 + int(math.sin(math.radians(angle)) * depth * 10.0)
        ctrlPoints = (x1, y1, x2, y2)
        brushSize(depth * depth * (int(size / ((image.height - y1)) / image.height)) + 4)
        pdb.gimp_paintbrush_default(drawable, len(ctrlPoints), ctrlPoints)
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
    image = gimp.image_list()[0]
    for tree in range(0, trees):
        y1 = 2 * (image.height / 3) + random.randrange(-1 * (image.height / 5), image.height / 5)
        x1 = random.randrange(image.width / 20, 19 * (image.width / 20))
        angle = random.randrange(250, 290)
        size = (y1 / (2.0 * (image.height / 3.0) + (image.height / 5.0))) + 4
        depth = random.randrange(3, 7)
        drawForestTree(x1, y1, angle, depth, size)
