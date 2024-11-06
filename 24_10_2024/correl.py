import math

import numpy as np


def correl(x, y):
    return sum((x[i] - np.mean(x)) * (y[i] - np.mean(y)) for i in range(len(x))) / np.sqrt(
        sum((x[i] - np.mean(x)) ** 2 for i in range(len(x))) * sum((y[i] - np.mean(y)) ** 2 for i in range(len(x))))


arr = np.array([1, 2, 3, 4, 5])
arr1 = np.array([1, 3, 3, 2, 5])
print(correl(arr, arr1))
