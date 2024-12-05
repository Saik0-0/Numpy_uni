import numpy as np


def correlation(data1, data2):
    correlation_matrix = np.zeros((data1.shape[0], data1.shape[0]))

    # Вычисление коэффициентов корреляции
    for i in range(data1.shape[0]):
        for j in range(data1.shape[0]):
            correlation_matrix[i, j] = np.corrcoef(data1[i, :], data2[j, :])[0, 1]

    return np.round(correlation_matrix, 2)


data1 = np.array([[106, 40, 104, -23, 59, 101, 2],
                  [5, -48, 25, 94, -89, 70, 34],
                  [162, 60, 47, -22, 108, -82, -3],
                  [14, -68, 153, 197, 93, -3, 70]])

data2 = np.array([[128, 172, 60, 155, -30, -2, 112],
                  [63, 45, -94, 29, -48, 88, 5],
                  [143, 45, 84, -46, 11, 193, 106],
                  [36, -79, 37, 115, -86, 15, 193]])

print(correlation(data1, data2))
