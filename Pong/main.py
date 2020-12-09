import os
import pyxel
import sys

class MouseCheckLocation:
    def __init__(self,x,y,w,h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
    def IsColliding(self, other):
        return self.x < other.x + other.w and \
            self.x + self.w > other.x and \
            self.y < other.y + other.h and \
            self.y + self.h > other.y

class Botones:
    def __init__(self,x,y,w,h,col,texto):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.col = col
        self.texto = texto

        
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
        self.MouseLocation = MouseCheckLocation(0,0,3,3)
        self.ButtonLocal = Botones(105,150,50,20,7,"LOCAL 2P")
        self.ButtonLAN = Botones(105,180,50,20,7,"LAN")
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

        self.MouseLocation.x = pyxel.mouse_x
        self.MouseLocation.y = pyxel.mouse_y
        if (self.MouseLocation.IsColliding(self.ButtonLocal)):
            self.ButtonLocal.col = 3
            if (pyxel.btn(pyxel.MOUSE_LEFT_BUTTON)):
                os.system("python Pong/Resources/GameTwoPlayersLocal.py")
                
        else:
            self.ButtonLocal.col = 7
        
    def draw(self):
        pyxel.cls(self.ColorBG)
        pyxel.circ(self.BallX,self.BallY,2,self.ColorObjects)
        pyxel.text(121,20,"Pong",self.ColorObjectsBG)
        pyxel.text(10,10,str(self.MouseLocation.x),7)
        pyxel.text(10,20,str(self.MouseLocation.y),7)
        #pyxel.text(10,40,str(pyxel.MOUSE_RIGHT_BUTTON),7)
        #ButtonLocal
        pyxel.rectb(self.ButtonLocal.x,self.ButtonLocal.y,self.ButtonLocal.w,self.ButtonLocal.h,self.ButtonLocal.col)
        pyxel.text(self.ButtonLocal.x + 10,self.ButtonLocal.y + 7,self.ButtonLocal.texto,self.ButtonLocal.col)
        #ButtonLan
        pyxel.rectb(self.ButtonLAN.x,self.ButtonLAN.y,self.ButtonLAN.w,self.ButtonLAN.h,self.ButtonLAN.col)
        pyxel.text(self.ButtonLAN.x + 20,self.ButtonLAN.y + 7,self.ButtonLAN.texto,self.ButtonLAN.col)

    def ColorDefine(self):
        """if  self.ColorBG == 7 and self.ColorObjects == 0 and self.ColorObjectsBG == 0:
            self.ColorBG = 0
            self.ColorObjects = 7
            self.ColorObjectsBG = 7
        else:
            self.ColorBG = 7
            self.ColorObjects = 0
            self.ColorObjectsBG = 0"""


            
Menu()
