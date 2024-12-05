import numpy as np


class Cabbage:
    def __init__(self, upper_leaf, step, size):
        self.upper_leaf = upper_leaf
        self.leafs = np.arange(upper_leaf)
        self.step = step
        self.size = size

    def leaf(self):
        if self.upper_leaf - self.step > self.size:
            print(self.leafs[self.upper_leaf - self.step])
            self.upper_leaf -= self.step
        else:
            print(self.size)


cb = Cabbage(10, 3, 2)
cb.leaf()
cb.leaf()
cb.leaf()
cb.leaf()