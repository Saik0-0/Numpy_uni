import numpy as np


class JamesWebb:
    def __init__(self, stars_array):
        self.stars_array = np.array(stars_array, dtype=object)

    def brightest_star(self):
        return tuple(map(int, np.unravel_index(np.argmin(self.stars_array), self.stars_array.shape)))

    def brightest_galaxy(self):
        return tuple(map(int, np.unravel_index(np.argmax(self.stars_array), self.stars_array.shape)))

    def stars(self):
        return np.sum(self.stars_array < 0)

    def galaxies(self):
        return np.sum(self.stars_array > 0)

    def voids(self):
        return np.sum(self.stars_array == 0)


data = [[0, 0, 1, 2],
        [3, 1, -1, -1],
        [0, 3, -1, 0]]
jw = JamesWebb(data)
print(jw.brightest_star())
print(jw.brightest_galaxy())
print(jw.stars())
print(jw.galaxies())