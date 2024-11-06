import numpy as np


def vector_length(arr):
    sum_arr = np.sum(arr ** 2)
    return np.sqrt(sum_arr)
