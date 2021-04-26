import pyxel
import math

class Rect():
    def __init__(self,pos,scale):
        self.pos = pos
        self.scale = scale
        self.per = [0,50]
        self.col = 7    
    def update(self):
        self.center = [self.pos[0]+(self.scale[0]/2),self.pos[1]+(self.scale[1]/2)]
        # if (pyxel.mouse_x>=self.pos[0] and pyxel.mouse_x<=self.pos[0]+self.scale[1]): self.per[0] = pyxel.mouse_x
        if (pyxel.mouse_x > self.pos[0] and pyxel.mouse_x < self.pos[0] + self.scale[0]): self.per[0] = pyxel.mouse_x
        elif (pyxel.mouse_x < self.pos[0]): self.per[0] = self.pos[0]
        elif (pyxel.mouse_x > self.pos[0]): self.per[0] = self.pos[0]+self.scale[0]-1
        
        if (pyxel.mouse_y > self.pos[1] and pyxel.mouse_y < self.pos[1] + self.scale[1]): self.per[1] = pyxel.mouse_y
        elif (pyxel.mouse_y < self.pos[1]): self.per[1] = self.pos[1]
        elif (pyxel.mouse_y > self.pos[1]): self.per[1] = self.pos[1]+self.scale[1]-1
        
    def draw(self):
        pyxel.rect(self.pos[0],self.pos[1],self.scale[0],self.scale[1],self.col)
        
    def colliding(self,pos,r):
        # Círculo con centro en (cx,cy) y radio r
        # Rectángulo con esquina superior izquierda en (x,y) ancho w y algo h
        # Punto (en verde) del perímetro del rectángulo más cercano a la circunferencia en (px,py)
        
        self.per[0] = pos[0]
        if ( self.per[0] < self.pos[0] ): self.per[0] = self.pos[0]
        if ( self.per[0] > self.pos[0] + self.scale[0] ): self.per[0] = self.pos[0] + self.scale[0];
        self.per[1] = pos[1];
        if ( self.per[1] < self.pos[1] ): self.per[1] = self.pos[1];
        if ( self.per[1] > self.pos[1] + self.scale[1] ): self.per[1] = self.pos[1] + self.scale[1];
        distancia = math.sqrt( (pos[0] - self.per[0])*(pos[0] - self.per[0]) + (pos[1] - self.per[1])*(pos[1] - self.per[1]) );
        if ( distancia < r ): self.col = 10
        else: self.col = 7
        
class Circle():
    def __init__(self,pos,r):
        self.pos = pos
        self.r = r
        self.col = 8
    def draw(self):
        pyxel.circ(self.pos[0],self.pos[1],self.r,self.col)
        
class App():
    def __init__(self):
        pyxel.init(100,80)
        self.rect = Rect([pyxel.width/2,pyxel.height/2],[10,10])
        self.circle = Circle([0,0],3)
        pyxel.run(self.update,self.draw)
    def update(self):
        self.circle.pos = [pyxel.mouse_x,pyxel.mouse_y]
        self.rect.update()
        self.rect.colliding(self.circle.pos,self.circle.r)
    def draw(self):
        pyxel.cls(0)
        self.rect.draw()
        self.circle.draw()
        # pyxel.line(self.circle.pos[0],self.circle.pos[1],self.rect.center[0],self.rect.center[1],14)
        pyxel.pset(self.rect.per[0],self.rect.per[1],14)
        
App()
