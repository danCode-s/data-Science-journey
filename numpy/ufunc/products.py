import numpy as np

arr1 = np.array([1, 2, 3, 4])
arr2 = np.prod(arr1)

arr3 = np.array([5, 6, 7, 8])
arr4 = np.prod([arr1, arr3])

arr5 = np.prod([arr1, arr3], axis=1)

# cumulative product
arr6 = np.cumprod(arr3)

print(arr2)
print(arr4)
print(arr5)
print(arr6)
