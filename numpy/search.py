import numpy as np

arr_0 = np.array([1, 2, 3, 4, 65, 3, 6 , 4, 6, 4])

x = np.where(arr_0 == 4)
y = np.where(arr_0 % 2 == 0)


print(x)
print(y)

# Search Sorted

arr_1 = np.array([6, 7, 8, 9])
z = np.searchsorted(arr_1, 7)
g = np.searchsorted(arr_1, 7, side="right")

print(z)
print(g)

arr_2 = np.array([1, 3, 5, 6])
j = np.searchsorted(arr_2, [2, 4, 6])
print(j)

