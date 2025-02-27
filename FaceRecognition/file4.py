import cv2
img=cv2.imread("person.jpg")
print(img)
edges=cv2.Canny(img,100,100)

cv2.imshow("original image",img)

cv2.imshow("edges detected images",edges)

cv2.waitKey(0)
cv2.destroyAllWindows