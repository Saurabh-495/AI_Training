import numpy as np

arr1 = np.array([1, 2,3,4,5,6,7,8,9])

for x in arr1:
    print(x)
    
# 2d array
print()

arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]])

for x in arr2d:
    for y in x:
        print(y)
        
# nditer() 

print()

arr3d = np.array([[[1,2,3],[4,5,6],[7,8,9]],[[10,11,12],[13,14,15],[16,17,18]]])
for x in np.nditer(arr3d):
    print(x)
