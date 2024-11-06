import numpy as np


def inverse(arr1, arr2):
    return arr1.round().all() == np.linalg.inv(arr2).round().all()


matrix = np.array([[1, 2, 3],
                   [2, 3, 4],
                   [3, 4, -5]])
matrix1 = np.array([[-3.1, 2.2, -0.1],
                    [2.2, -1.4, 0.2],
                    [-0.1, 0.2, -0.1]])
print(inverse(matrix, matrix1))