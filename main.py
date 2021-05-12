import cv2
import numpy as np

cap = cv2.VideoCapture(0)

def empty(a):
    pass
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # cv2.putText(frame,"OpenCV",(300,200),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
    cv2.namedWindow("Hello")
    cv2.resizeWindow("Hello",(200,300))
    cv2.createTrackbar("Min","Hello",1,190,empty)
    cv2.imshow('frame',gray)

    if cv2.waitKey(1)== ord("q"):
        break

cap.release()
cv2.destroyAllWindows()