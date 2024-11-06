import numpy as np


n = int(input())
arr = np.eye(n) * [i for i in range(1, n + 1)]
print(arr)
