from gimpfu import gimp, pdb
import random


def brushSize(size=-1):
    """"
    Set brush size
    """
    image = gimp.image_list()[0]
    drawable = pdb.gimp_image_active_drawable(image)
    if size < 1:
        size = random.randrange(2, ((image.height + image.width) / 8))
    pdb.gimp_context_set_brush_size(size)


# Set brush opacity
def brushOpacity(op=-1):
    if op == -1:
        op = random.randrange(15, 100)
    pdb.gimp_brushes_set_opacity(op)
    return op


# Set random brush color no parameters set random
def brushColor(r1=-1, g1=-1, b1=-1, r2=-1, g2=-1, b2=-1):
    if not r1 == -1:
        pdb.gimp_context_set_foreground((r1, g1, b1))
    if not r2 == -1:
        pdb.gimp_context_set_background((r2, g2, b2))
    elif r1 == -1:
        r1 = random.randrange(0, 255)
        g1 = random.randrange(0, 255)
        b1 = random.randrange(0, 255)
        r2 = random.randrange(0, 255)
        g2 = random.randrange(0, 255)
        b2 = random.randrange(0, 255)
        pdb.gimp_context_set_foreground((r1, g1, b1))
        pdb.gimp_context_set_background((r2, g2, b2))
    return (r1, g1, b1, r2, g2, b2)


#set gray scale color
def grayColor(gray_color):
    pdb.gimp_context_set_foreground((gray_color, gray_color, gray_color))


# Set random brush
def randomBrush():
    num_brushes, brush_list = pdb.gimp_brushes_get_list('')
    brush_pick = brush_list[random.randrange(0, len(brush_list))]
    pdb.gimp_brushes_set_brush(brush_pick)
    return brush_pick


# Set random brush dynamics
def randomDynamics():
    dynamics_pick = random.choice(pdb.gimp_dynamics_get_list('')[1])
    pdb.gimp_context_set_dynamics(dynamics_pick)
    return dynamics_pick

