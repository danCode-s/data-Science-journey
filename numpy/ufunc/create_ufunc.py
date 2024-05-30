import numpy as np

def myadd(x, y):
    return x + y

myadd = np.frompyfunc(myadd, 2, 1)

print(myadd([1, 3, 6, 2], [9, 5, 1, 7]))
print(type(myadd))