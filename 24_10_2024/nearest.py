import numpy as np


def nearest(matrix, value):
    differences = np.abs(matrix - value)
    index = np.unravel_index(np.argmin(differences), matrix.shape)
    return tuple(int(i) for i in index)


matrix = np.array([[1, 2, 3],
                   [4, -6, 2],
                   [5, 3, 1],
                   [1, -5, -3]])

print(nearest(matrix, -4))
print(matrix[nearest(matrix, -4)])