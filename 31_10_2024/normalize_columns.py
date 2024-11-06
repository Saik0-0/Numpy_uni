import numpy as np


def normalize(arr):
    return arr - arr.mean(axis=0)


matrix = np.array([[1, 2, 3],
                   [4, 5, 2],
                   [5, 4, 1],
                   [2, 6, 3]], dtype=float)
print(matrix)
print(normalize(matrix))
print(matrix)