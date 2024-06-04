'''
Mean - The average value
Median - The mid point value, after you have sorted all the values
Mode - The most common value/ Appears most of the times

'''

import numpy as np 
from scipy import stats
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = np.mean(speed)
y = np.median(speed)
z = stats.mode(speed)




print(x)
print(y)
print(z)
