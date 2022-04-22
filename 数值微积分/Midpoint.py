# （复合）中点法则积分

import sympy as sp
import re
x = sp.symbols('x')


def Midpoint(expr, a, b, m : int):
    h = (b - a) / m
    i = sp.symbols('i')
    return sp.N(h *
        sp.Sum(expr.subs(x, a + (2 * i - 1) * h / 2), (i, 1, m)).doit()    
    )


if __name__ == '__main__':
    expr = sp.sympify(input())
    a, b, m = map(sp.sympify, re.split(r'[\s,;]+', input().strip()))
    print(Midpoint(expr, a, b, m))