import numpy as np
from math import log


arr0 = np.arange(1, 10)

nplog = np.frompyfunc(log, 2, 1)

print(np.log2(arr0))
print(np.log10(arr0))
print(np.log(arr0))

print(nplog(100, 15))