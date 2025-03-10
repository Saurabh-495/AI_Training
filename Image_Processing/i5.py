import cv2 
import numpy as np

img = cv2.imread("cat.jpeg")
# Obtain the dimensions of the image array
# using the shape method
(row, col) = img.shape[0:2]
# Take the average of pixel values of the BGR Channels
# to convert the colored image to grayscale image
for i in range(row):
    for j in range(col):
# Find the average of the BGR pixel values 
      img[i,j] = sum(img[i, j]) * 0.80
cv2.imshow('Grayscale Image', img)
cv2.waitKey(0)
# Window shown waits for any key pressing event
cv2.destroyAllWindows()