import math
import numpy as np


def prod_diag(arr, main=1):
    if main:
        return math.prod(np.diag(arr))
    return math.prod(np.diag(arr[::-1]))
