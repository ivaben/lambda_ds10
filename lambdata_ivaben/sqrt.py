def lazy_sqrt(x):
    """Takes x and returns square root"""
    return x**0.5

def built_sqrt(x):
    """Uses built in math library to get squere root"""
    from math import sqrt
    return sqrt(x)

def newton_sqrt1(x):
    """Return the squere root of x using Newton's Method"""
    val=x
    while True:
        last = val
        val = (val+x/val)* 0.5
        if abs(val - last) < 1e-9:
            break
    return val




