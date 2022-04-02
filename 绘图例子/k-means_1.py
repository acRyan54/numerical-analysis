# k-means算法非凸的一个反例

import numpy as np
import matplotlib.pyplot as plt

def np_max(x, y):
    return (x+y+np.fabs(x-y))/2
def np_min(x, y):
    return (x+y-np.fabs(x-y))/2
def func(x, y):
    return np_min((x-1)**2+(y-1)**2,  (x+1)**2+(y+1)**2)

x = np.arange(-2, 2, 0.1)
y = np.arange(-2, 2, 0.1)
X, Y = np.meshgrid(x, y)
Z = func(X, Y)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap = 'coolwarm')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()