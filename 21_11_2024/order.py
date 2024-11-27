import numpy as np


def order(array, axis=-1):
    array.sort(axis=axis)


matrix = np.array(
    [[[20, 7, 38, 50],
      [34, 15, 12, 50]],
     [[46, 10, 38, 31],
      [5, 6, 32, 38]],
     [[36, 39, 36, 0],
      [1, 29, 36, 11]]])
print(order(matrix, 1))
print(matrix)