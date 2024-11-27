import numpy as np
from math import gcd
from numpy import vectorize


def equal(tools, players):
    return vectorize(gcd)(tools, players)


matrix = np.array([[2, 30, 336, 99, 165, 110],
                   [33, 44, 3234, 9317, 1815, 112],
                   [144, 60, 26, 1960, 1820, 220]])
gamers = np.array([27, 33, 22, 99, 21, 121])
print(equal(matrix, gamers))