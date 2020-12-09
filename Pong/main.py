import pyxel
import socket


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
    def __init__(self,x,y,w,h,col,texto,Visible):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.col = col
        self.texto = texto
        self.Visible = Visible
        
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
        self.BorderLAN = 20
        self.ServerButton = Botones(105,200,50,20,7,"Server",False)
        self.ClientButton = Botones(105,220,50,20,7,"Client",False)
        self.Hover = 3
        self.MouseLocation = MouseCheckLocation(0,0,3,3)
        self.ButtonLocal = Botones(105,150,50,20,7,"LOCAL 2P",True)
        self.ButtonLAN = Botones(105,180,50,20,7,"LAN",True)
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
            self.ButtonLocal.col = self.Hover
            if (pyxel.btn(pyxel.MOUSE_LEFT_BUTTON)):
                pyxel.quit()
                PongLocal2P()
        else:
            self.ButtonLocal.col = 7
        if self.MouseLocation.IsColliding(self.ButtonLAN):
            self.ButtonLAN.col = self.Hover
            if (pyxel.btnr(pyxel.MOUSE_LEFT_BUTTON)):
                self.LANOptions()
        else:
            self.ButtonLAN.col = 7
        if (self.MouseLocation.IsColliding(self.ServerButton)):
            self.ServerButton.col = self.Hover
            if(pyxel.btnr(pyxel.MOUSE_LEFT_BUTTON)):
                pyxel.quit()
                PongLANServer()
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
        pyxel.text(self.ButtonLAN.x + self.BorderLAN,self.ButtonLAN.y + 7,self.ButtonLAN.texto,self.ButtonLAN.col)

        if (self.ServerButton.Visible==True and self.ClientButton.Visible==True):
            pyxel.rectb(self.ServerButton.x,self.ServerButton.y,self.ServerButton.w,self.ServerButton.h,self.ServerButton.col)
            pyxel.text(self.ServerButton.x + 13,self.ServerButton.y + 7,self.ServerButton.texto,self.ServerButton.col)
            pyxel.rectb(self.ClientButton.x,self.ClientButton.y,self.ClientButton.w,self.ClientButton.h,self.ClientButton.col)
            pyxel.text(self.ClientButton.x + 13,self.ClientButton.y + 7,self.ClientButton.texto,self.ClientButton.col)
    def ColorDefine(self):
        """if  self.ColorBG == 7 and self.ColorObjects == 0 and self.ColorObjectsBG == 0:
            self.ColorBG = 0
            self.ColorObjects = 7
            self.ColorObjectsBG = 7
        else:
            self.ColorBG = 7
            self.ColorObjects = 0
            self.ColorObjectsBG = 0"""
    
    def LANOptions(self):
        if ((self.ServerButton.Visible == True) and (self.ClientButton.Visible == True)):
            self.ButtonLAN.texto = "LAN"
            self.BorderLAN = 20
            self.ServerButton.Visible = False
            self.ClientButton.Visible = False
        else:
            self.ButtonLAN.texto = "Close"
            self.BorderLAN = 15
            self.ServerButton.Visible = True
            self.ClientButton.Visible = True
class Ball:
    def __init__(self,x,y,w,h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.col = 8
class Players:
    def __init__(self,x,y,w,h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.col = 8

    def is_colliding(self, other):
        return self.x < other.x + other.w and \
            self.x + self.w > other.x and \
            self.y < other.y + other.h and \
            self.y + self.h > other.y
class PongLocal2P:
    def __init__(self):
        self.PuntosPlayerOne = 0
        self.PuntosPlayerTwo = 0
        self.OnePlayerY = 63
        self.TwoPlayerY = 63
        self.BallX = 120
        self.BallY = 75
        self.Velocity = 3
        self.Score = 0
        self.MensajeGanador = ""
        self.Horizontal = True
        self.Vertical = False
        self.PASOS = 4
        self.PlayerOne = Players(15,self.OnePlayerY,4,25)
        self.PlayerTwo = Players(220,self.TwoPlayerY,4,25)
        self.BallDetails = Ball(self.BallX,self.BallY,2,2)
        self.ColorObjectsBG = 7
        self.ColorBG = 0
        self.ColorObjects =7
        pyxel.init(240,150,caption="PongGame LOCAL",fullscreen=True)
        pyxel.mouse(True)
        pyxel.run(self.update,self.draw)

    def update(self):
        #Player1 Keys
        if (pyxel.btn(pyxel.KEY_W) and self.OnePlayerY>0):
            self.OnePlayerY -= self.PASOS
        if (pyxel.btn(pyxel.KEY_S) and self.OnePlayerY<125):
            self.OnePlayerY += self.PASOS
        #Plater2 Keys
        if (pyxel.btn(pyxel.KEY_UP) and self.TwoPlayerY>0):
            self.TwoPlayerY -= self.PASOS
        if (pyxel.btn(pyxel.KEY_DOWN) and self.TwoPlayerY<125):
            self.TwoPlayerY += self.PASOS
        #TocaBordeDerecho
        if (self.BallX>=240):
            PongLocal2P.ColorDefine(self)
            self.BallX = 120
            self.BallY = 75
            self.Horizontal = True
            self.PuntosPlayerOne += 1
        #TocaBordeIzquierdo
        if (self.BallX<=0):
            PongLocal2P.ColorDefine(self)
            self.BallX = 120
            self.BallY = 75
            self.Horizontal = False
            self.PuntosPlayerTwo += 1
        #Concional de ganador
        if (self.PuntosPlayerOne==5 or self.PuntosPlayerTwo==5):
            if (self.PuntosPlayerOne==5):
                self.MensajeGanador = "Player ONE win \n\n\n\n R = Reset\n X = Return to Menu\n ESC = Exit"
            if (self.PuntosPlayerTwo==5):
                self.MensajeGanador = "Player TWO win \n\n\n\n R = Reset\n X = Return to Menu\n ESC = Exit"
            pyxel.flip()
            self.Velocity = 0
            self.PASOS = 0
            self.BallX = 120
            self.BallY = 75
            self.OnePlayerY = 63
            self.TwoPlayerY = 63
            if (pyxel.btn(pyxel.KEY_R)):
                self.Score = 0
                self.PuntosPlayerOne = 0
                self.PuntosPlayerTwo = 0
                self.MensajeGanador = ""
                self.PASOS = 4
                self.Velocity = 3
                self.OnePlayerY = 63
                self.TwoPlayerY = 63
            if (pyxel.btn(pyxel.KEY_X)):
                pyxel.quit()
                Menu()
        #TocaBordes Inferior y Superior
        if (self.BallY>=150):
            self.Vertical = True
        if (self.BallY<=0):
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

        #Update position players
        self.PlayerOne.y = self.OnePlayerY
        self.PlayerTwo.y = self.TwoPlayerY

        #Update position ball
        self.BallDetails.x = self.BallX
        self.BallDetails.y = self.BallY

        #Collsions
        if self.PlayerOne.is_colliding(self.BallDetails):
            self.Horizontal = False
            self.Score += 5
        if self.PlayerTwo.is_colliding(self.BallDetails):
            self.Horizontal = True
            self.Score += 5

    def draw(self):
        pyxel.cls(self.ColorBG)
        pyxel.line(120,0,120,150,self.ColorObjectsBG)
        pyxel.text(95,60,str(self.MensajeGanador),self.ColorObjectsBG)
        pyxel.text(105,10,"Score: "+str(self.Score),self.ColorObjectsBG)
        pyxel.text(15,10,str(self.PuntosPlayerOne),self.ColorObjectsBG)
        pyxel.text(220,10,str(self.PuntosPlayerTwo),self.ColorObjectsBG)
        pyxel.rect(15,self.OnePlayerY,4,25,self.ColorObjects)
        pyxel.rect(220,self.TwoPlayerY,4,25,self.ColorObjects)
        pyxel.circ(self.BallX,self.BallY,2,self.ColorObjects)

    def ColorDefine(self):
        if  self.ColorBG == 7 and self.ColorObjects == 0 and self.ColorObjectsBG == 0:
            self.ColorBG = 0
            self.ColorObjects = 7
            self.ColorObjectsBG = 7
        else:
            self.ColorBG = 7
            self.ColorObjects = 0
            self.ColorObjectsBG = 0

class PongLANServer:
    def __init__(self):
        """self.LAN = socket.socket()
        self.nombre_equipo = socket.gethostname()
        self.direccion_equipo = socket.gethostbyname(self.nombre_equipo)
        self.LAN.bind((socket.gethostbyname(self.nombre_equipo),8080))
        self.LAN.listen(1)
        self.Usuario = self.LAN.accept()
        print("Nueva conexion")"""
        #self.Usuario.send("Hola desde el servidor".encode())
        self.PuntosPlayerOne = 0
        self.PuntosPlayerTwo = 0
        self.OnePlayerY = 63
        self.TwoPlayerY = 63
        self.BallX = 120
        self.BallY = 75
        self.Velocity = 3
        self.Score = 0
        self.MensajeGanador = ""
        self.Horizontal = True
        self.Vertical = False
        self.PASOS = 4
        self.PlayerOne = Players(15,self.OnePlayerY,4,25)
        self.PlayerTwo = Players(220,self.TwoPlayerY,4,25)
        self.BallDetails = Ball(self.BallX,self.BallY,2,2)
        self.ColorObjectsBG = 7
        self.ColorBG = 0
        self.ColorObjects =7
        self.ConexionMensaje = "Esperando conexion...\n{}".format(self.direccion_equipo)
        pyxel.init(240,150,caption="PongGame LOCAL",fullscreen=False)
        pyxel.mouse(True)
        pyxel.run(self.update,self.draw)
    def EncontrarCliente(self):
        a= 0
    def update(self):
        #Player1 Keys
        if (pyxel.btn(pyxel.KEY_W) and self.OnePlayerY>0):
            self.OnePlayerY -= self.PASOS
        if (pyxel.btn(pyxel.KEY_S) and self.OnePlayerY<125):
            self.OnePlayerY += self.PASOS
        #TocaBordeDerecho
        if (self.BallX>=240):
            PongLocal2P.ColorDefine(self)
            self.BallX = 120
            self.BallY = 75
            self.Horizontal = True
            self.PuntosPlayerOne += 1
        #TocaBordeIzquierdo
        if (self.BallX<=0):
            PongLocal2P.ColorDefine(self)
            self.BallX = 120
            self.BallY = 75
            self.Horizontal = False
            self.PuntosPlayerTwo += 1
        #Concional de ganador
        if (self.PuntosPlayerOne==5 or self.PuntosPlayerTwo==5):
            if (self.PuntosPlayerOne==5):
                self.MensajeGanador = "Player ONE win \n\n\n\n R = Reset\n X = Return to Menu\n ESC = Exit"
            if (self.PuntosPlayerTwo==5):
                self.MensajeGanador = "Player TWO win \n\n\n\n R = Reset\n X = Return to Menu\n ESC = Exit"
            pyxel.flip()
            self.Velocity = 0
            self.PASOS = 0
            self.BallX = 120
            self.BallY = 75
            self.OnePlayerY = 63
            self.TwoPlayerY = 63
            if (pyxel.btn(pyxel.KEY_R)):
                self.Score = 0
                self.PuntosPlayerOne = 0
                self.PuntosPlayerTwo = 0
                self.MensajeGanador = ""
                self.PASOS = 4
                self.Velocity = 3
                self.OnePlayerY = 63
                self.TwoPlayerY = 63
            if (pyxel.btn(pyxel.KEY_X)):
                pyxel.quit()
                Menu()
        #TocaBordes Inferior y Superior
        if (self.BallY>=150):
            self.Vertical = True
        if (self.BallY<=0):
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
        #Update position players
        self.PlayerOne.y = self.OnePlayerY
        self.PlayerTwo.y = self.TwoPlayerY
        #Update position ball
        self.BallDetails.x = self.BallX
        self.BallDetails.y = self.BallY
        #Collsions
        if self.PlayerOne.is_colliding(self.BallDetails):
            self.Horizontal = False
            self.Score += 5
        if self.PlayerTwo.is_colliding(self.BallDetails):
            self.Horizontal = True
            self.Score += 5

    def draw(self):
        pyxel.cls(self.ColorBG)
        pyxel.line(120,0,120,150,self.ColorObjectsBG)
        pyxel.text(95,60,str(self.MensajeGanador),self.ColorObjectsBG)
        pyxel.text(105,10,"Score: "+str(self.Score),self.ColorObjectsBG)
        pyxel.text(15,10,str(self.PuntosPlayerOne),self.ColorObjectsBG)
        pyxel.text(220,10,str(self.PuntosPlayerTwo),self.ColorObjectsBG)
        pyxel.rect(15,self.OnePlayerY,4,25,self.ColorObjects)
        pyxel.rect(220,self.TwoPlayerY,4,25,self.ColorObjects)
        pyxel.circ(self.BallX,self.BallY,2,self.ColorObjects)
        pyxel.text(100,100,str(self.Usuario),7)
        """if (self.Usuario == None):
            pyxel.text(100,100,self.ConexionMensaje,7)
            self.EncontrarCliente()"""
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
