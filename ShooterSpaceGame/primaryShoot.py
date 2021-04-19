import pyxel
import math
import time

class Shoot():
    def __init__(self,x,y,r,col,a,vi):
        
        self.x = x # X ubicacion
        self.xi = x
        self.y = y # Y ubicacion
        self.yi = y
        
        self.a = a-90 # Angulo
        self.vi = vi # Velocidad Inicial = hipotenusa
                
        self.t = 0
        self.starting_point = time.time() # Tiempo
        
        self.r = r # Radio
        self.col = col # Color
    
        self.viY = round((math.sin(math.radians(self.a)))*self.vi,2) # Velocidad Inicial Y
        self.vX = round((math.cos(math.radians(self.a)))*self.vi,2) # Velocidad vector X constante

        self.index = 0
    
    def update(self):
                
        self.elapsed_time = round(time.time () - self.starting_point,2)
        self.t = self.elapsed_time

        self.x = self.xi + self.vX * self.t # multiplica la constante por el timepo para saber la poscicion
        self.y = self.yi + self.viY*self.t
        
    def draw(self):
        pyxel.circ(self.x,self.y,self.r,self.col) # Dibujando
        # pyxel.line(self.x,self.y,self.x+self.r,self.y+self.r,self.col)