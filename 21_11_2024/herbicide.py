import numpy as np


def herbicide(array, weights):
    weighted_means = np.average(array, axis=1, weights=weights)
    mask = array < weighted_means[:, np.newaxis]
    selected_elements = array[mask]

    return np.median(selected_elements)


# Пример
massive = np.array([[10, 33, 46, 37, 23, 4, 26, 23],
                    [31, 31, 2, 45, 6, 8, 24, 34],
                    [29, 10, 35, 32, 11, 47, 22, 16],
                    [43, 4, 0, 46, 7, 32, 26, 26],
                    [44, 29, 11, 16, 25, 18, 21, 35]])
weights = np.array([0.1, 0.4, 0.15, 0.05, 0.1, 0.1, 0.05, 0.05])

print(herbicide(massive, weights))  # Результат: 11.0
