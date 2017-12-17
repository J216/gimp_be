import numpy as np
from gimpfu import gimp, pdb

def jL(segments=30):
    image = gimp.image_list()[0]
    drawable = pdb.gimp_image_active_drawable(image)
    x=range(0,image.width,image.width/segments)
    y_dist=np.random.randn(segments)
    y_dist=y_dist*(image.height*0.9)
    y=[]
    for i in y_dist:
        y.append(abs(int(i))+image.height*0.05)
    cord=[]
    for i in y:
        cord.append(x.pop())
        cord.append(i)
    pdb.gimp_paintbrush_default(drawable, len(cord), cord)