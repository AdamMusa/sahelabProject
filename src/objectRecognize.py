import cv2
import numpy as np

class ObjectRecognize:

    def __init__(self,haarFace,haarEyes):
        self.haarFace = haarFace
        self.haarEyes = haarEyes

    def videoInitialize(self):
        return cv2.VideoCapture(0)

    def init(self):
        faceCascade = cv2.CascadeClassifier(self.haarFace)
        eyesCascade = cv2.CascadeClassifier(self.haarEyes)
        ret, frame = videoInitialize().read()
        return faceCascade,eyesCascade,ret,frame

    def detectObject(self):
        face,eyes,ret,frame = init()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face.detectMultiScale(gray,scaleFactor=1.1,
        minNeighbors=5,minSize=(30, 30),)

        for (x,y,w,h) in faces:
            pass
