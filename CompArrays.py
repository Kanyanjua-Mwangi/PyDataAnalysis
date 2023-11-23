
import numpy as np
np.random.seed(0)

def compute_reciprocals(values):
    output = np.empty(len(values))
    for i in range(len(values)):
        output[i] = 1.0 / values[i]
    return output
        
values = np.random.randint(1, 10, size=5)

compute_reciprocals(values)

big_array = np.random.randint(1, 100, size=1000000)
#%timeit compute_reciprocals(big_array)

print(compute_reciprocals(values))
print(1.0 / values)

print(np.arange(5) / np.arange(1, 6))

x = np.arange(27).reshape((3, 3, 3))
print(2 ** x)

#Ufuncs utilise native py arithmetic operators
print("x     =", x)
print("x + 5 =", x + 5)
print("x - 5 =", x - 5)
print("x * 2 =", x * 2)
print("x / 2 =", x / 2)
print("x // 2 =", x // 2)

print("-x     = ", -x)
print("x ** 2 = ", x ** 2)
print("x % 2  = ", x % 2)

#operators can be strung together.
print(-(0.5*x + 1) ** 2)
print((3.3*-x % 4) ** -0.05)

#arithmetic operations are convenient wrappers around specific functions built into NumPy
print(np.add(x, 2))

#Numpy understands python's built in absolute value function.
print(abs(x))

#Trigonometric functions
#an array of angles
theta = np.linspace(0, np.pi, 3)
print(theta)

#Trigonometric functions.
print("theta      = ", theta)
print("sin(theta) = ", np.sin(theta))
print("cos(theta) = ", np.cos(theta))
print("tan(theta) = ", np.tan(theta))

#Inverse Trigonometric functions
print("arcsin(theta) = ", np.arcsin(theta))
print("arccos(theta) = ", np.arccos(theta))
print("arctan(theta) = ", np.arctan(theta))

#Exponential and Logarithms
Ex = [1, 2, 3]
print("Ex     =", Ex)
print("e^Ex   =", np.exp(Ex))
print("2^Ex   =", np.exp2(Ex))
print("3^Ex   =", np.power(3, Ex))

print("ln(Ex)    =", np.log(Ex))
print("log2(Ex)  =", np.log2(Ex))
print("log10(Ex) =", np.log10(Ex))

#For very small input we use:
x = [0, 0.001, 0.01, 0.1]
print("exp(x) - 1 =", np.expm1(x))
print("log(1 + x) =", np.log1p(x))

#Specialized Ufuncs
from scipy import special

# Gamma functions (generalized factorials) and related functions
m = [1, 5, 10]
print("gamma(m)     =", special.gamma(m))
print("ln|gamma(m)| =", special.gammaln(m))
print("beta(m, 2)   =", special.beta(m, 2))

#Specifying output.
k = np.arange(5)
l = np.empty(5)
np.multiply(k, 10, out=l)
print(l)

n = np.zeros(10)
np.power(2, k, out=n[::2])
print(n)