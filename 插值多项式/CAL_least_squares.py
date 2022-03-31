# 最小二乘法 求解系统
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
    return ans_arr

if __name__ == '__main__':
    n = int(eval(input()))
    m = int(eval(input()))
    X, Y = [], []
    for i in range(m):
        recv = re.split(r'[\s,]+', input().strip())
        X.append(eval(recv[0]))
        Y.append(eval(recv[1]))
    print(Least_Squares(n, m, X, Y))