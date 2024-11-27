import numpy as np


def deviation(array):
    mean = np.mean(array)
    std_dev = np.std(array)
    filtered = array[(array >= mean - std_dev) & (array <= mean + std_dev)]
    return filtered.flatten()


matrix = np.array([[106, 40, 104, -23, 59, 101, 2],
                   [5, -48, 25, 94, -89, 70, 34],
                   [162, 60, 47, -22, 108, -82, -3],
                   [14, -68, 153, 197, 93, -3, 70],
                   [-46, -40, 3, 192, 6, 90, 96]])
print(deviation(matrix))