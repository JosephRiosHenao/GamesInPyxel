import math
from angleMouse import Pitagoras
import pyxel
import rotateEngine
from angleMouse import Pitagoras
from time import time

VELOCITY = 1
ROTATION_VELOCITY = 0.1

class Player():
    def __init__(self,w,h,x,y,col):
        self.size = [w,h]
        self.pos = [x,y]
        self.col = col
        self.angle = 0
        self.points = [
            [self.pos[0],self.pos[1]-self.size[1]], #SUPERIOR
            [self.pos[0]+self.size[0]/2,self.pos[1]+self.size[1]], #DERECHA
            [self.pos[0],self.pos[1]], #ABAJO
            [self.pos[0]-self.size[0]/2,self.pos[1]+self.size[1]], #IZQUIERDA
        ]
        self.pt = time()
        self.angleController = Pitagoras(self.pos[0], self.pos[1])
        
    def update(self):
        self.resetFormPosition()
        self.angleController.update(self.pos[0], self.pos[1])
        self.angle = 270
        if (pyxel.btnp(pyxel.KEY_SPACE)): self.angle += 0
        self.updateHeadPos()
        self.keyDownScan()
        self.points = rotateEngine.update_points(self.points,self.points[2],self.pos,math.radians(self.angle))
                
        #COMPROBAR SECUAENCIA HASTA ANGULO
        
    def draw(self):
        for pixel in self.points:
            pyxel.pset(pixel[0],pixel[1],11)
        self.angleController.draw()
        
    def keyDownScan(self):
        if (pyxel.btn(pyxel.KEY_W)):
            self.pos[1]-=VELOCITY
        if (pyxel.btn(pyxel.KEY_A)):
            self.pos[0]-=VELOCITY
        if (pyxel.btn(pyxel.KEY_S)):
            self.pos[1]+=VELOCITY
        if (pyxel.btn(pyxel.KEY_D)):
            self.pos[0]+=VELOCITY
                
    def updateHeadPos(self):
        newPoint = self.points[2]
        newPoint[0] = self.pos[0]
        newPoint[1] = self.pos[1]
        self.points[2] = newPoint
        
    def resetFormPosition(self):
        self.points = [
            [self.pos[0],self.pos[1]-self.size[1]], #SUPERIOR
            [self.pos[0]+self.size[0]/2,self.pos[1]+self.size[1]], #DERECHA
            [self.pos[0],self.pos[1]], #ABAJO
            [self.pos[0]-self.size[0]/2,self.pos[1]+self.size[1]], #IZQUIERDA
        ]