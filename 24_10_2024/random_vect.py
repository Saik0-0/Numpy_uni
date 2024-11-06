import numpy as np


length = int(input())
arr = np.random.randint(1, 200, length) / 10
arr = np.floor(arr)
print(arr)
print(np.sort(arr))
