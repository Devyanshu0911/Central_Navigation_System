import cv2 as cv
from cv2 import aruco
import numpy as np

marker_dict=aruco.Dictionary_get(aruco.DICT_4X4_1000)

parameters_marker=aruco.DetectorParameters_create()
 
img = cv.imread("Photos/ar3.jpg")




gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
marker_corner,marker_IDs,reject=aruco.detectMarkers(gray,marker_dict,parameters=parameters_marker) #Detecting markers
print(marker_corner)
if marker_corner: #Giving condition
    for id,corners in zip(marker_IDs,marker_corner):
        cv.polylines(img,[corners.astype(np.int32)],True,(0,255,0),2,cv.LINE_AA)
        corners=corners.reshape(4,2)
        corners=corners.astype(int)
        top_right=corners[0].ravel()
        cv.putText(img,f"id:{id[0]}",top_right,cv.FONT_HERSHEY_TRIPLEX,1.0,(0,0,255),thickness=2)
        print(corners)
        print(corners.shape)
cv.imshow('Video',img)
cv.waitKey(0)