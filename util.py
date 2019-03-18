
def eps_eq(z1, z2, eps):
    return abs(z1 - z2) < eps

def root_attraction(x, y, *, method, roots, eps) -> int:
    ans = method(complex(x, y))
    for i in range(0, len(roots)):
        if eps_eq(ans, roots[i-1], eps):
            return i + 1
    return 0
