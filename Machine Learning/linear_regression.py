'''
Regression
The term regression is used when you try to find the relationship between variables.

In Machine Learning, and in statistical modeling, that relationship is used to predict the outcome of future events.

Linear Regression
Linear regression uses the relationship between the data-points to draw a straight line through all them.

This line can be used to predict future values.

How Does it Work?
Python has methods for finding a relationship between data-points and to draw a line of linear regression. We will show you how to use these methods instead of going through the mathematic formula.

In the example below, the x-axis represents age, and the y-axis represents speed. We have registered the age and speed of 13 cars as they were passing a tollbooth. Let us see if the data we collected could be used in a linear regression:
'''

import matplotlib.pyplot as plt
from scipy import stats

# x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
# y = [99,86,87,88,111,86,103,87,94,78,77,85,86]
# 
# slope, intercept, r, p, std_err = stats.linregress(x, y)
# def myfunc(x):
#     return slope * x + intercept
# 
# mymodel = list(map(myfunc, x))
# 
# 
# 
# plt.scatter(x, y)
# plt.plot(x, mymodel, c='r')
# plt.show()


# predict future values 
# speed = myfunc(10)
# 
# print(speed)
# 
# BAD FIT

x = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
y = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
    return slope * x + intercept


mymodel = list(map(myfunc, x))

print(r)

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()

# Low 'r' shows there is bad relation b/w the data
# it is not suitable for linear regression
