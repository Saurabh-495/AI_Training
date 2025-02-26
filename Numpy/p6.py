import numpy as np

 
arr_2d = np.array([[1, 2, 4], [4, 5, 6]])
print("Searching the value:")
filter = np.where(arr_2d == 4)
print(filter)
x = arr_2d[filter] 
print(x)




arr = np.array([
    [1, "Green" , 2.5, "Red"],
    [4, "Red", 3.8, "Blue"],
    [7, "Blue", 6.1, "Green"]
])

f = np.where(arr == "Green")
print(f)
x = arr[f]
print(x)
