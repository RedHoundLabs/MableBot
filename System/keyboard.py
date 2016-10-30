from pykeyboard import PyKeyboard
keyboard = PyKeyboard()

''' Press key on the keyboard '''
def press(character):
    keyboard.tap_key(character)

''' Type a string '''
def type(string):
    keyboard.type_string(string)

''' Press Multiple Keys '''
def pressMultiple(arr):
    keyboard.press_keys(arr)
