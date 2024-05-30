import numpy as np

arr = np.array([1, 2, 5, 6, 4, 1, 3, 9, 1, 9, 3, 7])

# 1D to 2D

newarr = arr.reshape(4, 3)
print(newarr)


# 1D to 3D

newarr_1 = arr.reshape(2, 3, 2)
print(newarr_1)

print(f"\n{arr.reshape(4, 3).base}")

# unknown dimensions
newarr_2 = arr.reshape(2, 2, -1)
print(newarr_2)

# flattening - multidimensional into 1D
arr_1 = np.array([[1,23, 53, 1]])
newarr_3 = arr_1.reshape(-1)
print(newarr_3)

