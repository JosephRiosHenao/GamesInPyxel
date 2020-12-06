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
        self.OnePlayerY = 63
        self.TwoPlayerY = 63
        self.BallX = 120
        self.BallY = 75
        self.Velocity = 3
        self.Score = 0
        self.Horizontal = True
        self.Vertical = False
        self.PASOS = 4
        self.PlayerOne = Players(15,self.OnePlayerY,4,25)
        self.PlayerTwo = Players(220,self.TwoPlayerY,4,25)
        self.BallDetails = Ball(self.BallX,self.BallY,2,2)
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
            #self.Horizontal = True
            self.BallX = 120
            self.BallY = 75
        if (self.BallX<=0):
            #self.Horizontal = False
            self.BallX = 120
            self.BallY = 75
            
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

        #Update position players
        self.PlayerOne.y = self.OnePlayerY
        self.PlayerTwo.y = self.TwoPlayerY

        #Update position ball
        self.BallDetails.x = self.BallX
        self.BallDetails.y = self.BallY

        #Collsions
        if self.PlayerOne.is_colliding(self.BallDetails):
            self.Horizontal = False
        if self.PlayerTwo.is_colliding(self.BallDetails):
            self.Horizontal = True

    def draw(self):
        pyxel.cls(0)
        pyxel.rect(15,self.OnePlayerY,4,25,7)
        pyxel.rect(220,self.TwoPlayerY,4,25,7)
        pyxel.circ(self.BallX,self.BallY,2,7)

Pong() 