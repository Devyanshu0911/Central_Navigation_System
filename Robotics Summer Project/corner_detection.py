import cv2 as cv
import numpy as np

img_init=cv.imread("Photos/4.png")

img=cv.resize(img_init,(1000,500),interpolation=cv.INTER_AREA)


gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

imgCanny = cv.Canny(gray,255,255)
gray=np.float32(gray)

corners=cv.cornerHarris(gray,2,3,0.04)

corners=cv.dilate(corners,None)

print(corners)



contours, _ = cv.findContours(imgCanny, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
for cnt in contours:
    area=cv.contourArea(cnt)
    for corner in corners:
        if area>50:
            img[corner>0.1*corner.max()]=[0,255,0]

            
cv.imshow('image',img)

cv.waitKey(0)