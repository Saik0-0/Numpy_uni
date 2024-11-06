import numpy as np


def alternate(n, *args):
    num_elements = len(args)
    indices = (np.arange(n)[:, None] + np.arange(n)) % num_elements
    matrix = np.array(args)[indices]
    return matrix
