import pyxel
class Keyboard():
    def __init__(self):
        pass
    def detect(self):
        state = 0 
        if pyxel.btn(pyxel.KEY_SPACE): state = 1
        return state