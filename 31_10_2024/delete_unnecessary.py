import numpy as np


def remove_triples(arr):
    return np.delete(arr, np.argwhere(arr % 3 == 0)[:, 0], axis=0)


matrix = np.array([[1, 2, 5, 4],
                   [5, 6, 7, 8],
                   [8, 7, 6, 5],
                   [4, 7, 2, 1]])
print(remove_triples(matrix))