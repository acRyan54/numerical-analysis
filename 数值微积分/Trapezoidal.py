# （复合）梯形法则积分

import sympy as sp
import re
x = sp.symbols('x')


def Trapizoidal(expr, a, b, m : int):
    if m == 1: # 非复合情况
        h = b - a
        return sp.N(h/2 * (
            expr.subs(x, a) + 
            expr.subs(x, b)
        ))
    
    h = (b - a) / m
    i = sp.symbols('i')
    return sp.N(h/2 * (
        expr.subs(x, a) +
        expr.subs(x, b) +
        2 * sp.Sum(expr.subs(x, a + i * h), (i, 1, m - 1)).doit()    
    ))


if __name__ == '__main__':
    expr = sp.sympify(input())
    a, b, m = map(sp.sympify, re.split(r'[\s,;]+', input().strip()))
    print(Trapizoidal(expr, a, b, m))