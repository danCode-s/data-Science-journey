import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

print(newarr)

# Split into arrays
print(newarr[0])
print(newarr[1])
print(newarr[2])

# 2D Arrays 
arr_2D = np.array([[1, 23, 5, 6], [12, 6, 2, 8], [99, 45, 6, 31]])

arr_new_2D = np.array_split(arr_2D, 3)
print(arr_new_2D)

#Split along rows 
arr_2D_1 = np.array([[1, 5, 6], [12, 6, 8], [99, 45, 31]])

arr_2D_new = np.array_split(arr_2D_1, 3, axis=1)

print(arr_2D_new)

#Same thing using hsplit()
arr_2D_new_1 = np.hsplit(arr_2D_1, 3)
print(arr_2D_new_1)
