#1. Capture a background image, image 1
#2. Wait 'delta t' amount of time
#3. Capture a foreground image, second image, image 2
#4. Subtract one image from the other

import numpy as np
import cv2
#for using the sleep function
import time 

cap=cv2.VideoCapture(0)

while(1):
    _,frame=cap.read()

    red1=np.matrix(frame[:,:,2])
    green1=np.matrix(frame[:,:,1])
    blue1=np.matrix(frame[:,:,0])

    red_only1=np.int16(red1)-np.int16(green1)-np.int16(blue1)

    red_only1[red_only1<0]=0
    red_only1[red_only1>255]=255

    time.sleep(0.1)

    _,frame=cap.read()

    red2=np.matrix(frame[:,:,2])
    green2=np.matrix(frame[:,:,1])
    blue2=np.matrix(frame[:,:,0])

    red_only2=np.int16(red2)-np.int16(green2)-np.int16(blue2)

    red_only2[red_only2<0]=0
    red_only2[red_only2>255]=255

    motion=red_only2-red_only1

    motion[motion<0]=0
    motion[motion>255]=255

   #to find the location the motion is happening at
    column_sums=np.matrix(np.sum(motion,0))
    column_numbers=np.matrix(np.arange(640))
    column_mult=np.multiply(column_sums,column_numbers)
    total=np.sum(column_mult)
    total_total=np.sum(np.sum(motion))
    column_location=total/total_total

    print(column_location)

    motion=np.uint8(motion)

    cv2.imshow('rgb',frame)
    cv2.imshow('motion',motion)

    k=cv2.waitKey(5)
    if k==27:
        break
    
cv2.destroyAllWindows()

print(frame)
