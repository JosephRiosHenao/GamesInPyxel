import pyxel
class MouseLocation:
    def __init__(self):
        self.x = pyxel.mouse_x
        self.y = pyxel.mouse_y
        self.w = 3
        self.h = 3
    def IsColliding(self, other):
        return self.x < other.x + other.w and \
            self.x + self.w > other.x and \
            self.y < other.y + other.h and \
            self.y + self.h > other.y
        

class Botones:
    def __init__(self,x,y,w,h,col):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.col = col

class Menu:
    def __init__(self):
        self.BallX = 125
        self.BallY = 20
        self.Velocity = 2
        self.ColorBG = 0
        self.ColorObjects = 7
        self.ColorObjectsBG = 7
        self.Horizontal = True
        self.Vertical = True
        self.MouseLocation
        self.ButtonLocal = Botones(125,100,10,5,7)
        pyxel.init(250,256,caption="MenuPrincipal",fullscreen=True)
        pyxel.mouse(True)
        pyxel.load("Resources/BG.pyxres")
        pyxel.run(self.update,self.draw)
    def update(self):
        #TocaBordeDerecho
        if (self.BallX>=250):
            Menu.ColorDefine(self)
            self.Horizontal = True
        #TocaBordeIzquierdo
        if (self.BallX<=0):
            Menu.ColorDefine(self)
            self.Horizontal = False
        #TocaBordes Inferior y Superior
        if (self.BallY>=256):
            Menu.ColorDefine(self)
            self.Vertical = True
        if (self.BallY<=0):
            Menu.ColorDefine(self)
            self.Vertical = False
        #SeleccionaDireccion en las 4 diagonales
        if(self.Horizontal==False and self.Vertical==False):
            self.OrientacionX = False
            self.OrientacionY = False
        if(self.Horizontal==False and self.Vertical==True):
            self.OrientacionX = False
            self.OrientacionY = True
        if(self.Horizontal==True and self.Vertical==False):
            self.OrientacionX = True
            self.OrientacionY = False
        if(self.Horizontal==True and self.Vertical==True):
            self.OrientacionX = True
            self.OrientacionY = True
        #Mueve la pelota
        if (self.OrientacionX==True and self.Horizontal==True):
            self.BallX -= self.Velocity
        if (self.OrientacionX==False and self.Horizontal==False):
            self.BallX += self.Velocity
        if (self.OrientacionY==True and self.Vertical==True):    
            self.BallY -= self.Velocity
        if (self.OrientacionY==False and self.Vertical==False):
            self.BallY += self.Velocity
        if self.MouseLocation.IsColliding(self.ButtonLocal):
            self.ColorBG = 2
        
    def draw(self):
        pyxel.cls(self.ColorBG)
        #pyxel.bltm(0,0,0,0,0,250,256)
        pyxel.circ(self.BallX,self.BallY,2,self.ColorObjects)
        pyxel.text(121,20,"Pong",self.ColorObjectsBG)
        pyxel.rect(self.ButtonLocal.x,self.ButtonLocal.y,self.ButtonLocal.w,self.ButtonLocal.h,self.ButtonLocal.col)
        
    
    def ColorDefine(self):
        if  self.ColorBG == 7 and self.ColorObjects == 0 and self.ColorObjectsBG == 0:
            self.ColorBG = 0
            self.ColorObjects = 7
            self.ColorObjectsBG = 7
        else:
            self.ColorBG = 7
            self.ColorObjects = 0
            self.ColorObjectsBG = 0
Menu()
