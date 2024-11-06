import numpy as np


def step_vectors(vect1, vect2):
    return np.sum(np.diag(np.outer(vect1, vect2)))

