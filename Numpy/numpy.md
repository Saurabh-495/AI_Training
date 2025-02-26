# What is NumPy?

NumPy (Numerical Python) is a fundamental library in Python for numerical computing. It provides powerful tools for working with multi-dimensional arrays and matrices, along with a vast collection of mathematical functions to operate on these arrays. 1   Think of it as a supercharged list that's optimized for numerical operations.

# Why Numpy

<Efficiency>: NumPy arrays are stored contiguously in memory, making operations much faster than standard Python lists, especially for large datasets.
<Convenience>: NumPy provides a high-level interface for array manipulation, making complex mathematical operations easier to express.
<Foundation>: Many other scientific computing libraries in Python, like Pandas, SciPy, and Matplotlib, are built upon NumPy.

# Installation
-- pip install numpy 
# Importing
-- Import numpy as np

# Creating arrays using numpy
-- # From a Python list
arr = np.array([1, 2, 3, 4, 5])
print(arr)  # Output: [1 2 3 4 5]

# Multi-dimensional array (matrix)
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(matrix)
--Output:
-- [[1 2 3]
-- [4 5 6]]

### i values
 i1 → int8 (1 byte = 8 bits)
i2 → int16 (2 bytes = 16 bits)
i4 → int32 (4 bytes = 32 bits)
i8 → int64 (8 bytes = 64 bits)