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
        self.per[0] = pyxel.mouse_x
        if (pyxel.mouse_x < self.pos[0]): self.per[0] = self.pos[0]
        if (pyxel.mouse_x > self.pos[0]): self.per[0] = self.pos[0]+self.scale[0]
    def draw(self):
        pyxel.rect(self.pos[0],self.pos[1],self.scale[0],self.scale[1],self.col)
        
class Circle():
    def __init__(self,pos,r):
        self.pos = pos
        self.r = r
        self.col = 8
    def draw(self):
        pyxel.circ(self.pos[0],self.pos[1],self.r,self.col)
    def colliding(self,pos):
        # px = cx; // En principio son iguales
        # if ( px < x ) px = x;
        # if ( px > x + w ) px = x + w;
        # py = cy;
        # if ( py < y ) py = y;
        # if ( py > y + h ) py = y + h;
        # distancia = sqrt( (cx - px)*(cx - px) + (cy - py)*(cy - py) );
        # if ( distancia < r ) {
        #     // Colisión detectada
        # }	
        pass
        
class App():
    def __init__(self):
        pyxel.init(100,80)
        self.rect = Rect([pyxel.width/2,pyxel.height/2],[5,5])
        self.circle = Circle([0,0],3)
        pyxel.run(self.update,self.draw)
    def update(self):
        self.circle.pos = [pyxel.mouse_x,pyxel.mouse_y]
        self.rect.update()
    def draw(self):
        pyxel.cls(0)
        self.rect.draw()
        self.circle.draw()
        pyxel.line(self.circle.pos[0],self.circle.pos[1],self.rect.center[0],self.rect.center[1],14)
        pyxel.pset(self.rect.per[0],self.rect.per[1],14)
        
App()
