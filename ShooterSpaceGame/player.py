import math
import primaryShoot
import secondShoot
import thirdShoot
from angleMouse import Pitagoras
import pyxel
import rotateEngine
from time import time

VELOCITY = 0.1
REDUCE_VELOCITY = 0.01
MAX_VELOCITY = 1

class Player():
    def __init__(self,w,h,x,y,col):
        self.size = [w,h]
        self.pos = [x,y]
        self.col = col
        self.angle = 0
        self.velocity = [0,0]
        self.stateShoot = True
        self.points = [
            [self.pos[0],self.pos[1]-self.size[1]], #SUPERIOR
            [self.pos[0]+self.size[0]/2,self.pos[1]+self.size[1]], #DERECHA
            [self.pos[0],self.pos[1]], #ABAJO
            [self.pos[0]-self.size[0]/2,self.pos[1]+self.size[1]], #IZQUIERDA
        ]
        self.shoots = []
        self.angleController = Pitagoras(self.pos[0], self.pos[1])
        
    def update(self, stateShoot):
        self.stateShoot = stateShoot
        self.resetFormPosition()
        self.angleController.update(self.pos[0], self.pos[1])
        self.angle = self.angleController.angle
        if (pyxel.btnp(pyxel.KEY_SPACE)): self.angle += 0
        self.updateHeadPos()
        self.keyDownScan()
        self.points = rotateEngine.update_points(self.points,self.points[2],self.pos,math.radians(self.angle))
        
        for shoot in self.shoots:
            shoot.update()
        self.calculateShoot()
        
        
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
            self.velocity[1] -=VELOCITY
        if (pyxel.btn(pyxel.KEY_A)):
            self.velocity[0] -=VELOCITY
        if (pyxel.btn(pyxel.KEY_S)):
            self.velocity[1] +=VELOCITY
        if (pyxel.btn(pyxel.KEY_D)):
            self.velocity[0] +=VELOCITY
        if (pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON) and self.stateShoot):
            self.shoot(1)
        if (pyxel.btnp(pyxel.MOUSE_RIGHT_BUTTON) and self.stateShoot):
            self.shoot(2)
        if (pyxel.btnp(pyxel.KEY_SPACE) and self.stateShoot):
            self.shoot(3)
        if (pyxel.btnp(pyxel.KEY_Q)):
            print(self.shoots)
            
        self.pos[1]+=self.velocity[1] 
        self.pos[0]+=self.velocity[0] 

        if (self.velocity[0] >0):
            self.velocity[0] -= REDUCE_VELOCITY
        if (self.velocity[0] <0):
            self.velocity[0] += REDUCE_VELOCITY
            
        if (self.velocity[1] >0):
            self.velocity[1] -= REDUCE_VELOCITY
        if (self.velocity[1] <0):
            self.velocity[1] += REDUCE_VELOCITY
            
        if (self.velocity[0] < (MAX_VELOCITY*-1)): self.velocity[0] = MAX_VELOCITY*-1
        if (self.velocity[0] > MAX_VELOCITY): self.velocity[0] = MAX_VELOCITY
        
        if (self.velocity[1] < (MAX_VELOCITY*-1)): self.velocity[1] = MAX_VELOCITY*-1
        if (self.velocity[1] > MAX_VELOCITY): self.velocity[1] = MAX_VELOCITY
                
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
    def shoot(self,type):
        if (type==1): self.shoots.append( primaryShoot.Shoot(self.pos[0],self.pos[1],0.5,15,self.angle,100 ))
        if (type==2): self.shoots.append( secondShoot.Shoot(self.pos[0],self.pos[1],2,14,self.angle,50,15))
        if (type==3): self.shoots.append( thirdShoot.Shoot(self.pos[0],self.pos[1],2,14,self.angle,50,4))
        if (type==4): self.shoots.append( thirdShoot.Shoot(self.pos[0],self.pos[1],2,14,self.angle,50,8))
        self.defineIndex()

    def defineIndex(self):
        for i in range(0,len(self.shoots)):
            self.shoots[i].index = i
            
    def removeShoot(self,index):
        self.shoots.pop(index)
        self.defineIndex()

    
    def calculateShoot(self):
        for shoot in self.shoots:
            if (shoot.destroy==True): self.removeShoot(shoot.index)
            elif (shoot.destroy==True): self.removeShoot(shoot.index)