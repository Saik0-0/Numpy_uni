import numpy as np


def for_three(arr):
    if arr.shape[0] % 3 == 0:
        return np.array_split(arr, 3, axis=0)
    return np.array_split(arr, 3, axis=1)


matrix = np.array([[1, 2, 3, 4, 5, 6],
                   [7, 8, 9, 0, 1, 2],
                   [3, 4, 5, 6, 7, 8],
                   [9, 0, 1, 2, 3, 4]])
a, b, c = for_three(matrix)
print(a, b, c, sep='\n')