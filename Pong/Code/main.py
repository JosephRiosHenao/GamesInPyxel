import pyxel

class Pong:
    def __init__(self):
        self.OnePlayerY = 63
        self.TwoPlayerY = 63
        self.BallX = 126
        self.BallY = 87
        self.Score = 0
        self.PASOS = 2
        pyxel.init(240,150,caption="PongGame",)
        pyxel.run(self.update,self.draw)
    def update(self):
        if (pyxel.btn(pyxel.KEY_W) and self.OnePlayerY>0):
            self.OnePlayerY -= self.PASOS
        if (pyxel.btn(pyxel.KEY_S) and self.OnePlayerY<125):
            self.OnePlayerY += self.PASOS

        if (pyxel.btn(pyxel.KEY_UP) and self.TwoPlayerY>0):
            self.TwoPlayerY -= self.PASOS
        if (pyxel.btn(pyxel.KEY_DOWN) and self.TwoPlayerY<125):
            self.TwoPlayerY += self.PASOS

    def draw(self):
        pyxel.cls(0)
        pyxel.text(10,10,str(self.TwoPlayerY),1)
        pyxel.rect(0,75,240,1,2)
        pyxel.rect(15,self.OnePlayerY,4,25,7)
        pyxel.rect(220,self.TwoPlayerY,4,25,7)
Pong()