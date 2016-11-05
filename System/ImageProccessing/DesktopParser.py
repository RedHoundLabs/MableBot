import cv2
from PIL import ImageGrab
from PIL import Image
import numpy
from matplotlib import pyplot as plt


# initialize the list of reference points and boolean indicating
# whether cropping is being performed or not
refPt = []
cropping = False

def click_and_crop(event, x, y, flags, param):
	# grab references to the global variables
	global refPt, cropping

	# if the left mouse button was clicked, record the starting
	# (x, y) coordinates and indicate that cropping is being
	# performed
	if event == cv2.EVENT_LBUTTONDOWN:
		refPt = [(x, y)]
		cropping = True

	# check to see if the left mouse button was released
	elif event == cv2.EVENT_LBUTTONUP:
		# record the ending (x, y) coordinates and indicate that
		# the cropping operation is finished
		refPt.append((x, y))
		cropping = False

		# draw a rectangle around the region of interest
		cv2.rectangle(image, refPt[0], refPt[1], (0, 255, 0), 2)
		cv2.imshow("image", image)


# load the image, clone it, and setup the mouse callback function
pil_image = ImageGrab.grab()
image = cv2.cvtColor(numpy.array(pil_image), cv2.COLOR_RGB2BGR)
clone = image.copy()
cv2.namedWindow("image")
cv2.setMouseCallback("image", click_and_crop)

# keep looping until the 'q' key is pressed
while True:
	# display the image and wait for a keypress
	cv2.imshow("image", image)
	key = cv2.waitKey(1) & 0xFF

	# if the 'c' key is pressed, break from the loop
	if key == ord("c"):
		break

# if there are two reference points, then crop the region of interest
# from teh image and display it
cv2.destroyWindow("image")
if len(refPt) == 2:
	# close all open windows
    cv2.destroyWindow("image")
    cv2.waitKey(0)
    img = ImageGrab.grab(bbox=(refPt[0][0], refPt[0][1], refPt[1][0], refPt[1][1]))
    img.show()
