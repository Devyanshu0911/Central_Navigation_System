import cv2 as cv
from pyamaze import agent
from queue import PriorityQueue

img_initial=cv.imread('Photos/path.png')

img=cv.resize(img_initial,(1000,500),interpolation=cv.INTER_AREA)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
blur=cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)

canny=cv.Canny(blur,125,175)

def h(cell1,cell2):
    x1,y1=cell1  

    x2,y2=cell2   

    return abs(x1-x2)+abs(y1-y2) 

i=0
contour,heirarchy=cv.findContours(gray,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)

def A_star(m):

    start=(m[0])
    g_score={cell:float("inf") for cell in list1}

    g_score[start]=0 
    f_score={cell:float("inf") for cell in list1}

    n=len(list1)
   
    f_score[start]=h(start,list1[n-1])

   
    open=PriorityQueue()

    open.put((h(start,list1[n-1]),h(start,(1,1)),start)) 
    apath={}


    while not open.empty():
        
        CurrCell=open.get()[2]

        if CurrCell==(1,1):
            break
        for d in "ESWN":
            
            if list1[CurrCell][d]==True:
                
                if d=='E':
                    
                    childCell=(CurrCell[0],CurrCell[1]+1)
                
                if d=='W':
                   
                    childCell=(CurrCell[0],CurrCell[1]-1)

                if d=='N':
                    childCell=(CurrCell[0]-1,CurrCell[1])

                if d=='S':
                    
                    childCell=(CurrCell[0]+1,CurrCell[1])
                
                temp_g_score=g_score[CurrCell]+1
                
                temp_f_score=temp_g_score+h(childCell,(1,1))

                if temp_f_score < f_score[childCell]:
                   
                    g_score[childCell]=temp_g_score
                    f_score[childCell]=temp_f_score

                    open.put((temp_f_score,h(childCell,(1,1)),childCell))

                    apath[childCell]=CurrCell

    fwdPath={}
    cell=(1,1)
    while cell!=start:
        fwdPath[apath[cell]]=cell
        cell=apath[cell]
    return fwdPath

j=0
list1=[]
for cnt in contour:
    val = str((i,j))
    a=(i,j)
    area=cv.contourArea(cnt)
    if area<2800:
        cv.drawContours(img,cnt,-1,(0,255,0),2)
        cv.putText(img,val,cnt[0][0]+20,cv.FONT_HERSHEY_TRIPLEX,0.5,(0,0,255),thickness=1)
    i+=1
    list1.append(i)

A_star(list1)

print(list1)
    
cv.imshow('image',img)

cv.waitKey(0)
