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
