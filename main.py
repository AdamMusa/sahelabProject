import cv2
from src.objectRecognize import ObjectRecognizer


if __name__ == "__main__":
    obj = ObjectRecognizer(
    "provider/haarcascade_frontalface_default.xml",
    "provider/haarcascade_eye.xml")
    obj.detectObject()
    obj.cap.release()
    cv2.destroyAllWindows()