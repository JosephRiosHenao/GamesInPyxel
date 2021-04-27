import pyxel

class Circle():
    def __init__(self,pos,r):
        self.pos = pos
        self.r = r
    def draw(self):
        pyxel.circ(self.pos[0],self.pos[1],self.r,2)
