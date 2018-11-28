import numpy as np
import random

class Random_To_Sorted(object):

    def __init__(self):
        self.values = np.empty((0,10), np.uint8)
        for i in range(10):
            self.values = np.append(self.values, [np.full((10), i, np.uint8)], axis=0)

    def swap_axes(self):
        self.values = np.swapaxes(self.values, 0, 1)

    def current_values(self):
        return self.values

rTS = Random_To_Sorted()

print("\nInitial Values")
print(rTS.current_values())

rTS.swap_axes()
print("\nSwapped Values")
print(rTS.current_values())

