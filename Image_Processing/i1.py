import numpy as np
import cv2

img = cv2.imread("cat.jpeg",0)
# print(img)
cv2.imshow("Display window",img)
k = cv2.waitKey(0)
pixel = img[150,150]# h and w || row or columns value  100 100
cv2.imshow("Display window",img)
k = cv2.waitKey(0)
print(pixel) #[ 90 104 116] 3 channel pixels 

