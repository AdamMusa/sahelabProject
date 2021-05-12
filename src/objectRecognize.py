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
        faces = face.detectMultiScale(scaleFactor=1.1,
        minNeighbors=5,minSize=(30, 30),)
