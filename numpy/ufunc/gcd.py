import numpy as np

x, y = 6, 9

z = np.gcd(x, y)

print(z)

# GCD of arrays

arr0 = np.array([20, 8, 32, 36, 16])
g = np.gcd.reduce(arr0)


print(g)
