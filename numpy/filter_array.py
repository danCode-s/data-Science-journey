import numpy as np

arr_0 = np.array([41, 42, 43, 45])

x = [True, False, True, False]

newarr_0 = arr_0[x]

print(newarr_0)

# Create a filter array that will return only values higher than 42:
filter_arr = []

for element in arr_0:
    if element > 42:
        filter_arr.append(True)
    else: 
        filter_arr.append(False)

newarr_1 = arr_0[filter_arr]

print(newarr_1)

## Easier Way Provided by NumPy

filter_arr_1 = arr_0 > 42

newarr_2 = arr_0[filter_arr]
print(newarr_2)