import numpy as np


def largest(arr, n):
    return np.sort(arr, None)[::-1][:n]


matrix = np.array([[1, 2, 3],
                   [4, -6, 2],
                   [5, 3, 1],
                   [1, -5, -3]])
print(largest(matrix, 4))