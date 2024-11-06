import numpy as np


def solve(arr):
    return np.sin(arr / 5) * np.exp(arr / 10) + 5 * np.exp(arr / -2)


print(solve(x))