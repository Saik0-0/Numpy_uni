import numpy as np


def box(arr, n):
    new_arr_shape = (arr.shape[0] + 2, arr.shape[1] + 2)
    new_arr = np.zeros(new_arr_shape, dtype=int)
    new_arr[1:-1, 1:-1] = arr
    new_arr[0:len(new_arr):len(new_arr) - 1] = n
    new_arr[:, 0:len(new_arr[0]):len(new_arr[0]) - 1] = n
    return new_arr


matrix = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(matrix)
print(box(matrix, 3))