import numpy as np
import cv2 as c
cap=c.VideoCapture(0)

while(1):
    a,frame=cap.read()
    blue,green,red=c.split(frame)
    red_only=np.int16(red)-np.int16(green)-np.int16(blue) 
    red_only[red_only<0]=0
    red_only[red_only>255]=255
    red_only=np.uint8(red_only)
    c.imshow('red',red)
    c.imshow('red_only',red_only)
    c.imshow('rgb',frame)
    k=c.waitKey(5)
    if k==27:
        break
c.destroyAllWindows()
print(red_only)
#print(a)
