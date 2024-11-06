import numpy as np


def strings(vect1, vect2):
    cos = np.dot(vect1, vect2) / (np.linalg.norm(vect1) * np.linalg.norm(vect2))
    angle = np.arccos(cos)
    return np.degrees(angle)


m1 = np.array([1, 0])
m2 = np.array([1, 1])
print(strings(m1, m2))