import pyxel
from modelPoint import Point

class Player():
    def __init__(self,w,h,x,y,col):
        self.w = w
        self.h = h
        self.x = x
        self.y = y
        self.col = col
        self.angle = 0
        self.speedRotation = 0.1
        self.points = [
            
        ]
        
    def update(self):
        self.angle += self.speedRotation
        
    def draw(self):
        pass
