import numpy as np
import cv2

cap=cv2.VideoCapture(0)

while(1):
    _,frame=cap.read()

    red=np.matrix(frame[:,:,2])
    green=np.matrix(frame[:,:,1])
    blue=np.matrix(frame[:,:,0])

    red_only=np.int16(red)-np.int16(green)-np.int16(blue)

    red_only[red_only<0]=0
    red_only[red_only>255]=255

    #sum of columns
    column_sums=np.matrix(np.sum(red_only,0)) #0 refers to the sum of all columns, 1=sum of rows and 2=sum of colors
    #number of columns
    column_numbers=np.matrix(np.arange(640))#arange=it gives a range of number, gets number b/w 1-640
    #sum of columns * number of columns
    column_mult=np.multiply(column_sums,column_numbers)
    #sum of all the elements in matrix
    total=np.sum(column_mult)
    total_total=np.sum(np.sum(red_only))
    column_location=total/total_total

    print(column_location)
    
    red_only=np.uint8(red_only)

    cv2.imshow('rgb',frame)
    cv2.imshow('red',red)
    cv2.imshow('green',green)
    cv2.imshow('blue',blue)
    cv2.imshow('red_only',red_only)

    k=cv2.waitKey(5)
    if k==27:
        break

cv2.destroyAllWindows()

print(frame)
    
