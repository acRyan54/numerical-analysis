import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import ginput

from Bezier_curve import BezierCurve
plt.ion()

def tellme(s):
    # print(s)
    plt.title(s, fontsize=16)
    plt.draw()

def bezierdraw(num=3, color='orange'):
    
    tellme('click for P0')
    P0 = np.asarray(ginput(1))[0]
    plt.scatter(P0[0], P0[1], c=color, marker='o')
    curves_pos = []
    for i in range(num):
        tellme('click for P1, P2, P3; round {}'.format(i+1))
        P1 = np.asarray(ginput(1))[0]
        plt.scatter(P1[0], P1[1], c=color, marker='s')
        P2 = np.asarray(ginput(1))[0]
        plt.scatter(P2[0], P2[1], c=color, marker='s')
        P3 = np.asarray(ginput(1))[0]
        plt.scatter(P3[0], P3[1], c=color, marker='o')
        control_points = np.asarray([P0, P1, P2, P3])
        curves_pos.append(control_points)
        BezierCurve(control_points).draw()
        P0 = P3
    plt.waitforbuttonpress()
    return np.asarray(curves_pos)

if __name__ == '__main__':
    plt.axis([-10, 10, -10, 10])
    print(bezierdraw(3))
    
