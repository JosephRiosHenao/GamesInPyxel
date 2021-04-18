import math
from shoot import Shoot
from angleMouse import Pitagoras
import pyxel
import rotateEngine
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
        self.shoots = []
        self.angleController = Pitagoras(self.pos[0], self.pos[1])
        
    def update(self):
        self.resetFormPosition()
        self.angleController.update(self.pos[0], self.pos[1])
        self.angle = self.angleController.angle
        if (pyxel.btnp(pyxel.KEY_SPACE)): self.angle += 0
        self.updateHeadPos()
        self.keyDownScan()
        self.points = rotateEngine.update_points(self.points,self.points[2],self.pos,math.radians(self.angle))
        
        for shoot in self.shoots:
            shoot.update()
        #COMPROBAR SECUAENCIA HASTA ANGULO
        
    def draw(self):
        for pixel in self.points:
            pyxel.pset(pixel[0],pixel[1],11)
        for i in range(1,len(self.points)):
            point = self.points[i-1]
            nextPoint = self.points[i]
            pyxel.line(point[0],point[1],nextPoint[0],nextPoint[1],self.col )
        pyxel.line(self.points[0][0],self.points[0][1],self.points[3][0],self.points[3][1],self.col )
        
        for shoot in self.shoots:
            shoot.draw()
        # pyxel.trib(self.points[0][0],self.points[0][1],self.points[1][0],self.points[1][1],self.points[3][0],self.points[3][1],self.col)
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
        if (pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON)):
            self.shoot()
                
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
    def shoot(self):
        self.shoots.append( Shoot(self.pos[0],self.pos[1],0.5,15,self.angle,100 ))
