import numpy as np


def coding(array):
    if len(array) == 0:
        return np.array([]).reshape(0, 2)

    change_indices = np.where(np.diff(array) != 0)[0] + 1
    encoded = []
    start_ind = 0

    for end_ind in change_indices:
        encoded.append([array[start_ind], end_ind - start_ind])
        start_ind = end_ind

    encoded.append([array[start_ind], len(array) - start_ind])

    return np.array(encoded)


# Пример
matrix = np.array([1, 2, 2, 2, 2, 1, 1, 5, 2, 1, 1, 4, 3, 3, 3, 5, 5])
print(coding(matrix))
