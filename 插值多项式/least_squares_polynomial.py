# 最小二乘法 插值多项式
from turtle import color
import numpy as np
import sympy as sp
from matplotlib import pyplot as plt 
import re

x = sp.symbols('x')

def Vandermondre(n, m, X):
    Van = []
    for i in range(m):
        col = []
        for j in range(n):
            col.append(X[i]**j)
        Van.append(col)
    return np.array(Van)

def Least_Squares(n, m, X, Y):
    A = Vandermondre(n, m, X)
    Y = np.array(Y)
    ans_arr = np.linalg.solve(np.matmul(A.T, A), np.matmul(A.T, Y))
    ans = 0
    for i, ai in enumerate(ans_arr.tolist()):
        ans = ans + ai * x**i
    return ans

if __name__ == '__main__':
    n = int(eval(input())) + 1 # n阶多项式, 但计算时用P_{n-1}
    m = int(eval(input()))
    X, Y = [], []
    for i in range(m):
        recv = re.split(r'[\s,]+', input().strip())
        X.append(eval(recv[0]))
        Y.append(eval(recv[1]))
    p_poly = Least_Squares(n, m, X, Y)
    print(p_poly)
    p_func = sp.lambdify(x, p_poly, 'numpy') ###
    
    r = np.array(Y) - p_func(np.array(X)) # 计算误差
    RMSE = np.linalg.norm(r, ord=2) / m**0.5
    print("RMSE=", RMSE)
    
    t = np.arange(-5, 5, 0.01)
    plt.plot(t, p_func(t), '-b')
    plt.scatter(X, Y, color='r')
    plt.show()