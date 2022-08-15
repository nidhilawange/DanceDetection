import numpy as np
import cv2
from picamera2 import Picamera2
import time


picam2 = Picamera2()

# Configure camera image types
def configCamera():
    config = picam2.create_still_configuration({"size": (320, 240)}) #main={"size": (320, 240)}
    picam2.configure(config)
    picam2.start()
    time.sleep(1)

def takePic():
    # Get image and convert to BGR to HSV
    buffer = picam2.capture_array()
    dim = (640,480)
    cv2.resize(buffer, dim, interpolation = cv2.INTER_AREA)
    color = cv2.cvtColor(buffer, cv2.COLOR_RGB2BGR)
    cv2.imwrite("color.jpg", color)

if __name__ == "__main__":
    configCamera()
    takePic()