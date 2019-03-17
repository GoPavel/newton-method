import math
from math import sqrt, inf


def f(z):
    return z ** 3 - 1


def df(z):
    return 3 * z ** 2


root1 = complex(1, 0)
root2 = complex(-1/2, sqrt(3)/2)
root3 = complex(-1/2, -sqrt(3)/2)


def eq(z1, z2):
    eps = 1e-15
    return abs(z1 - z2) < eps


assert eq(f(root1), 0) and eq(f(root2), 0) and eq(f(root3), 0)


def newton_iters(z0, iters):
    prev_z = z0
    cur_z = z0
    for i in range(iters):
        if df(prev_z) == 0:
            return complex(inf, inf)
        cur_z = prev_z - f(prev_z) / df(prev_z)
        prev_z = cur_z
    return cur_z


ITERS_CNT = 100
def get_color(x, y):
    ans = newton_iters(complex(x, y), ITERS_CNT)
    if eq(ans, root1):
        return 0
    elif eq(ans, root2):
        return 1
    elif eq(ans, root3):
        return 2
    else:
        return 3
