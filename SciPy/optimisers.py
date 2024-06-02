from scipy.optimize import root 
from math import cos

def eqn(x):
    return x + cos(x)

myroot = root(eqn, 0)

# print(myroot)

# minimize a Function

from scipy.optimize import minimize

def eqn_1(x):
    return x**2 + x + 2

mymin = minimize(eqn_1, 0, method="BFGS")
print(mymin)