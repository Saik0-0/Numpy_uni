import numpy as np


def only_largest(arr1, arr2):
    return np.maximum(arr1, arr2)


matrix = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 0, 1, 2]])
matrix1 = np.array([[5, 1, 3, 7],
                    [2, 4, 9, 6],
                    [0, 1, 7, 4]])
print(only_largest(matrix, matrix1))