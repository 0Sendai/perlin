```
```get_random_gradient(v):
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
```



Примеры:
v = 3: h = 3 & 3 = 3; res = vector(-1.0,-1.0)
v = 2: h = 2 & 3 = 2; res = vector(-1.0,1.0)
v = 1: h = 1 & 3 = 1; res = vector(1.0,-1.0)
v = 0: h = 0 & 3 = 0; res = vector(1.0,1.0)




```dist_grad_prod(x0, y0, x, y, v):
gradient = get_random_gradient(v)

    dx = x0 - x
    dy = y0 - y

    return (dx * gradient.x + dy * gradient.y)
```

Примеры:
x = 2; y = 1

gradient = vector(1.0,1.0): dx = 1 - 2 = -1
							dy = 1 - 1 = 0
							dx * gradient.x + dy * gradient.y = -2

gradient = vector(1.0,-1.0): dx = 1 - 2 = -1
							dy = -1 - 1 = -2
							dx * gradient.x + dy * gradient.y = -4
							
gradient = vector(-1.0,1.0): dx = -1 - 2 = -3
							dy = 1 - 1 = 0
							dx * gradient.x + dy * gradient.y = -6

gradient = vector(-1.0,-1.0): dx = -1 - 2 = -3
							dy = -1 - 1 = -2
							dx * gradient.x + dy * gradient.y = -8