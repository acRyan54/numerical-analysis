# Secant
from sympy import *
x = symbols('x')

def cal(f, x0, x1, step):
    ans = [x0, x1]
    for i in range(1, step + 1):
        x_i0 = ans[i - 1]
        x_i1 = ans[i]
        f_i0 = f.evalf(subs = {x : x_i0}, n = 30)
        f_i1 = f.evalf(subs = {x : x_i1}, n = 30)
        if f_i0 == f_i1:
            break
        f_i2 = x_i1 - (f_i1 * (x_i1 - x_i0)) / (f_i1 - f_i0)
        ans.append(f_i2)
    return ans


if __name__ == '__main__':
    f = simplify(sympify(input()))
    x0 = eval(input())
    x1 = eval(input())
    step = int(eval(input()))
    ans = cal(f, x0, x1, step)
    print(ans[-1])