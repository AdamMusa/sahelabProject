import cv2
from src.objectRecognize import ObjectRecognizer


if __name__ == "__main__":
    objRecognizer = ObjectRecognizer(
    "provider/haarcascade_frontalface_default.xml",
    "provider/haarcascade_eye.xml")
    objRecognizer.detectObject()
    cap = objRecognizer.initializeVideo()
    #For end instructions
    cap.release()
    cv2.destroyAllWindows()