import numpy as np


def paradox(vect1, vect2):
    dist = np.arange(1, len(vect1) + 1)
    m_calc = (vect1 ** 2) * dist / 2
    m_measure = (vect2 ** 2) * dist / 2

    return m_measure - m_calc


m1 = np.array([47, 48, 50, 53, 54, 55, 55, 54, 52, 49, 47])
m2 = np.array([48, 53, 62, 78, 81, 88, 92, 97, 99, 102, 110])
print(paradox(m1, m2))