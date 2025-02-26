import cv2
import numpy as np

"""image = cv2.imread("cat.jpeg",1)
cv2.imshow("Cat Image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""

# Image shapes and dimentions
"""image = cv2.imread("cat.jpeg",1)
cv2.imshow("Cat Image",image)

print("Image shape", image.shape)
print("Total number of pixels", image.size)
print("Data type of pixels", image.dtype)
cv2.waitKey(0)
cv2.destroyAllWindows()"""


## COnverting into grayscale image
"""img = cv2.imread("cat.jpeg",1)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Cat Image",gray)
cv2.waitKey(0)
cv2.destroyAllWindows()"""

# Resizing the image

"""img = cv2.imread("cat.jpeg",1)
# resized = cv2.resize(img, (500,500), interpolation = cv2.INTER_AREA)
resized = cv2.resize(img,(300,300))
cv2.imshow("Resized Image", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()"""

# Drawing on an image
# img = cv2.imread("cat.jpeg",1)
# img = np.zeros((500, 500, 3), dtype="uint8")


"""text = "Saurabh Pandey"
position = (50, 250)  # Bottom-left corner
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
color = (255, 255, 255)  # White color
thickness = 2

# Put text on the image
cv2.putText(img, text, position, font, font_scale, color, thickness, cv2.LINE_AA)

cv2.line(img, (50,50), (200,50), (0,255,0),5)
cv2.imshow("Cat Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()"""



# Edge Detection
"""img = cv2.imread("cat.jpeg",1)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 100, 200)
cv2.imshow("Edges", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()"""