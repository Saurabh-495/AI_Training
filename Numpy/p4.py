import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.shape)  

arr_reshaped = arr.reshape(3, 2)
print(arr_reshaped)


# nditer and ndenumerate
# The numpy.nditer() function allows you to iterate over elements of an array efficiently.

ARR = np.array([[1, 2, 3], [4, 5, 6]])

# Using nditer
for x in np.nditer(ARR):
    print(x)  
# Output: 1 2 3 4 5 6

## denumerate

for index, value in np.ndenumerate(ARR):
    print(f"Index: {index}, Value: {value}")

