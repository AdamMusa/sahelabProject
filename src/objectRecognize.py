import cv2
import numpy as np

class ObjectRecognizer:

    def __init__(self,haarFace,haarEyes):
        self.haarFace = haarFace
        self.haarEyes = haarEyes

    def initializeVideo(self):
        return cv2.VideoCapture(0)

    def detectObject(self):
        faceCascade = cv2.CascadeClassifier(self.haarFace)
        eyesCascade = cv2.CascadeClassifier(self.haarEyes)
        cap = self.initializeVideo()

        while True:
            ret,frame = cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = faceCascade.detectMultiScale(gray,1.3,5)
            for (x,y,w,h) in faces:
                cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)

            cv2.imshow("Object Recognizer",frame)

            if cv2.waitKey(1)== ord("q"):
                break
