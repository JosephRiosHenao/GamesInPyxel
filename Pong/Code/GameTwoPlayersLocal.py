import pyxel

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

class Pong:
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
        pyxel.init(240,150,caption="PongGame",fullscreen=True)
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
            Pong.ColorDefine(self)
            self.BallX = 120
            self.BallY = 75
            self.Horizontal = True
            self.PuntosPlayerOne += 1
        #TocaBordeIzquierdo
        if (self.BallX<=0):
            Pong.ColorDefine(self)
            self.BallX = 120
            self.BallY = 75
            self.Horizontal = False
            self.PuntosPlayerTwo += 1
        #Concional de ganador
        if (self.PuntosPlayerOne==5 or self.PuntosPlayerTwo==5):
            if (self.PuntosPlayerOne==5):
                self.MensajeGanador = "Player ONE win \n\n\n\n R = Reset\n ESC = Exit"
            if (self.PuntosPlayerTwo==5):
                self.MensajeGanador = "Player TWO win \n\n\n\n R = Reset\n ESC = Exit"
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
Pong()
