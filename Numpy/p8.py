import numpy as np

# arr = np.array([1, 2, 3, 4, 5, 6])

# newarr = np.array_split(arr, 3)

# print(newarr)

# spilit arrays in 4 parts 

# arr1 = np.array([1, 2, 3, 4, 5, 6])

# newarr1 = np.array_split(arr1, 4)

# print(newarr1)

# join


# Arr1 = np.array([1, 2, 3])

# Arr2 = np.array([4, 5, 6])

# Arr = np.concatenate((Arr1, Arr2))

# print(Arr)

arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[5, 6], [7, 8]])

arr = np.concatenate((arr1, arr2), axis=1)

print(arr)