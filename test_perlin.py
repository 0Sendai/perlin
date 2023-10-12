from math import sin,cos,radians
from random import randint,uniform


class vector:
    def __init__(self,x=0,y=0):
        """This function creates two-dimensional vectors"""
        self.x = x
        self.y = y


def shuffle(array):
    """The function will shuffle the elements in this array."""
    e = len(array)-1
    while e > 0:
        index = round(randint(0,len(array)-1))
        temp  = array[e]

        array[e] = array[index]
        array[index] = temp
        e -= 1

def makeperm():
    """This code implements the makeperm function,
       which creates and returns a permutation list.
       It first creates a list of numbers from 0 to 255,
       then shuffles it randomly using the shuffle function,
       and finally adds duplicate items to the end of the list.
       The result will be a list containing randomly shuffled numbers
       from 0 to 255."""
    perm = []
    for i in range(0,256):
        perm.append(i)
    shuffle(perm)
    for i in range(0,256):
        perm.append(perm[i])
    return perm

perm = makeperm()

def get_random_gradient(v):
    """Depending on the value of v,
       it selects one of four possible gradients:
       (1.0, 1.0), (1.0, -1.0), (-1.0, 1.0), or (-1.0, -1.0)
       and returns it."""
    h = v & 3
    if h == 0:
        res = vector(1.0,1.0)
    elif h == 1:
        res = vector(1.0,-1.0)
    elif h == 2:
        res = vector(-1.0,1.0)
    else: 
        res = vector(-1.0,-1.0)
   
    return res


def dist_grad_prod(x0, y0, x, y,v):
    """This code implements the function dist_grad_prod,
       which calculates the dot product between the random
       gradient and a vector representing the difference in coordinates
       between two points (x0, y0) and (x, y).
       The result of this product is returned from the function."""
    gradient = get_random_gradient(v)

    dx = x0 - x
    dy = y0 - y

    return (dx * gradient.x + dy * gradient.y)


def interpolate(d0,d1,weight):
    """This code implements the interpolate function,
       which calculates the interpolated value between
       d0 and d1 using the weight factor."""
    return (d1-d0) * (3.0 - weight * 2.0) * weight * weight + d0

def perlin(x,y):
    """This code implements a perlin function that is used to
        calculate noise in two-dimensional (x, y) coordinates.
        It calculates the integer coordinates of cells (x0, y0)
        as well as the coordinates of neighboring cells (x1, y1).
        These values are used for further noise calculations."""
    x0 = int(x)
    y0 = int(y)
    x1 = x0 + 1
    y1 = y0 + 1

    wx = x - x0
    wy = y - y0

    valtopr = perm[perm[x1]+y1]
    valtopl = perm[perm[x0]+y1]
    valbotr = perm[perm[x1]+y0]
    valbotl = perm[perm[x0]+y0]

    d0 = dist_grad_prod(x0, y0, x, y,valbotl)
    d1 = dist_grad_prod(x1, y0, x, y,valbotr)
    ix0 = interpolate(d0, d1, wx)

    d0 = dist_grad_prod(x0, y1, x, y,valtopl)
    d1 = dist_grad_prod(x1, y1, x, y,valtopr)
    ix1 = interpolate(d0, d1,wx)

    return interpolate(ix0, ix1,wy)

"""__________________________________________________________________________________________________________________________________________________________"""

import dearpygui.dearpygui as dpg
import array
import test_perlin as perlin

"""Creating a working field"""
dpg.create_context()

grid_size = 100
width = 400
heigth = 400
rawdata = [0] * width * heigth * 3
octav = 5

def perlin():
    """This code is used to generate Perlin noise on a 2D mesh
       with dimensions width and height. Each point (x, y) in
       the grid calculates a noise value and uses it to determine
       the brightness of the pixel's color. The resulting values
       are stored in the raw_data array, which will
       be used to create an image or other noise visualization."""
    for x in range(0,width):
        for y in range(0,heigth):

            index = (y * width + x) * 3

            angle = 0

            val = perlin.perlin(x octav /grid_size, y octav/grid_size)

            val = 1.2

            if val > 1.0: val = 1.0
            elif val < -1.0: val = -1.0

            color = int(((val + 1.0) 0.5 )* 255)

            raw_data[index] = val
            raw_data[index+1] = val
            rawdata[index+2] = val

""""This code is used to create a texture based
    on the generated Perlin noise and register
    it using the dpg library."""
perlin()
raw_data = array.array('f', raw_data)

with dpg.texture_registry():
    dpg.add_raw_texture(width=width, height=heigth, default_value=raw_data, format=dpg.mvFormat_Float_rgb, tag="texture_tag")



"""This code is used to create a window displaying
   the generated Perlin noise and display it in the
   user interface using the Dear PyGui library."""
with dpg.window(label="perlin"):
    dpg.add_image("texture_tag")

dpg.create_viewport(title='perlin test', width=500, height=500)
dpg.setup_dearpygui()
dpg.show_viewport()
while dpg.is_dearpygui_running():
    dpg.render_dearpygui_frame()
dpg.destroy_context()
