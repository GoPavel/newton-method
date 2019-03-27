from math import inf
from util import eps_eq

def get_root(*, f, fd, z0, eps, roots, max_iteration_count):
    prev_z = z0
    cur_z = z0
    for iter in range(0, max_iteration_count):
        for i, r in enumerate(roots):
            if eps_eq(cur_z, r, eps):
                return (i+1, iter)
        if fd(prev_z) == 0:
            return complex(inf, inf)
        cur_z = prev_z - f(prev_z) / fd(prev_z)
        prev_z = cur_z
    return (0, max_iteration_count)
