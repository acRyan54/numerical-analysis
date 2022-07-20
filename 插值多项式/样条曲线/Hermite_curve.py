import sympy as sp
import numpy as np
import matplotlib.pyplot as plt


class HermiteCurve(object):
    
    def __init__(self, points): # 4个点:P1,P2,T1,T2
        
        self.points = np.asarray(points)
        self.X = self.points[..., 0]; self.Y = self.points[..., 1]
        
        
    def draw(self, color = 'blue', num = 50):
        
        t_data = np.linspace(0, 1, num)
        x_data = ((1 - 3 * t_data**2 + 2 * t_data**3) * self.X[0] +
                  t_data**2 * (3 - 2 * t_data) * self.X[1] +
                  t_data * (t_data - 1)**2 * self.X[2] +
                  t_data**2 * (t_data - 1) * self.X[3])
        y_data = ((1 - 3 * t_data**2 + 2 * t_data**3) * self.Y[0] +
                  t_data**2 * (3 - 2 * t_data) * self.Y[1] +
                  t_data * (t_data - 1)**2 * self.Y[2] +
                  t_data**2 * (t_data - 1) * self.Y[3])
        plt.plot(x_data, y_data, color = color)
        
        
if __name__ == '__main__':
    hc = HermiteCurve([[1,1], [1,3], [3,3], [2,2]])
    hc.draw()
    
    plt.show()
