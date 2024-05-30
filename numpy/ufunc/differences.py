import numpy as np

arr1 = np.array([10, 15, 25, 5])

arr2 = np.diff(arr1)
print(arr2)

# discrete difference 'n' number of time
arr3 = np.diff(arr1, n=2)
print(arr3)