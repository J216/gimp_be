from gimpfu import pdb, gimp
import math

#draws polygon of N sides at a x-y location
def drawPolygon(sides=5,size=300,x_pos=0,y_pos=0, angle_offset=0):
    image = gimp.image_list()[0]
    drawable = pdb.gimp_image_active_drawable(image)
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
    pdb.gimp_paintbrush(drawable, fade_out, len(points_list), points_list, method, gradient_length)


#draw a grid of polygons of N sides
def drawPolygonGrid(size=60,sides=3, angle_offset=0):
    image = gimp.image_list()[0]
    drawable = pdb.gimp_image_active_drawable(image)
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
    pdb.gimp_paintbrush(drawable, fade_out, len(points_list), points_list, method, gradient_length)


def drawFrygon(sides=5,size=300,x_pos=0,y_pos=0, angle_offset=0):
    image = gimp.image_list()[0]
    drawable = pdb.gimp_image_active_drawable(image)
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
    pdb.gimp_paintbrush(drawable, fade_out, len(points_list), points_list, method, gradient_length)


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