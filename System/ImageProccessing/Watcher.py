from PIL import ImageGrab
from PIL import Image
import cv2
import numpy
import time
import threading
import gtk.gdk

def getImage(bbox):
    while True:
        pil_image = ImageGrab.grab(bbox=(bbox[0], bbox[1], bbox[2], bbox[3])).convert('RGB')
        image = cv2.cvtColor(numpy.array(pil_image), cv2.COLOR_RGB2BGR)
        cv2.imshow("image", image)
        cv2.waitKey(1)


def gtkThingy():
    w = gtk.gdk.get_default_root_window()
    sz = w.get_size()
    print "The size of the window is %d x %d" % sz
    pb = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB,False,8,sz[0],sz[1])
    pb = pb.get_from_drawable(w,w.get_colormap(),0,0,0,0,sz[0],sz[1])
    if (pb != None):
        pb.save("screenshot.png","png")
        print "Screenshot saved to screenshot.png."
    else:
        print "Unable to get the screenshot."


def callback():
    print "hello"


def displayGameFeed(bbox):
    thread = threading.Thread(target=getImage, args=(bbox,))
    thread.start()
