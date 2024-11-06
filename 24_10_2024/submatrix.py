import numpy as np


# matrix = np.array([[1, 2, 3, 4],
#                    [4, 3, 2, 1],
#                    [5, 6, 7, 8]])


def sub_matrix(arr, n, m):
    if arr.ndim == 1:
        return arr[n:m]
    elif arr.ndim == 2:
        return arr[n:m, n:m]
    return arr[n:m, n:m, n:m]


# print(sub_matrix(matrix, 1, 3))