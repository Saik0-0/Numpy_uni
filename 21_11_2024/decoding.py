import numpy as np


def decoding(array):
    return np.repeat(array[:, 0], array[:, 1])


matrix = np.array([[1, 1], [2, 4], [1, 2], [5, 2],
                   [2, 1], [1, 2], [4, 1], [3, 3], [5, 2]])
print(decoding(matrix))