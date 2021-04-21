import pyxel
import time

class Mouse():
    def __init__(self,margin,col):
        self.col = col
        self.colOriginal = col
        self.margin = margin
        self.timeReference = time.time()
    
    def update(self):
        self.x = pyxel.mouse_x
        self.y = pyxel.mouse_y
        timeActually = time.time()-self.timeReference
        
        if (self.col < self.colOriginal and timeActually>0.1): 
            self.col = self.colOriginal
            
        if (pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON) or pyxel.btnp(pyxel.MOUSE_RIGHT_BUTTON)): 
            self.col = 13
            self.timeReference = time.time()
        
    def draw(self):
        pyxel.pset(self.x+self.margin,self.y,self.col) # RIGHT
        pyxel.pset(self.x-self.margin,self.y,self.col) # LEFT
        
        pyxel.pset(self.x,self.y+self.margin,self.col) # DOWN
        pyxel.pset(self.x,self.y-self.margin,self.col) # UP
        
        pyxel.pset(self.x,self.y,self.col) # CENTER