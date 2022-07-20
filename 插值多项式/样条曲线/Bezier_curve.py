import sympy as sp
import numpy as np
import matplotlib.pyplot as plt


class BezierCurve(object):
    
    def __init__(self, points): # 4个点:P0,P1,P2,P3
        
        self.points = np.asarray(points)
        self.X = self.points[..., 0]; self.Y = self.points[..., 1]
        
        
    def draw(self, color = 'blue', num = 50):
        
        t_data = np.linspace(0, 1, num)
        x_data = ((1 - t_data)**3 * self.X[0] +
                  3 * (1 - t_data)**2 * t_data * self.X[1] +
                  3 * (1 - t_data) * t_data ** 2 * self.X[2] +
                  t_data**3 * self.X[3])
        y_data = ((1 - t_data)**3 * self.Y[0] +
                  3 * (1 - t_data)**2 * t_data * self.Y[1] +
                  3 * (1 - t_data) * t_data ** 2 * self.Y[2] +
                  t_data**3 * self.Y[3])
        plt.plot(x_data, y_data, color = color)
        
        
if __name__ == '__main__':
    bc = BezierCurve([[1,1], [1,3], [3,3], [2,2]])
    bc.draw()
    
    plt.show()
