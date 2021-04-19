import pyxel
import math
import time
import primaryShoot

class Shoot():
    def __init__(self,x,y,r,col,a,vi,explosion):
        
        self.x = x # X ubicacion
        self.xi = x
        self.y = y # Y ubicacion
        self.yi = y
        
        self.explosion = explosion
        
        self.a = a-90 # Angulo
        self.vi = vi # Velocidad Inicial = hipotenusa
                
        self.t = 0
        self.starting_point = time.time() # Tiempo
        
        self.r = r # Radio
        self.col = col # Color
    
        self.viY = round((math.sin(math.radians(self.a)))*self.vi,2) # Velocidad Inicial Y
        self.vX = round((math.cos(math.radians(self.a)))*self.vi,2) # Velocidad vector X constante
        self.miniShoots = []
        self.angleShoot = 360/self.explosion
        self.angle = 0
        
        self.index = 0

        
        self.state = True
    
    def update(self):
                
        self.elapsed_time = round(time.time () - self.starting_point,2)
        self.t = self.elapsed_time

        if (self.t<0.5):
            self.x = self.xi + self.vX * self.t # multiplica la constante por el timepo para saber la poscicion
            self.y = self.yi + self.viY*self.t
        else:
            if (self.state==True): self.generateExplosion()
            self.state=False
            for shoot in self.miniShoots:
                shoot.update()
        
    def draw(self):
        if (self.t<0.5):
            pyxel.circ(self.x,self.y,self.r,self.col) # Dibujando
        else:
            for shoot in self.miniShoots:
                shoot.draw()
        # pyxel.line(self.x,self.y,self.x+self.r,self.y+self.r,self.col)
        
    def generateExplosion(self):
        for ex in range(self.explosion):
            self.angle += self.angleShoot 
            self.miniShoots.append( primaryShoot.Shoot(self.x,self.y,0.5,self.col,self.angle,100))
        