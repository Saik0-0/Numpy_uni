import numpy as np


length = int(input())
arr = np.ones((length, length))
arr[0:length:length - 1] = 10
arr[:, 0:length:length - 1] = 10
print(arr)
