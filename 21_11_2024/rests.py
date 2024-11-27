import numpy as np


def rests(array1, array2, number=2):
    return array1 % number == array2 % number


matrix1 = np.array([[20, 29, 10, 18, 15, 12, 44],
                    [21, 34, 15, 13, 30, 14, 33],
                    [14, 7, 19, 35, 27, 40, 1]])
matrix2 = np.array([[46, 47, 44, 9, 28, 29, 41],
                    [16, 50, 18, 32, 5, 32, 38],
                    [47, 46, 16, 37, 6, 29, 16]])
print(rests(matrix1, matrix2, 3))