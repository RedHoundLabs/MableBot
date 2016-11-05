from PIL import ImageGrab
from PIL import Image
import cv2
import numpy

def displayGameFeed(bbox):
    while True:
        pil_image = ImageGrab.grab(bbox=(bbox[0], bbox[1], bbox[2], bbox[3])).convert('RGB')
        image = cv2.cvtColor(numpy.array(pil_image), cv2.COLOR_RGB2BGR)
        cv2.imshow("image", image)
        cv2.waitKey(1)
