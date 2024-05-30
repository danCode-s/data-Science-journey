import numpy as np


x = np.sin(np.pi/2)
print(x)

y = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
z = np.sin(y)

print(z)

# Degress to radians
arr1 = np.array([90, 180, 270, 360])
arr2 = np.deg2rad(arr1)

print(arr2)

#Radians to Degrees

arr3 = np.rad2deg(y)
print(arr3)

'''
Finding Angles
Finding angles from values of sine, cos, tan. E.g. sin, cos and tan inverse (arcsin, arccos, arctan).

NumPy provides ufuncs arcsin(), arccos() and arctan() that produce radian values for corresponding sin, cos and tan values given.

'''

j = np.arcsin(1.0)
print(j)

arr4 = np.array([1, -1, 0.1])
arr5 = np.arcsin(arr4)

print(arr5)


# HYPOTENUSE

base = 3
perp = 5

i = np.hypot(base, perp)

print(i)

