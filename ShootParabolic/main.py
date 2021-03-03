import pyxel
import random

G = 9.8
PYXELWIDHT = 0.1
#a = input("digite angulo")
#A = 0 #X
#B = 0 #y

#H = 0 #HIPOTENUSA

# 20a, 0.9t, 2.87m --> 3.8ms2

# x distancia recorrida de lanzamiento
# t tiempo
# a angulo
# cosa 

# cosa = A/H
# sina = B/H
class Ball():
    def __init__(self,x,y,r,col,a,v):
        self.x = x
        self.y = y
        self.a = a
        self.v = v
        self.t = 0
        self.r = r
        self.col = col
    def update(self):
        if self.y < 120: self.y += G*PYXELWIDHT #SimulatingGrav
        
    def draw(self):
        pyxel.circ(self.x,self.y,self.r,self.col)
        
class Pitagoras():
    def __init_(self,Ax,Ay):
        
        self.a = 0 # Adyaciente
        self.b = 0 # Opuesto
        self.h = 0 # hipotenusa
        
        self.A = 0 # AnguloHallar
        self.B = 0 # AnguloSuperior
        self.C = 90 # AnguloRectangulo
        
        self.Ax = 0 # X Objeto
        self.Ay = 0 # Y Objeto
        
        self.Bx = 0 # X Superior
        self.By = 0 # Y Superor
        
        self.Cx = 0 # X Rectangulo
        self.Cy = 0 # Y Rectangulo
        
    def update(self):
        pass
    def draw(self):
        pyxel.line()
        
class App():
    def __init__(self):
        pyxel.init( width      = 192,
                    height     = 128,
                    caption    = "MoveParabolist",
                    fps        = 60,
                    fullscreen = False )
        self.listBalls = []
        
        pyxel.run(self.update,self.draw)
        
    def update(self):
        self.checkInput()
        for ball in self.listBalls:
            ball.update()
    
    def draw (self):
        
        pyxel.cls(0)
        
        for ball in self.listBalls:
            ball.draw()
    
    def checkInput(self):
        if (pyxel.btnp(pyxel.KEY_SPACE)): self.generateBall()
        if (pyxel.btnp(pyxel.KEY_R)): self.clearListBall()
        
    def generateBall(self):
        color = random.randint(1, 15)
        self.listBalls.append(Ball(10,10,2,color,10,10))
    
    def clearListBall(self):
        self.listBalls.clear()
        
App()