import cv2 as cv

img_initial=cv.imread('Photos/path.png')

img=cv.resize(img_initial,(1000,500),interpolation=cv.INTER_AREA)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
blur=cv.GaussianBlur(gray,(7,7),1)

canny=cv.Canny(gray,255,255)

i=1
contour,hierarchy=cv.findContours(canny,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE)

for cnt in contour:
    area=cv.contourArea(cnt)
    if area>500:
        cv.drawContours(img,cnt,-1,(0,255,0),2)
        peri = cv.arcLength(cnt,True)
        approx = cv.approxPolyDP(cnt,0.1*peri,True)
        x,y,w,h = cv.boundingRect(approx)
        cv.putText(img,str(i),(cnt[0][0][0]+20,cnt[0][0][1]+20),cv.FONT_HERSHEY_TRIPLEX,0.5,(0,0,255),thickness=1)
        i+=1
    
cv.imshow('CONTOUR',img)


cv.waitKey(0)

