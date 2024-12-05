import numpy as np


def fallout(array, number=10):
    array_flat = array.flatten()
    min_val = np.min(array_flat)
    max_val = np.max(array_flat)
    bins = np.linspace(min_val, max_val, number + 1)
    histogram, _ = np.histogram(array_flat, bins=bins)
    return histogram


matrix = np.array([[21, 15, 0, 39, 8, 33, 50, 0],
                   [42, 39, 12, 8, 28, 39, 23, 13],
                   [37, 0, 27, 11, 14, 19, 9, 36],
                   [41, 35, 28, 39, 15, 18, 0, 11],
                   [19, 0, 22, 16, 0, 27, 36, 48]])

print(fallout(matrix, 8))
