import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

# Create a boolean mask
mask = arr > 3

# Apply the mask to filter elements
f_arr = arr[mask]
print(f_arr)  
# Output: [4 5 6]

# using and , or
f_arr = arr[(arr > 2) & (arr < 6)]
print(f_arr)  
# Output: [3 4 5]

# searching 

# indices = np.where(arr == 3)
indices = np.where(arr % 2 == 0)
print(indices)  
# Output: (array([2]),) → The number 3 is at index 2

# sorting

unsorted_arr = np.array([5, 3, 8, 1, 7])
sorted_arr = np.sort(unsorted_arr)
print(sorted_arr)  
# Output: [1 3 5 7 8]


# descending order
sorted_desc = np.sort(unsorted_arr)[::-1]
print(sorted_desc)  
# Output: [8 7 5 3 1]


# sorting 2d array
arr2D = np.array([[3, 2, 1], [6, 5, 4]])
sorted_2D = np.sort(arr2D)
print(sorted_2D)
# [[1 2 3]
 #[4 5 6]] output
