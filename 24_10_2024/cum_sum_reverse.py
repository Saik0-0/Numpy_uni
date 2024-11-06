import numpy as np


def cum_sum_reverse(matrix, axis=None):
    if axis is None:
        return np.cumsum(matrix.flatten()[::-1])[::-1]
    elif axis == 1:
        return np.cumsum(matrix[..., ::-1], axis=axis)[..., ::-1]
    elif axis == 0:
        return np.cumsum(matrix[::-1, ::-1], axis=axis)[::-1, ::-1]


matrix = np.array([[1, 2, 3, 4],
                   [4, 3, 2, 1],
                   [5, 6, 7, 8],
                   [8, 7, 6, 5]])

print(cum_sum_reverse(matrix, 0))