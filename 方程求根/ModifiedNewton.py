# ModifiedNewton
from sympy import *
x = symbols('x')


def FPI(g, x0, step):
    ans = [x0]
    for i in range(step):
        ans.append(g.evalf(subs={x: ans[i]}, n=30))
    return ans


def cal(f, x0, step):
    g = simplify(x - (f * diff(f, x)) / (diff(f, x) ** 2 - f * diff(f, x, 2)))
    return FPI(g, x0, step)


if __name__ == '__main__':
    f = simplify(sympify(input()))
    x0 = eval(input())
    step = int(eval(input()))
    ans = cal(f, x0, step)
    print(ans[-1])
