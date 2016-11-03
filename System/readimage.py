import cv2
from PIL import ImageGrab
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt

'''Read image from screen and convert it to opencv'''
pil_image = ImageGrab.grab()
img = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.bilateralFilter(gray, 11, 17, 17)
edged = cv2.Canny(gray, 30, 200)


# find contours in the edged image, keep only the largest
# ones, and initialize our screen contour
(_, cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:10]
screenCnt = None

for c in cnts:
	# approximate the contour
	peri = cv2.arcLength(c, True)
	approx = cv2.approxPolyDP(c, 0.02 * peri, True)

	# if our approximated contour has four points, then
	# we can assume that we have found our screen
	if len(approx) == 4:
		screenCnt = approx


cv2.drawContours(img, [screenCnt], -1, (0, 255, 0), 3)

plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()

'''cv2.imwrite('houghlines3.jpg',img)'''
'''Image._show(test)'''
