from pykeyboard import PyKeyboard
keyboard = PyKeyboard()

def press(character):
    keyboard.press_key(character)

def type(string):
    keyboard.type_string(string)
