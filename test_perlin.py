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
       which creates and returns a permutation list."""
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
       it selects one of four possible gradients and returns it."""
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
    """The function calculates the dot product between the random gradient and the vector"""
    gradient = get_random_gradient(v)

    dx = x0 - x
    dy = y0 - y

    return (dx * gradient.x + dy * gradient.y)


def interpolate(d0,d1,weight):
    """This code implements the interpolate function."""
    return (d1-d0) * (3.0 - weight * 2.0) * weight * weight + d0

def perlin(x,y):
    """This function is used to calculate perlin noise in two-dimensional (x, y) coordinates."""

    """Grid coordinates, rounded to nearest integer"""
    x0 = int(x)
    y0 = int(y)
    x1 = x0 + 1
    y1 = y0 + 1

    wx = x - x0
    wy = y - y0

    """This block of code gets the values from the perm array for the four corners of the cell that contains point (x, y)."""
    valtopr = perm[perm[x1]+y1]
    valtopl = perm[perm[x0]+y1]
    valbotr = perm[perm[x1]+y0]
    valbotl = perm[perm[x0]+y0]

    """Calculates the product of the distance between points (x0, y0) and (x, y) and the gradient."""
    d0 = dist_grad_prod(x0, y0, x, y,valbotl)
    d1 = dist_grad_prod(x1, y0, x, y,valbotr)
    ix0 = interpolate(d0, d1, wx)

    d0 = dist_grad_prod(x0, y1, x, y,valtopl)
    d1 = dist_grad_prod(x1, y1, x, y,valtopr)
    ix1 = interpolate(d0, d1,wx)

    return interpolate(ix0, ix1,wy)
