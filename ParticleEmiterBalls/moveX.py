import pyxel
import random
import math
import time


G = 9.8
PYXELWIDHT = 0.1 

class Ball():
    def __init__(self,x,y,r,col,a,vi):
        
        self.x = x # X ubicacion
        self.xi = x
        self.y = y # Y ubicacion
        
        self.a = a # Angulo
        self.vi = vi # Velocidad Inicial = hipotenusa
                
        self.t = 0
        self.starting_point = time.time() # Tiempo
        
        self.r = r # Radio
        self.col = col # Color
        
        self.starting_point = time.time() # Tiempo

        self.vX = round((math.cos(math.radians(self.a)))*self.vi,2) # Velocidad vector X constante
        
    
    def update(self):
                
        self.elapsed_time = round(time.time() - self.starting_point,2)
        self.t = self.elapsed_time
        
        self.x = self.xi + self.vX * self.t # multiplica la constante por el timepo para saber la poscicion
        
    def draw(self):
        pyxel.circ(self.x,self.y,self.r,self.col) # Dibujando
        
class Pitagoras():
    def __init__(self,Ax,Ay):
        
        self.ca = 0 # Adyaciente
        self.co = 0 # Opuesto
        self.h = 0 # hipotenusa
        
        self.A = 0 # AnguloHallar

        self.Ax = Ax # X Objeto
        self.Ay = Ay # Y Objeto
        
        self.Bx = 0 # X Superior
        self.By = 0 # Y Superor
        
        
    def update(self):
        self.Bx = pyxel.mouse_x # Capturando Posicion MouseX
        self.By = pyxel.mouse_y # Capturando Posicion MouseY
        #self.MouseXVelocity = -pyxel.mouse_x*0.2 # Mejorando presicion de velocidad actual: 38.2
        
        self.ca = self.Bx - self.Ax # Hallar tamaño de cateto adyaciente (Mouse - Triangulo)
        self.co = self.Ay - self.By # Hallar tamaño de cateto opuesto (Triangulo - mouse)
        self.h = round(math.sqrt(math.pow(self.ca, 2) + math.pow(self.co, 2)),2) # Hallar hipotenusa
        self.A = round(math.degrees(math.atan((self.co/self.ca))),2) # Angulo
        
    def draw(self):
        pyxel.line(self.Ax,self.Ay,self.Bx,self.By,15) # Hipotenusa
        pyxel.line(self.Ax,self.Ay,self.Bx,self.Ay,14) # Adyacente
        pyxel.line(self.Bx,self.Ay,self.Bx,self.By,13) # Opuesto
        
class App():
    def __init__(self):
        pyxel.init( width      = 192,
                    height     = 128,
                    caption    = "MoveParabolist",
                    fps        = 60,
                    fullscreen = False )
        
        self.listBalls = []
        self.Triangulo = Pitagoras(10,120) 
        pyxel.run(self.update,self.draw)
        
    def update(self):
        self.checkInput()
        self.Triangulo.update()
        for ball in self.listBalls:
            ball.update()
    
    def draw (self):
        
        pyxel.cls(0) # Fondo
        
        for ball in self.listBalls: # Array de objetos
            ball.draw() # Dibujar Objeto
        self.Triangulo.draw()
    
    def checkInput(self): 
        if (pyxel.btnp(pyxel.KEY_SPACE)): self.generateBall() # Space -> generar bola
        if (pyxel.btnp(pyxel.KEY_R)): self.clearListBall() # R -> Resetear todo
        
    def generateBall(self):
        color = random.randint(1, 15) # Colores random
        self.listBalls.append(Ball(10,120,2,color,self.Triangulo.A,self.Triangulo.h)) # Agregar objecto a la lista
    
    def clearListBall(self):
        self.listBalls.clear() # Limpiar lista de objetos
        
App()