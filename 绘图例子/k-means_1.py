import numpy as np
import matplotlib.pyplot as plt


def np_max(x, y):
    return (x+y+abs(x-y))/2
def np_min(x, y):
    return (x+y-abs(x-y))/2
def func(x, y):
    return np_min((x-1)**2+(y-1)**2,  (x+1)**2+(y+1)**2)

x = np.arange(-3, 3, 0.1)
y = np.arange(-3, 3, 0.1)
X, Y = np.meshgrid(x, y)
Z = func(X, Y)


fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap = 'rainbow')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()

'''
import sympy as sp
from sympy.plotting import plot3d
x, y = sp.symbols('x y')
expr = np_min((x-1)**2+(y-1)**2, (x+1)**2+(y+1)**2)
p1 = plot3d(expr, (x, -3, 3), (y, -3, 3), surface_color='1')
'''