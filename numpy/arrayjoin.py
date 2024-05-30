import numpy as np

arr_0 = np.array([1, 2, 3, 5, 6])
arr_1 = np.array([5, 1, 6, 1, 7])

arr_2 = np.array([[2, 9], [8, 2]])
arr_3 = np.array([[1, 3], [5, 8]])


arr = np.concatenate((arr_0, arr_1))
arr1 = np.concatenate((arr_2, arr_3), axis=1)

print(arr)
print(f"\n{arr1}")

# Using the Stack function

arr2 = np.stack((arr_0, arr_1), axis=1)
print(arr2)

#stack along rows

arr3 = np.hstack((arr_0, arr_1))
print(arr3)

#stack along columns
arr4 = np.vstack((arr_0, arr_1))
print(arr4)

# Stack along height(DEPTH)

arr5 = np.dstack((arr_0, arr_1))
print(arr5)