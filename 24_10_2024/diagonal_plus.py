import numpy as np


def diagonal_plus(arr):
    max_arr = int(np.max(arr))
    min_arr = int(np.min(arr))
    arr_for_add = np.eye(len(arr)) * (max_arr - min_arr)
    return (arr + arr_for_add).astype(int)
