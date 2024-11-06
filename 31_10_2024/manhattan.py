import numpy as np


def manhattan(rows, cols, vector):
    rows_ind = np.arange(rows).reshape(-1, 1)
    columns_ind = np.arange(cols).reshape(1, -1)
    return np.abs(rows_ind - vector[0]) * 1.0 + np.abs(columns_ind - vector[1])


print(manhattan(5, 4, np.array((1, 2))))