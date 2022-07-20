import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

x = sp.symbols('x')


class CubicSpline(object): # 三次样条（钳制条件）
    
    def __init__(self, X, Y, v1 = 0, vn = 0):
        
        self.n = len(X); self.X = np.asarray(X); self.Y = np.asarray(Y)
        self.derivatives = np.asarray(vn) # 记录节点处的导数
        self.A = np.zeros((self.n, self.n))
        self.B = np.zeros(self.n)
        self.dx = np.diff(self.X); self.dy = np.diff(self.Y)
        for i in range(1, self.n - 1):
            self.A[i, i - 1 : i + 2] = [self.dx[i - 1], 2*(self.dx[i - 1] + self.dx[i]), self.dx[i]]
            self.B[i] = 3 * (self.dy[i] / self.dx[i] - self.dy[i - 1] / self.dx[i - 1])
        
        '''钳制条件'''
        
        self.A[0, :2] = [2 * self.dx[0], self.dx[0]]
        self.B[0] = 3 * (self.dy[0] / self.dx[0] - v1)
        self.A[self.n - 1, -2:] = [self.dx[self.n - 2], 2 * self.dx[self.n - 2]]
        self.B[self.n - 1] = 3 * (vn - self.dy[self.n - 2] / self.dx[self.n - 2])
        
        '''计算系数矩阵'''
        
        self.coeffs = np.zeros((self.n, 4)) # coeff的列分别为a,b,c,d
        self.coeffs[..., 0] = self.Y # 系数a
        self.coeffs[..., 2] = np.linalg.solve(self.A, self.B) # 系数c
        for i in range(self.n - 1):
            self.coeffs[i, 1] = (self.dy[i] / self.dx[i] - 
                           self.dx[i] / 3 * (self.coeffs[i + 1, 2] + 2 * self.coeffs[i, 2])) # 系数b
            self.coeffs[i, 3] = (self.coeffs[i + 1, 2] - self.coeffs[i, 2]) / (3 * self.dx[i]) # 系数d
        self.coeffs = self.coeffs[:-1, ...] # 取前n-1行
        self.derivatives = np.append(self.coeffs[..., 1], self.derivatives)
        
        '''计算样条函数'''
        
        self.spline_funcs = []
        self.spline_dfuncs = []
        for i in range(self.n - 1):
            self.spline_funcs.append(self.coeffs[i][0] +
                                self.coeffs[i][1] * (x - self.X[i]) + 
                                self.coeffs[i][2] * (x - self.X[i])**2 + 
                                self.coeffs[i][3] * (x - self.X[i])**3)
            self.spline_dfuncs.append(self.spline_funcs[i].diff(x))
        
        
    def draw(self, color = 'blue', num = 100):
        
        for i in range(self.n - 1):
            x_data = np.linspace(self.X[i], self.X[i + 1], num)
            y_data = sp.lambdify(x, self.spline_funcs[i], 'numpy')(x_data)
            plt.plot(x_data, y_data, color = color)


    def cal_val(self, x_val):
        
        if x_val == self.X[0]: # 左端点特判
            return self.Y[0]
        index = self._lower_bound(self.X, x_val)
        return self.spline_funcs[index - 1].subs(x, x_val)
    
    
    def cal_derivative(self, x_val):
        
        if x_val == self.X[0]: # 左端点特判
            return self.derivatives[0]
        index = self._lower_bound(self.X, x_val)
        return self.spline_dfuncs[index - 1].subs(x, x_val)
    
    
    def _lower_bound(self, alist, target) -> int: # 返回第一个大于等于target的下标
        
        left, right = 0, len(alist) - 1
        while left <= right: 
            mid = (left + right) // 2
            if target > alist[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return left
            

if __name__ == '__main__':
    
    X1 = [1,2,5,6,7,8,10,13,17]
    Y1 = [3.0, 3.7, 3.9, 4.2, 5.7, 6.6, 7.1, 6.7, 4.5]
    # plt.scatter(X1, Y1)
    cs1 = CubicSpline(X1, Y1, 1.0, -0.67)
    cs1.draw('red')

    
    X2 = [17,20,23,24,25,27,27.7]
    Y2 = [4.5, 7.0, 6.1, 5.6, 5.8, 5.2, 4.1]
    cs2 = CubicSpline(X2, Y2, 3.0, -4.0)
    cs2.draw('green')
    
    
    X3 = [27.7, 28, 29, 30]
    Y3 = [4.1, 4.3, 4.1, 3.0]
    cs3 = CubicSpline(X3, Y3, 0.33, -1.5)
    cs3.draw('blue')
    
    plt.show()