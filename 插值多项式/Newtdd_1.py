# 牛顿差商 n > 2
import sympy as sp
from sympy.plotting import plot
import re

x = sp.symbols('x')

def cal(n, X, Y):
    f = {}
    for i in range(n): #初始化
        f[(i, i)] = Y[i]
    for i in range(2, n + 1): #差商计算
        for j in range(n + 1 - i):
            f[(j, j + i - 1)] = (f[(j + 1, j + i - 1)]  - f[(j, j + i - 2)]) / (X[j + i - 1] - X[j])
    P = 0
    for i in range(n):
        tmp = f[(0, i)]
        for j in range(i):
            tmp = tmp * (x - X[j])
        P = P + tmp
    return P

if __name__ == '__main__':
    num = int(eval(input()))
    X, Y = [], []
    for i in range(num):
        recv = re.split(r'[\s,]+', input().strip())
        X.append(eval(recv[0]))
        Y.append(eval(recv[1]))
    ans = cal(num, X, Y)
    # print(ans)
    print(sp.expand(sp.simplify(ans)))
    plot(ans, (x, -10, 10))