import numpy as np


class Megalith:
    def __init__(self, array):
        self.array = np.array(array)

    def middle(self):
        return self.array[len(self.array) // 2]

    def lowest(self):
        return np.min(self.array)

    def highest(self):
        return np.max(self.array)

    def median(self):
        return np.sort(self.array)[len(self.array) // 2]


data = [1, 2, 3, 5, 1, 7, 9]
ml = Megalith(data)
print(ml.middle())
print(ml.lowest())
print(ml.highest())
print(ml.median())
