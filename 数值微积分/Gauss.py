# Gauss-Legendre积分

import sympy as sp
import re
x = sp.symbols('x')


def Gauss(expr, a, b, n : int = 4): # 四阶高斯积分
    xi = [-((15+2*30**.5)/35)**.5, -((15-2*30**.5)/35)**.5, ((15-2*30**.5)/35)**.5, ((15+2*30**.5)/35)**.5]
    ci = [(90-5*30**.5)/180, (90+5*30**.5)/180, (90+5*30**.5)/180, (90-5*30**.5)/180]
    t = sp.symbols('t')
    ans = 0
    for i in range(4):
        ans += ci[i] * sp.N(expr.subs(x, ((b - a) * xi[i] + b + a) / 2))
    return ans * (b - a) / 2


if __name__ == '__main__':
    expr = sp.sympify(input())
    a, b = map(sp.sympify, re.split(r'[\s,;]+', input().strip()))
    print(Gauss(expr, a, b))