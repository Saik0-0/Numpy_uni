import numpy as np

length = int(input())
arr = np.arange(length)
arr[0:length:3] = 0
print(arr)
