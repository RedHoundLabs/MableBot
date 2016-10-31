from pykeyboard import PyKeyboard
import time
k = PyKeyboard()

''' Press key on the keyboard '''
def press(character):
    k.tap_key(character)

''' Type a string '''
def type(string):
    k.type_string(string)

''' Press Multiple Keys '''
def pressMultiple(arr):
    k.press_keys(arr)


def forward():
    k.press_key('d')

def backward():
    k.press_key('a')

def attack():
    k.tap_key('b')


def stop():
    k.release_key('d')
    k.release_key('a')

def longJump():
    k.press_key('z')
    time.sleep(1)
    k.release_key('z')


def jump():
    k.press_key('z')
    time.sleep(.2)
    k.release_key('z')
