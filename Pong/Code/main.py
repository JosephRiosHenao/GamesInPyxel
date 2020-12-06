import pyxel

class Pong:
    def __init__(self):
        self.OnePlayerY = 63
        self.TwoPlayerY = 63
        self.BallX = 120
        self.BallY = 75
        self.Velocity = 3
        self.Score = 0
        self.Horizontal = True
        self.Vertical = False
        self.PASOS = 2
        pyxel.init(240,150,caption="PongGame",)
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

        #Movimiento Prueba1
        if (self.BallX>=240):
            self.Horizontal = True
        if (self.BallX<=0):
            self.Horizontal = False
        if (self.BallY>=150):
            self.Vertical = True
        if (self.BallY<=0):
            self.Vertical = False

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

        if (self.OrientacionX==True and self.Horizontal==True):
            self.BallX -= self.Velocity
        if (self.OrientacionX==False and self.Horizontal==False):
            self.BallX += self.Velocity
        if (self.OrientacionY==True and self.Vertical==True):    
            self.BallY -= self.Velocity
        if (self.OrientacionY==False and self.Vertical==False):
            self.BallY += self.Velocity


    def draw(self):
        pyxel.cls(0)
        pyxel.text(10,10,str(self.BallY),1)
        pyxel.text(20,20,str(self.BallX),1)
        pyxel.text(10,20,str(self.OrientacionY),1)
        pyxel.text(20,30,str(self.OrientacionX),1)

        pyxel.rect(0,75,240,1,2)
        pyxel.circ(self.BallX,self.BallY,2,3)
        pyxel.rect(15,self.OnePlayerY,4,25,7)
        pyxel.rect(220,self.TwoPlayerY,4,25,7)
Pong()