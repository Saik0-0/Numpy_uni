import numpy as np


def transpose(arr):
    return arr.dot(np.transpose(arr))


matrix = np.array([[4, -15, 2, 7, 1], [-19, -10, -13, 11, 17], [14, -15, 17, 20, 10], [8, -20, 20, -13, -15], [-14, -3, 0, -17, 8]])
print(transpose(matrix))