import cv2
from PIL import ImageGrab
from PIL import Image
import numpy
from matplotlib import pyplot as plt

pil_image = ImageGrab.grab()
img = cv2.cvtColor(numpy.array(pil_image), cv2.COLOR_RGB2BGR)

'''img = cv2.imread(opencvImage,0)'''
edges = cv2.Canny(img,100,200)

plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()

'''Image._show(test)'''
