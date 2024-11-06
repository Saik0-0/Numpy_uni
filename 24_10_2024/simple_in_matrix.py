import numpy as np


def is_not_prime(num):
    if num <= 1:
        return True
    if num <= 3:
        return False
    if num % 2 == 0 or num % 3 == 0:
        return True
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return True
        i += 6
    return False


vectorized_is_not_prime = np.vectorize(is_not_prime)
n, m, a = map(int, input().split())
arr = np.resize(np.array([i for i in range(a, a + n * m + 1)]), (n, m))
mask = (vectorized_is_not_prime(arr))
arr[mask] *= 0
print(arr)
