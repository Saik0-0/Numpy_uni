import numpy as np


def positive_sum(arr):
    arr[arr <= 0] *= 0
    return np.sum(arr)
