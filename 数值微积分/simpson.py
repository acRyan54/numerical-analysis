# （复合）Simpson法则积分

import sympy as sp
import re
x = sp.symbols('x')


def Simpson(expr, a, b, m : int):
    if m == 1: # 非复合情况
        h = (b - a) / 2
        return sp.N(h/3 * (
            expr.subs(x, a) + 
            4 * expr.subs(x, a + h) +
            expr.subs(x, b)
        ))
    
    m //= 2 # 如果m不能被2整除，则自动舍去最后一位
    h = (b - a) / (2 * m)
    i = sp.symbols('i')
    return sp.N(h/3 * (
        expr.subs(x, a) +
        expr.subs(x, b) +
        4 * sp.Sum(expr.subs(x, a + (2 * i - 1) * h), (i, 1, m)).doit() +
        2 * sp.Sum(expr.subs(x, a + (2 * i) * h), (i, 1, m - 1)).doit()    
    ))


if __name__ == '__main__':
    expr = sp.sympify(input())
    a, b, m = map(sp.sympify, re.split(r'[\s,;]+', input().strip()))
    print(Simpson(expr, a, b, m))