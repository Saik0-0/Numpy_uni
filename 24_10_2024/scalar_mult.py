import numpy as np


def scalar(arr1, arr2):
    try:
        return True, arr1.dot(arr2)
    except Exception:
        return False, np.array([])
