import numpy as np

arr0 = np.array([10, 11, 12, 13, 14, 15])
arr1 = np.array([20, 21, 22, 23, 24, 25])
arr2 = np.array([10, 20, 30, 40, 50, 60])
arr3 = np.array([3, 5, 10, 8, 2, 33])
arr4 = np.array([-1, -2, 1, 2, 3, -4])


x = np.add(arr0, arr1)
print(x)

y = np.subtract(arr1, arr0)
print(y)

z = np.multiply(arr2, arr1)
print(z)

j = np.divide(arr2, arr3)
print(j)

h = np.power(arr2, arr3)
print(h)

# both the mod() and remainder() can be used to get remainder
k = np.mod(arr2, arr3)
print(k)

# divmod returns both the quotiend and the mod
l = np.divmod(arr2, arr3)
print(l)

# absolute() and abs() can be used to get absolute, absolute() is preffered
m = np.absolute(arr4)
print(m)