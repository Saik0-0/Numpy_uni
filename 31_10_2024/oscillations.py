import numpy as np


def oscillations(cort, velocity, t):
    x0, y0 = cort
    x = x0 * np.cos(velocity * np.arange(0, t, 0.1))
    y = y0 * np.sin(velocity * np.arange(0, t, 0.1))
    return np.column_stack((x, y))


print(oscillations((1, 1), 1.57, 1))