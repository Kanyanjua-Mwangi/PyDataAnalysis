
import numpy as np
import array
print('Hello World')

L = list(range(10))
A = array.array('i', L)

print(L)
print(A)

Q = np.array([1, 4, 2, 5, 3, 3.14], dtype='float32')
print(Q)

# nested lists result in multi-dimensional arrays
W = np.array([range(i, i + 3) for i in [2, 4, 6]])
print(W)

# Create a length-10 integer array filled with zeros
E = np.ones(10, dtype=int)
print(E)

# Create a 3x5 floating-point array filled with ones
R = np.ones((3, 5), dtype=float)
print(R)

# Create a 3x5 array filled with 3.14
T = np.full((3, 5), 3.14)
print(T)

# Create an array filled with a linear sequence
Y = np.arange(0, 20, 2)
print(Y)

#Create an array of five values evenly spaced
U = np.linspace(0, 50, 9)
print(U)

# Create a 5x7 array of uniformly distributed random values
I = np.random.random((5, 7))
print(I)

# Create a 3x3 array of normally distributed random values
# with mean 0 and standard deviation 1
O = np.random.normal(0, 1, (3, 3))
print(O)

# Create a 3x3 array of random integers in the interval [0, 10)
P = np.random.randint(0, 10, (3, 3))
print(P)

# Create a 3x3 identity matrix
A = np.eye(3)
print (A)

np.random.seed(0)  # seed for reproducibility

x1 = np.random.randint(10, size=6)  # One-dimensional array
x2 = np.random.randint(10, size=(3, 4))  # Two-dimensional array
x3 = np.random.randint(10, size=(3, 4, 5))  # Three-dimensional array

print(x1)
print(x2)
print(x3)

print("x1 ndim: ", x1.ndim)
print("x1 shape:", x1.shape)
print("x1 size: ", x1.size)
print("x1 type: ", x1.dtype)
print("x1 itemsize: ", x1.itemsize, 'bytes')
print("x1 nbytes:", x1.nbytes, "bytes")

print("x2 ndim: ", x2.ndim)
print("x2 shape:", x2.shape)
print("x2 size: ", x2.size)
print("x2 type: ", x2.dtype)
print("x2 itemsize: ", x2.itemsize, 'bytes')
print("x2 nbytes:", x2.nbytes, "bytes")


print("x3 ndim: ", x3.ndim)
print("x3 shape:", x3.shape)
print("x3 size: ", x3.size)
print("x3 type: ", x3.dtype)
print("x3 itemsize: ", x3.itemsize, 'bytes')
print("x3 nbytes:", x3.nbytes, "bytes")

print(x1[-1])
print(x2[2, 3])

x3[0,1,2] = 12

print(x3[0,1,2])

print(x1[::-1])
print(x2[0:0, 1:1])
print(x2[0,: ])

x3_sub = x3[:2, :2, :2]

print(x3_sub)

x3_sub[1, 1, 1] = 33
print(x3_sub)
print(x3)

x3_sub_copy = x3[:1, :1, :1].copy()
print(x3_sub_copy)

grid = np.arange(1, 10).reshape((3, 3))
print(grid)

print(x2.reshape(6, 2))
print(x2[np.newaxis, :])

x = np.array([1, 2, 3])
y = np.array([3, 2, 1])
z = [99, 99, 99]

#print(np.concatenate([x, y, z]))

x22 = np.concatenate([x2, x2], axis = 1)
#print(x22)

#print(np.vstack[x2, x2])

x4, x5, x6 = np.split(x,[2,4] )
#print(x4, x5, x6)

0 * np.nan
np.nan == np.nan
np.inf > np.nan
np.nan - np.nan
np.nan in set([np.nan])
0.3 == 3 * 0.1