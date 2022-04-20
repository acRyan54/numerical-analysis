import sympy as sp
import numpy as np
import re
x = sp.symbols('x')


def romberg(expr, a, b, n):
    np.set_printoptions(precision = 12)
    h = (b - a) / 2**(np.arange(0, n))
    r = np.zeros((n, n))
    r[0][0] = h[0] / 2 * (expr.subs(x, a) + expr.subs(x, b))
    for j in range(1, n):
        i = sp.symbols('i')
        r[j][0] = (1/2 * r[j-1][0] + h[j] *
                   sp.Sum(expr.subs(x, a + (2 * i - 1) * h[j]), (i, 1, 2**(j - 1))).doit())
        for k in range(1, j + 1):
            r[j][k] = (4**k * r[j][k-1] - r[j-1][k-1]) / (4**k - 1)
    return r
    
if __name__ == '__main__':
    expr = sp.sympify(input())
    a, b, n = map(sp.sympify, re.split(r'[\s,;]+', input().strip()))
    print(romberg(expr, a, b, n))