import numpy as np


def manhattan(rows, cols, vector):
    rows_ind = np.arange(rows).reshape(-1, 1)
    columns_ind = np.arange(cols).reshape(1, -1)
    return np.abs(rows_ind - vector[0]) * 1.0 + np.abs(columns_ind - vector[1])


def neumann(arr, vect, r):
    rows, columns = arr.shape
    x, y = vect

    return np.sum(arr[manhattan(rows, columns, (x, y)) <= r])


matrix = np.array([[1, 2, 3, 4],
                   [4, 3, 2, 5],
                   [1, 6, 5, 2],
                   [7, 3, 2, 1]])
print(neumann(matrix, np.array((1, 2)), 1))


