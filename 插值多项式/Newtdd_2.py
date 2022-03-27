# 牛顿差商 n > 2 实时更新
import sympy as sp
from sympy.plotting import plot
import re

x = sp.symbols('x')

def cal(n, X, Y, P_last):
    f = {}
    f[(n, n)] = Y[n]
    if n == 0: #特判
        return f[(n, n)]
    for i in range(n - 1, -1, -1):
        f[(i, n)] = (f[(i, n-1)] - f[(i+1, n)]) / (X[i] - X[n])
    tmp = f[(0, n)]
    for i in range(n):
        tmp = tmp * (x - X[i])
    return P_last + tmp

if __name__ == '__main__':
    X, Y = [], []
    P = 0
    num = int(eval(input()))
    for i in range(num):
        recv = re.split(r'[\s,]+', input().strip())
        X.append(eval(recv[0]))
        Y.append(eval(recv[1]))
        P = cal(i, X, Y, P)
        plot(P, (x, -10, 10), title='$'+str(sp.latex(sp.expand(sp.simplify(P))))+'$')