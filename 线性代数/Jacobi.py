# Jacobi迭代法

import numpy as np

def jacobi(a, b, epoch):
    n = len(b)
    d = np.diag(a)
    r = a - np.diag(d)
    x = np.zeros((n, 1))
    for _ in range(epoch):
        x = (b - np.matmul(r, x)) / d.reshape((n, 1))
    return x

if __name__ == '__main__':
    a = np.array([3,1,-1,2,4,1,-1,2,5]).reshape((3,3))
    b = np.array([4,1,1]).reshape((3,1))
    print(jacobi(a, b, 100))
    