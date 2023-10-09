from math import sin,cos

class vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y


def get_random_gradient(x,y):
    #рандомный вектор (необходимо реализовать )
    pass

    #То, что должно получиться :
    #res = vector()
    #return res


def dist_grad_prod(gradient:vector, x0, y0, x, y):
    #скалярное произведение между рандомным вектором и вектором до точки

    # x,y - координаты точки

    dx = x - x0
    dy = y - y0

    return dx * gradient.x + dy * gradient.y

def vector_rotate(v:vector, angle):
    res = vector()
    cosres = cos(angle)
    sinres = sin(angle)

    res.x = v.x * cosres - v.y * sinres
    res.y = v.x * sinres + v.y * cosres
    return res

#def interpolate(взять из sci-py)

def perlin(x,y,angle):
    #вычисление шума в x,y
    
    #вычисление координат клеток
    x0 = 