import numpy as np
from numpy import random

arr_0 = np.array([1, 2, 3, 4])

#this changes the original array
random.shuffle(arr_0)
print(arr_0)

# Returns a New Array
x = random.permutation(arr_0)

print(x)
