import cv
from src.objectRecognize import ObjectRecognize


if __name__ == "__main__":
    objRecognize = ObjectRecognize(
    "provider/haarcascade_frontalface_default.xml",
    "provider/haarcascade_eye.xml")
    cap = objRecognize.videoInitialize()

    #For end instructions
    cap.release()
    cv2.destroyAllWindows()