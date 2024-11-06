import numpy as np


def normalize(arr):
    return np.array([arr[i] - np.average(arr[i]) for i in range(np.shape(arr)[0])])


matrix = np.array([[1, 2, 3],
                   [4, 6, 2],
                   [5, 3, 1],
                   [1, 6, 2]], dtype=float)
print(matrix)
print(normalize(matrix))
print(matrix)