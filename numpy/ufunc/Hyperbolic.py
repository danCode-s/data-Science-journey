import numpy as np 

a1 = np.sinh(np.pi/2)

print(a1)

y = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
x = np.cosh(y)

print(x)

'''
Finding Angles
Finding angles from values of hyperbolic sine, cos, tan. E.g. sinh, cosh and tanh inverse (arcsinh, arccosh, arctanh).

Numpy provides ufuncs arcsinh(), arccosh() and arctanh() that produce radian values for corresponding sinh, cosh and tanh values given.

'''

print(np.arcsinh(1.0))

a2 = np.array([0.1, 0.2, 0.5])

print(np.arctanh(a2))
