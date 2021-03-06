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
        self.destroy = False
    
    def update(self):
        
        if (self.x > pyxel.width or self.x < 0): self.destroy = True
        if (self.y > pyxel.height or self.y < 0): self.destroy = True
            
        self.elapsed_time = round(time.time () - self.starting_point,2)
        self.t = self.elapsed_time

        self.x = self.xi + self.vX * self.t # multiplica la constante por el timepo para saber la poscicion
        self.y = self.yi + self.viY*self.t
        
    def draw(self):
        pyxel.circ(self.x,self.y,self.r,self.col) # Dibujando
        # pyxel.line(self.x,self.y,self.x+self.r,self.y+self.r,self.col)
        
    def isCollision(self, playerCollisionPos, collisionR):
        if ( not self.destroy):
            distancia = math.sqrt( (playerCollisionPos[0] - self.x)*(playerCollisionPos[0] - self.x) + (playerCollisionPos[1] - self.y)*(playerCollisionPos[1] - self.y) );
            if ( distancia < collisionR + self.r ):
                self.destroy = True
                return True
            else:
                if (not self.destroy): self.destroy = False
                return False