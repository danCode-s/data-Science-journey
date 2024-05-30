import numpy as np

x = 4
y = 6

z = np.lcm(x, y)
print(z)

# LCM in Arrays

arr0 = np.array([3, 6, 9])

arr1 = np.lcm.reduce(arr0)

print(arr1)

arr2 = np.arange(1, 11)

print(np.lcm.reduce(arr2))
