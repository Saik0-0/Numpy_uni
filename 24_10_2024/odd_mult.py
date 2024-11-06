import numpy as np


def odd_mult(arr, a):
    mask = (arr < 0) & (arr % 2 != 0)
    arr[mask] *= a
    return arr
