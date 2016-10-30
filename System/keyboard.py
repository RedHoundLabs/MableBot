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


def run():
    k.tap_key(k.right_key)

def jump():
    k.press_key('a')
    time.sleep(2)
