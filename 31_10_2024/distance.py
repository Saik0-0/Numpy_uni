import numpy as np


def distance(file1, file2):
    arr1 = np.load(file1)
    arr2 = np.load(file2)
    return np.linalg.norm(arr1 - arr2)
