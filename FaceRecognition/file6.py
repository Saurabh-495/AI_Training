import cv2 as cv
import numpy as np

# capture imagge and display

cap = cv.VideoCapture(0)

while (1):
    ret, frame = cap.read()
    # convert into hsv
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    
    # define range of red color
    lower_red = np.array([161, 155, 84])
    upper_red = np.array([179, 255, 255])
    
    # create a mask
    mask = cv.inRange(hsv, lower_red, upper_red)
    res = cv.bitwise_and(frame,frame,mask=mask)
    
    #DISPLAY
    cv.imshow('ORIGINAL', frame)
    edges = cv.Canny(frame,100,200)
    cv.imshow('mask', mask)
    cv.imshow('res', res)
    
    k = cv.waitKey(5) & 0xFF
    if k == ord("s"):
        cv.imwrite('saurabh', frame)

cap.release()    # release the video capture object 
cv.destroyAllWindows()

"""
# HSV :- An hsv coloris the most accurate color model as long  

#  

Hue: Hue tells the angle to look at the cylindrical disk. The hue represents the color. The hue value ranges from o to 360 degrees.

0-60     Red

60-120   Yellow

120-180  Green

180-240  Cyan

240-300  Blue

300-360  Magenta

# Saturation: The saturation value tells us how much quantity of respective color must be added. A 100% saturation means that complete pure color is added, while a 0% saturation means no color is added, resulting in grayscale.

# Value: The value represents the brightness concerning the saturation of the color. the value 0 represents total black darkness, while the value 100 will mean a full brightness and depend on the saturation. 
"""