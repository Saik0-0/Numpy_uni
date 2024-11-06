import numpy as np


def null_adding(arr, indexes, place='row'):
    if place == 'row':
        return np.insert(arr, indexes, 0, axis=0)
    return np.insert(arr, indexes, 0, axis=1)


matrix = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [8, 7, 6, 5],
                   [4, 3, 2, 1]])
print(null_adding(matrix, [0, 3]))