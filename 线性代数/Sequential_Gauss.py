# 顺序高斯消元
import numpy as np
np.set_printoptions(precision=16)


def SequentialGauss(A : np.ndarray, b, eps = .1**10): # 消去
    n = len(b)
    for j in range(n - 1):
        assert abs(A[j, j]) > eps, 'zero pivot encountered'
        for i in range(j + 1, n):
            mult = A[i, j] / A[j, j]
            A[i, j] = 0 # 可以省略，对回代无影响
            for k in range(j + 1, n):
                A[i, k] -= mult * A[j, k]
            b[i, 0] -= mult * b[j, 0]
    return A, b

def revert(A, b): # 回代
    n = len(b)
    x = np.zeros((n, 1))
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            b[i, 0] -= A[i, j] * x[j, 0]
        x[i, 0] = b[i, 0] / A[i, i]
    return x

def linsolve(A, b):
    A1, b1 = SequentialGauss(A, b)
    return revert(A1, b1)


if __name__ == '__main__':
    A = np.array([1, 2, -1, 2, 1, -2, -3, 1, 1]).reshape((3,3))
    b = np.matmul(A, np.array([10.1232421, -20, 3.111111111111]).reshape((3, 1)))
    print(np.linalg.solve(A, b))
    print(linsolve(A, b))