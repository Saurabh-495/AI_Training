import cv2
img = cv2.imread("cat.jpeg",1)
print('original Dimensions : ', img.shape)
scale = 70
width = int(img.shape[1] * scale / 100)
height = int(img.shape[0] * scale / 100)
dim = (width, height)
# resize image
resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
print(type(resized))
print('Resized Dimensions : ', resized.shape)
cv2.imshow("Resized image", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()