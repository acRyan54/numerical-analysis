#FixedPointIteration
from sympy import *
x = symbols('x')

def cal(g, x0, step):
    ans = [x0]
    for i in range(step):
        ans.append(g.evalf(subs = {x:ans[i]}, n = 30))
    return ans

if __name__ == '__main__':
    g = simplify(sympify(input()))
    x0 = eval(input())
    step = int(eval(input()))
    ans = cal(g, x0, step)
    print(ans[-1])