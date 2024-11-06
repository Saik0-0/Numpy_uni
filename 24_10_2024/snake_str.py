import numpy as np


a, b, n, m = map(int, input().split())
arr = np.arange(a, b).reshape(n, m)
arr[1::2] = arr[1::2][:, ::-1]
# транспонировали для столбцов
print(np.transpose(arr))
