import cv2
import numpy as np

# Read image as grayscale
img = cv2.imread("cat.jpeg")

# Check if the image was loaded successfully
if img is None:
    print("Error: Unable to read the image. Check the file path and format.")
else:
    # Get image height, width
    (h, w) = img.shape[0:2]

    # Calculate the center of the image
    center = (w / 2, h / 2)

    # Define angles and scale
    angle90 = 90
    angle180 = 180
    angle270 = 270
    scale = 1.0

    print("Image loaded successfully!")
    print(f"Image dimensions: {w}x{h}")
