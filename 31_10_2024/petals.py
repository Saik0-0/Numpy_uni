import sys

import numpy as np


strings = sys.stdin.read().strip().splitlines()

flowers = np.array([np.fromstring(string, dtype=int, sep=' ') for string in strings[:-1]])
count = np.fromstring(strings[-1], dtype=int, sep=' ')

if np.linalg.matrix_rank(flowers) >= min(count.shape):
    solution = np.linalg.solve(flowers, count)
else:
    solution = []

print(solution)
