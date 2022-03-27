#Bisection
from sympy import *
x = symbols('x')

def func(f, var):
    return f.evalf(subs = {x: var}, n = 30)

def cal(f, a, b, tol):
    fa = func(f, a)
    fb = func(f, b)
    while (b - a) / 2 > tol:
        c = (b + a) / 2
        fc = func(f, c)
        if fc == 0:
            return c
        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
    return (b + a) / 2
        
if __name__ == '__main__':
    f = simplify(sympify(input()))
    a = eval(input())
    b = eval(input())
    tol = eval(input())
    print(cal(f, a, b, tol))