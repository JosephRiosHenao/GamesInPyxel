import pyxel
from settings import CONFIG

class Path():
    def __init__(self, x,y):
        self.pos = [x,y]
        self.col = CONFIG["defaultColor"]
    def draw(self):
        pyxel.rect(self.pos[0], self.pos[1],CONFIG["scaleBG"],CONFIG["scaleBG"],self.col)