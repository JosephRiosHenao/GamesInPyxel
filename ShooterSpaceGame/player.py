import pyxel


class Player():
    def __init__(self,w,h,x,y,col):
        self.w = w
        self.h = h
        self.x = x
        self.y = y
        self.col = col
    
    def update(self):
        pass
    
    def draw(self):
        pyxel.line(self.x,self.y,self.x-self.w,self.y+self.h,1)
