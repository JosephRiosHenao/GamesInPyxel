import pyxel
import random
import math
import time


G = -9.8
PYXELWIDHT = 0.1 

class Pixel():
    def __init__(self,x,y,col):
        self.x = x
        self.y = y
        self.col = col
    def draw(self):
        pyxel.pset(self.x,self.y,self.col)
class Ball():
    def __init__(self,a,xFinal,t):
        self.a = a
        self.xFinal = xFinal
        self.x = self.xi + self.vX * math.cos(math.radians(self.a)) * self.t
        self.y = self.yi + self.vi * math.sin(math.radians(self.a)) + 1/2 * (-9.8) * math.pow(self.t,2)
        self.t = t
        
        self.v0 = 0
        self.xFinal = self.v0*math.cos(math.radians(a))*self.t
        
    def __init__(self,x,y,r,col,a,vi):
        
        self.x = x # X ubicacion
        self.xi = x # X ubicancion para determinar posicion incial
        self.y = y # Y ubicacion
        self.yi = y # Y ubicacion para determinar altura inicial
        
        self.a = a # Angulo
        self.vi = vi # Velocidad Inicial = hipotenusa - Fuerza lanzamiento
                
        self.t = 0
        self.starting_point = time.time() # Tiempo
        
        self.r = r # Radio
        self.col = col # Color
        
        self.dif = + pyxel.height - self.yi
        
        self.listPixel = []
        
        self.starting_point = time.time() # Tiempo

        self.viY = round((math.sin(math.radians(self.a)))*self.vi,2) # Velocidad Inicial Y
        self.vX = round((math.cos(math.radians(self.a)))*self.vi,2) # Velocidad vector X constante
        self.ts = round(self.viY/G,2) * -1 # Tiempo de subida al punto mas alto, multiplico por -1 por el signo
        self.yMax = round(math.pow(self.viY,2) / (2 * (G)),2) * -1 # Altura maxima alcanzada
        self.tTotal = round(2*self.ts,2) # Tiempo total de vuelo el doble de subida
        self.xTotal = round(self.vX*self.tTotal,2) # Despazamiento en X total
        
        print("Componente rectangular Y inicial:",self.viY,"m")
        print("Componente rectangular X constante:",self.vX,"m")
        print("Altura maxima:",self.yMax,"m")
        print("Tiempo para altura maxima:",self.ts,"s")
        print("Tiempo total de vuelo:",self.tTotal,"s")
        print("Dezplazamiento total:",self.xTotal,"m")

        
        
    def update(self):
        
        if self.t < self.tTotal:
            self.elapsed_time = round(time.time () - self.starting_point,2)
            self.t = self.elapsed_time
            
            self.x = self.xi + self.vX * self.t # multiplica la constante por el timepo para saber la poscicion
            
            self.y = (self.viY*self.t+1/2*G*math.pow(self.t,2))  * -1 + (pyxel.height - self.dif)
            
            self.listPixel.append(Pixel(self.x,self.y,self.col))


    def draw(self):
        pyxel.circ(self.x,self.y,self.r,self.col) # Dibujando
        for pixel in self.listPixel:
            pixel.draw()
        
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
        try:
            self.A = round(math.degrees(math.atan((self.co/self.ca))),2) # Angulo
        except ZeroDivisionError as e:
            print("angulo: 0",e)
            
        
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
        pyxel.text(5,5,"Angulo: "+str(self.Triangulo.A)+"°",15)
        pyxel.text(5,10,"Fuerza: "+str(self.Triangulo.h)+"m/s",15)

    
    def checkInput(self): 
        if (pyxel.btnp(pyxel.KEY_SPACE)): self.generateBall() # Space -> generar bola
        if (pyxel.btnp(pyxel.KEY_R)): self.clearListBall() # R -> Resetear todo
        
    def generateBall(self):
        color = random.randint(1, 14) # Colores random
        self.listBalls.append(Ball(10,120,2,color,self.Triangulo.A,self.Triangulo.h)) # Agregar objecto a la lista
    
    def clearListBall(self):
        self.listBalls.clear() # Limpiar lista de objetos
        
App()