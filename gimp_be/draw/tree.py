

# draw a tree
def drawTree(x1=50, y1=75, angle=270, depth=9, recursiondepth=0):
    if recursiondepth == 0:
        doLog('drawTree(' + str(x1) + ',' + str(y1) + ',' + str(angle) + ',' + str(depth) + ')')
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
    doLog('-tree stroke ' + str(ctrlPoints))
    pdb.gimp_paintbrush_default(drawable, len(ctrlPoints), ctrlPoints)
    if depth > 0:
        drawTree(x2, y2, angle - 20, depth - 1, recursiondepth + 1)
        drawTree(x2, y2, angle + 20, depth - 1, recursiondepth + 1)


# draw a tree with 3 branches per node
def drawTriTree(x1=100, y1=100, angle=270, depth=6, recursiondepth=0, size=10):
    if not recursiondepth:
        doLog('drawTriTree(' + str(x1) + ',' + str(y1) + ',' + str(angle) + ',' + str(depth) + ')')
    if depth:
        x2 = x1 + int(math.cos(math.radians(angle)) * depth * size) + random.randrange(-12, 12)
        y2 = y1 + int(math.sin(math.radians(angle)) * depth * size) + random.randrange(-12, 12)
        ctrlPoints = (x1, y1, x2, y2)
        brushSize(depth + int(size/10))
        brushColor()
        doLog('-tree stroke ' + str(ctrlPoints))
        pdb.gimp_paintbrush_default(drawable, len(ctrlPoints), ctrlPoints)
        drawTriTree(x2, y2, angle - 30, depth - 1, recursiondepth + 1,size)
        drawTriTree(x2, y2, angle, depth - 1, recursiondepth + 1,size)
        drawTriTree(x2, y2, angle + 30, depth - 1, recursiondepth + 1,size)


# draw random color tri-tree
def drawColorTriTree(x1=50, y1=75, angle=270, depth=9, recursiondepth=0):
    brushSize(depth + 1)
    if not recursiondepth:
        doLog('drawColorTriTree(' + tr(x1) + ',' + str(y1) + ',' + str(angle) + ',' + str(depth) + ')')
    if depth:
        x2 = x1 + int(math.cos(math.radians(angle)) * depth * 10.0) + random.randrange(-12, 12)
        y2 = y1 + int(math.sin(math.radians(angle)) * depth * 10.0) + random.randrange(-12, 12)
        ctrlPoints = (x1, y1, x2, y2)
        doLog('-tree stroke ' + str(ctrlPoints))
        pdb.gimp_paintbrush_default(drawable, len(ctrlPoints), ctrlPoints)
        drawColorTriTree(x2, y2, angle - 20 + random.choice(-10, -5, 0, 5, 10), depth - 1, recursiondepth + 1)
        drawColorTriTree(x2, y2, angle + random.choice(-10, -5, 0, 5, 10), depth - 1, recursiondepth + 1)
        drawColorTriTree(x2, y2, angle + 20 + random.choice(-10, -5, 0, 5, 10), depth - 1, recursiondepth + 1)


# draw a tree
def drawOddTree(x1=50, y1=75, angle=270, depth=9, recursiondepth=0):
    brushSize((depth * 8 + 30))
    if not recursiondepth:
        doLog('drawOddTree(' + str(x1) + ',' + str(y1) + ',' + str(angle) + ',' + str(depth) + ')')
    if depth:
        x2 = x1 + int(math.cos(math.radians(angle)) * depth * 10.0)
        y2 = y1 + int(math.sin(math.radians(angle)) * depth * 10.0)
        ctrlPoints = (x1, y1, x2, y2)
        doLog('-tree stroke ' + str(ctrlPoints))
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
def drawForestTree(x1=50, y1=75, angle=270, depth=9, size=10, recursiondepth=0):
    if not recursiondepth:
        doLog('drawForestTree(' + str(x1) + ',' + str(y1) + ',' + str(angle) + ',' + str(depth) + ')')
    global height
    if depth:
        x2 = x1 + int(math.cos(math.radians(angle)) * depth * 10.0)
        y2 = y1 + int(math.sin(math.radians(angle)) * depth * 10.0)
        ctrlPoints = (x1, y1, x2, y2)
        brushSize(depth * depth * (int(size / ((height - y1)) / height)) + 4)
        doLog('-tree stroke ' + str(ctrlPoints))
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
    doLog('drawForest(' + str(trees) + ',' + str(options) + ')')
    global height
    global width
    for tree in range(0, trees):
        y1 = 2 * (height / 3) + random.randrange(-1 * (height / 5), height / 5)
        x1 = random.randrange(width / 20, 19 * (width / 20))
        angle = random.randrange(250, 290)
        size = (y1 / (2.0 * (height / 3.0) + (height / 5.0))) + 4
        depth = random.randrange(3, 7)
        drawForestTree(x1, y1, angle, depth, size)
