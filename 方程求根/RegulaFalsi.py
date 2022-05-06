#Regula Falsi 试位法
from sympy import *
x = symbols('x')

def func(f, var):
    return f.evalf(subs = {x: var}, n = 30)

def cal(f, a, b, step):
    fa = func(f, a)
    fb = func(f, b)
    for i in range(step):
        c = (b*fa - a*fb) / (fa - fb)
        fc = func(f, c)
        if fc == 0:
            return c
        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
    return (b*fa - a*fb) / (fa - fb)
        
        

if __name__ == '__main__':
    f = simplify(sympify(input()))
    a = eval(input())
    b = eval(input())
    step = int(eval(input()))
    print(cal(f, a, b, step))