# Newton
from sympy import *
x = symbols('x')

def FPI(g, x0, step):
    ans = [x0]
    for i in range(step):
        ans.append(g.evalf(subs = {x:ans[i]}, n = 30))
    return ans

def cal(f, x0, step, m = 1):
    g = simplify(x - (m * f) / diff(f,x))
    return FPI(g, x0, step)


if __name__ == '__main__':
    f = simplify(sympify(input()))
    x0 = eval(input())
    step = int(eval(input()))
    m = int(eval(input()))
    ans = cal(f, x0, step, m)
    print(ans[-1])