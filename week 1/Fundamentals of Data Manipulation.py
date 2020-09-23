import numpy as np
from PIL import Image

a = np.array([1, 2, 3])
print(a)
print(a.ndim)
print(a.shape)

b = np.array([[1, 2, 3], [4, 5, 6]])
print(b)
print(b.ndim)
print(b.shape)
print(b.dtype)

d = np.zeros((2, 3))
print(d)

d = np.ones((2, 3))
print(d)

d = np.random.random((2, 3))
print(d)

f = np.arange(10, 50, 2)
print(f)

f = np.linspace(1, 2, 4)
print(f)

a = np.array([10, 20, 30, 40])
b = np.array([1, 2, 3, 4])
print(a - b)
print(a * b)

fahrenheit = np.array([0, -10, -15, -5])
celsius = (fahrenheit - 32) * 5 / 9
print(celsius)
t = type(1J)
print(t)

A = np.array([
    [1, 1],
    [0, 1]])
B = np.array([
    [2, 0],
    [3, 4]])
print(A * B)
print(A @ B)

img = Image.open('gray.jpeg')
# img.show()
array = np.array(img)
print(array.dtype)
print(array.shape)

mask = np.full(array.shape, 255)
print(mask)

modified_array = array - mask
modified_array *= -1
modified_array = modified_array.astype(np.uint8)
