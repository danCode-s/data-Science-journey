import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])


arr3 = np.sum([arr1, arr2])
arr4 = np.sum([arr1, arr2], axis=1)

# cumulative Sum
arr5 = np.cumsum([arr1])


print(arr3)
print(arr4)
print(arr5)