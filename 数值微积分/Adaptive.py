# 自适应积分

import sympy as sp
import re
x = sp.symbols('x')


def Simpson(expr, a, b, m):
    m //= 2
    h = (b - a) / (2 * m)
    i = sp.symbols('i')
    return sp.N(h/3 * (
        expr.subs(x, a) +
        expr.subs(x, b) +
        4 * sp.Sum(expr.subs(x, a + (2 * i - 1) * (b - a) / (2 * m)), (i, 1, m)).doit() +
        2 * sp.Sum(expr.subs(x, a + (2 * i) * (b - a) / (2 * m)), (i, 1, m - 1)).doit()    
    ))


if __name__ == '__main__':
    expr = sp.sympify(input())
    a, b, m = map(sp.sympify, re.split(r'[\s,;]+', input().strip()))
    print(Simpson(expr, a, b, m))