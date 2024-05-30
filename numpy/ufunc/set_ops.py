import numpy as np


# Convert numpy array into set 

arr1 = np.array([1, 1, 2, 3, 4, 5, 5, 6, 7])



ax = np.unique(arr1)

print(ax)

# Union

arr2 = np.array([1, 2, 3, 4, 4])
arr3 = np.array([4, 3, 5, 6, 7])

print(np.union1d(arr2, arr3))

# Intersection
# assume_unique = True when working with sets

print(np.intersect1d(arr2, arr3, assume_unique=True))

# Symmetric Differenc

print(np.setxor1d(arr2, arr3, assume_unique=True))


arr = np.array([1,2,3,4,5,6,7])
print(arr[3:])
print(arr.shape)