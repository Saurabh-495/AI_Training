import numpy as np

a = np.array([[1, 5, 3 , 5], [4, 5, 6 , 5]])
print("Filtering the value")
filter = (a%2 == 1)
print(filter)
x = a[filter]
print(x)