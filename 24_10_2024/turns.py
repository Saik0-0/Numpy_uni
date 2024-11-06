import numpy as np


def turns(arr, n):
    if n == 0:
        return arr
    if n > 0:
        return turns(np.rot90(arr), n - 1)
    else:
        return turns(np.rot90(arr, -1), n + 1)


matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(turns(matrix, 1))
print(turns(matrix, -1))