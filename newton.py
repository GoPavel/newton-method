from math import inf

def get_root(f, df, z0, count_iteration):
    prev_z = z0
    cur_z = z0
    for i in range(count_iteration):
        if df(prev_z) == 0:
            return complex(inf, inf)
        cur_z = prev_z - f(prev_z) / df(prev_z)
        prev_z = cur_z
    return cur_z
