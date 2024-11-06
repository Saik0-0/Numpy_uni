import math
import numpy as np


size = list(map(int, input().split()))
arr = np.resize(np.array([i for i in range(1, math.prod(size) + 1)]), (size))

print(arr)
