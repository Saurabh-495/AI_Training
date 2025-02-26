import numpy as np

a = np.array([1, 2, 3, 4, 5], dtype='i1')
print("Data type of array", a.dtype)

a = np.array([1, 2, 3, 4, 5], dtype = 'i2')
print("Data type of array", a.dtype)
a = np.array([1, 2, 3, 4, 5], dtype = 'S')
print("Data type of array", a.dtype)
a = np.array([1, 2, 3, 4, 5], dtype = 'f')

print("Data type of array", a.dtype)

arr = np.array([0,1, 2, 3,4, 5])
arr = arr.astype("i")
arr = arr.astype(bool)


print(arr.dtype)
print(arr)




arr1 = np.array([1, 2, 3], dtype='i1')  # int8
arr2 = np.array([1000, 2000, 3000], dtype='i2')  # int16

print(arr1, arr1.dtype)  # Output: [1 2 3] int8
print(arr2, arr2.dtype)  # Output: [1000 2000 3000] int16


f1 = np.array([2.4, 3.6, 4.8, 5])
print("Data type of array", f1.dtype)
# f1 = f1.astype("i2")
f1 = f1.astype("S") #When converting a floating-point (f) NumPy array to a string (S) using .astype(), you may notice a b prefix before the values. This happens because NumPy converts it to a byte string (S type represents byte strings, not Unicode strings).

print(f1)
print("Data type of array", f1.dtype)