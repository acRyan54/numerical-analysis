#bezier样条
from sympy import *
from sympy.plotting import plot_parametric
import re

t = symbols('t')

if __name__ == '__main__':
    X, Y = [0]*5, [0]*5
    for i in range(1, 5):
        recv = re.split(r'[\s,]+', input().strip())
        X[i], Y[i] = eval(recv[0]), eval(recv[1])
    b_x = 3*(X[2] - X[1])
    c_x = 3*(X[3] - X[2]) - b_x
    d_x = X[4] - X[1] - b_x - c_x
    b_y = 3*(Y[2] - Y[1])
    c_y = 3*(Y[3] - Y[2]) - b_y
    d_y = Y[4] - Y[1] - b_y - c_y
    xt = X[1] + b_x*t + c_x*t**2 + d_x*t**3
    yt = Y[1] + b_y*t + c_y*t**2 + d_y*t**3
    print((xt,yt))
    plot_parametric((xt, yt), (t, 0, 1), xlim=(-2,2), ylim=(-2,2))