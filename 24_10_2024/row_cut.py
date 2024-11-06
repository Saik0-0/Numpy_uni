import numpy as np


input_arr = []
while True:
    line = input()
    if len(line.split()) == 2:
        n, m = map(int, line.split())
        break
    input_arr.append(list(map(int, line.split())))

arr = np.array(input_arr)[:, n:m]
print(arr)
