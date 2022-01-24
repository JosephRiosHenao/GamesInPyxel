import pyxel
from settings import CONFIG

class Path():
    def __init__(self, x,y):
        self.pos = [x,y]
        self.col = CONFIG["defaultColor"]
        self.stateMouse = False
    def update(self):
        if (self.collisionMouse()): 
            self.stateMouse = True
            self.col = CONFIG["pathColor"]
        else: 
            self.stateMouse = False
            self.col = CONFIG["defaultColor"]
    def draw(self):
        pyxel.rect(self.pos[0], self.pos[1],CONFIG["scaleBG"],CONFIG["scaleBG"],self.col)
    def collisionMouse(self):
        return self.pos[0] < pyxel.mouse_x + 1 and self.pos[0] + CONFIG["scaleBG"] > pyxel.mouse_x and self.pos[1] < pyxel.mouse_y + 1 and self.pos[1] + CONFIG["scaleBG"] > pyxel.mouse_y
    def distanceSet(self, state):
        if (state==0): self.col = CONFIG["distanceColor"][0]