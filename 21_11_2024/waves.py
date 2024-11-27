import numpy as np


def waves(x_cort, phi_cort):
    x_values = np.arange(x_cort[0], x_cort[1] + 1, 1)

    phi_values = np.radians(np.arange(phi_cort[0], phi_cort[1] + 0.5, 0.5))

    y_values = np.zeros((len(phi_values), len(x_values)))

    for i, phi in enumerate(phi_values):
        y_values[i, :] = 10 * np.cos(0.072 * x_values + phi) + 15

    return y_values


# Пример использования
result = waves((-5, 5), (0, 4))
print(result)
