import numpy as np

n, a, b = map(int, input().split())
arr = np.linspace(a, b, n).reshape((3, n // 3))
print(arr)
