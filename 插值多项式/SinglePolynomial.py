#单项式
import numpy as np
import sympy as sp
from sympy.plotting import plot
import re

x = sp.symbols('x')

def Vandermondre(n, X):
    Van = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(X[i]**j)
        Van.append(row)
    return Van

def cal(n, X, Y):
    A = np.array(Vandermondre(n, X))
    Y = np.array(Y)
    ans_arr = np.linalg.solve(A, Y)
    ans = 0
    for i, ai in enumerate(ans_arr.tolist()):
        ans = ans + ai * x**i
    return ans
    
if __name__ == '__main__':
    num = int(eval(input()))
    X, Y = [], []
    for i in range(num):
        recv = re.split(r'[\s,]+', input().strip())
        X.append(eval(recv[0]))
        Y.append(eval(recv[1]))
    ans = cal(num, X, Y)
    print(ans)
    plot(ans, (x, -10, 10))

