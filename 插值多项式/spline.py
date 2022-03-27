#Spline 三次样条
import sympy as sp
import numpy as np
from sympy.plotting import plot
import re

x = sp.symbols('x')

def cal(n, X, Y, case='a', *, v1=0, vn=0):
    S = []
    A = np.zeros((n, n)) #初始化
    r = np.zeros((n, 1))
    dx, dy = [], []
    for i in range(n-1):
        dx.append(X[i+1] - X[i])
        dy.append(Y[i+1] - Y[i])
    for i in range(1, n-1):
        A[i, i-1:i+2] = [dx[i-1], 2*(dx[i-1] + dx[i]), dx[i]]
        r[i, 0] = 3 * (dy[i]/dx[i] - dy[i-1]/dx[i-1])
    
    #自然a
    if case == 'a':
        A[0, 0], A[n-1, n-1] = 1, 1
    #曲率调整b
    if case == 'b':
        A[0, 0], A[n-1, n-1] = 2, 2
        r[0, 0], r[n-1, 0] = v1, vn
    #钳制c
    if case == 'c':
        A[0, 0:2] = [2*dx[0], dx[0]]
        r[0, 0] = 3*(dy[0]/dx[0] - v1)
        A[n-1, n-2:] = [dx[n-2], 2*dx[n-2]]
        r[n-1, 0] = 3*(vn - dy[n-2]/dx[n-2])
    #抛物线d
    if case == 'd':
        A[0, 0:2], A[n-1, n-2:] = [1, -1], [1, -1]
    #非纽结e
    if case == 'e':
        A[0, 0:3] = [dx[1], -dx[0]-dx[1], dx[0]]
        A[n-1, n-3:] = [dx[n-2], -dx[n-3]-dx[n-2], dx[n-3]]
    
    coeff = np.zeros((n, 4))
    coeff[..., 0] = Y #a
    coeff[..., 2] = np.linalg.solve(A, r).flatten() #c
    for i in range(n-1):
        coeff[i, 1] = dy[i]/dx[i] - dx[i]/3 * (coeff[i+1, 2] + 2*coeff[i, 2]) #b
        coeff[i, 3] = (coeff[i+1, 2] - coeff[i, 2])/(3*dx[i]) #d
    coeff = coeff[:-1, ...]
    for i in range(n-1):
        S.append(coeff[i][0] + coeff[i][1]*(x-X[i]) + coeff[i][2]*(x-X[i])**2 + coeff[i][3]*(x-X[i])**3)
    return (coeff, S)
    
if __name__ == '__main__':
    num = int(eval(input()))
    X, Y = [], []
    for i in range(num):
        recv = re.split(r'[\s,]+', input().strip())
        X.append(eval(recv[0]))
        Y.append(eval(recv[1]))
    case = input().strip()
    ans = cal(num, X, Y, case)
    print(ans)

