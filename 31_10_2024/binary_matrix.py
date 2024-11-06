import numpy as np


def binary(n):
    count = 2 ** n

    arr = np.zeros((count, n), dtype=int)

    for i in range(count):
        binary_num = np.array(list(map(int, f'{i:0{n}b}')))
        arr[i] = binary_num

    return arr


matrix = binary(9)
print(f'matrix type = {matrix.dtype}')
print(f'matrix shape = {matrix.shape}')