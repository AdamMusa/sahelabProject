import cv2
from src.objectRecognize import ObjectRecognize


if __name__ == "__main__":
    objRecognize = ObjectRecognize(
    "provider/haarcascade_frontalface_default.xml",
    "provider/haarcascade_eye.xml")
    objRecognize.detectObject()
    cap = objRecognize.initializeVideo()
    #For end instructions
    cap.release()
    cv2.destroyAllWindows()