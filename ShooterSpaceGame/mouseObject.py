import pyxel
import time
import rotateEngine
import math

ROTATE = 10

class Mouse():
    def __init__(self,margin,col):
        self.col = col
        self.colOriginal = col
        self.margin = margin
        self.timeReference = time.time()
        self.pos = [0,0]
        self.stateTurn = False
        self.stateShoot = True

    
    def update(self):
        self.pos = [pyxel.mouse_x,pyxel.mouse_y]
        
        self.pixels = [
            [self.pos[0] , self.pos[1] ],             # CENTER
            [self.pos[0] + self.margin,self.pos[1] ], # RIGHT
            [self.pos[0] - self.margin,self.pos[1] ], # LEFT
            [self.pos[0] , self.pos[1] +self.margin], # DOWN
            [self.pos[0] , self.pos[1] -self.margin], # UP
        ]
        
        timeActually = time.time()-self.timeReference
        
        if (self.col < self.colOriginal and timeActually>0.1): 
            self.col = self.colOriginal
            
        if (pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON)): 
            self.col = 13
            self.setTurn(90)
            self.timeReference = time.time()
            
        if (pyxel.btnp(pyxel.MOUSE_RIGHT_BUTTON)):
            self.col = 13
            self.setTurn(-90)
            self.timeReference = time.time()

            self.timeReference = time.time()            
        if (pyxel.btnp(pyxel.KEY_SPACE)): 
            self.setTurn(360)
            
        if (self.stateTurn):
            self.turn()
        else:
            self.stateShoot = True
            self.actuallyGrades = 0
            self.necesaryGrades = 0     
            self.pixels = rotateEngine.update_points(self.pixels,self.pos,self.pos,math.radians(self.actuallyGrades))

    
    def draw(self):
        for pixel in self.pixels:
            pyxel.pset(pixel[0],pixel[1],self.col)
        if (not self.stateShoot):
            if (pyxel.btn(pyxel.MOUSE_LEFT_BUTTON) or pyxel.btn(pyxel.MOUSE_RIGHT_BUTTON) or pyxel.btn(pyxel.KEY_SPACE)):
                pyxel.text((self.pos[0])-((pyxel.FONT_WIDTH*len("RECARGANDO..."))/2),self.pos[1]+(self.margin*2),"RECARGANDO...",1)
            
    def setTurn(self,grades):
        if (self.stateShoot):
            self.stateShoot = False
            self.stateTurn = True
            self.actuallyGrades = 0
            self.necesaryGrades = grades
        
    def turn(self):
        if (self.necesaryGrades<0): self.actuallyGrades -= ROTATE 
        else: self.actuallyGrades += ROTATE
        if (self.necesaryGrades == self.actuallyGrades): self.stateTurn = False
        self.pixels = rotateEngine.update_points(self.pixels,self.pos,self.pos,math.radians(self.actuallyGrades))
            
            
