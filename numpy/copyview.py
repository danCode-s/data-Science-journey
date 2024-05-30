import numpy as np

arr = np.array([1, 5, 6, 2])
x = arr.copy() #doesnt own the data

arr[0] = 44

print(arr)
print(x)

arr_1 = np.array([43, 6, 6, 7, 1])

y = arr_1.view() #owns the data and changes to it changes the original array

y[0] = 49

print(arr_1)
print(y)

# if array owns the data, the data is printed
print(x.base)
print(y.base)