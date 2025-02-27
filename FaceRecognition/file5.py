import numpy as np
import cv2
img = cv2.imread("person.jpg")
cropped_img = img[200:600,200:500]

cv2.imshow("Original Image", img)

cv2.imshow("Cropped Image", cropped_img)

cv2.waitKey(0)

cv2.destroyAllWindows()

# Save the cropped image

cv2.imwrite("cropped_cat.jpg", cropped_img)

print("Image saved successfully!")