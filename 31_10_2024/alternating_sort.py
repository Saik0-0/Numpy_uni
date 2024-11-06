import numpy as np


def alter_sort(arr, axis=0):
    if axis == 0:
        return np.array([np.sort(row) if i % 2 == 0 else np.sort(row)[::-1] for i, row in enumerate(arr)])
    elif axis == 1:
        return np.array([np.sort(col) if i % 2 == 0 else np.sort(col)[::-1] for i, col in enumerate(arr.T)]).T


matrix = np.array([[1, 6, 2, 5],
                   [6, 3, 9, 1],
                   [8, 1, 2, 6],
                   [3, 5, 1, 7]])
print(alter_sort(matrix, axis=1))