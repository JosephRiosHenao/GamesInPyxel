import pyxel
import random
import socket

STEPS = 1

class Conection():
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect(('localhost', 8000))
        print('Conectando...')
        
    def update(self):
        pass

class Cube():
    def __init__(self,x,y,r):
        self.x = x
        self.y = y
        self.r = r
        self.col = random.randint(0,15)
    def draw(self):
        pyxel.rect(self.x,self.y,self.r,self.r,self.col)
        
class Game():
    def __init__(self):
        pyxel.init(180,120)
        self.player = Cube(pyxel.width/2,pyxel.height/2,2)
        self.client = Conection()
        pyxel.run(self.update,self.draw)
        
    def update(self):
        self.keyboardUpdate()
        self.client.update()
        
    def draw(self):
        pyxel.cls(pyxel.COLOR_LIME)
        self.player.draw()

    def keyboardUpdate(self):
        if (pyxel.btn(pyxel.KEY_A)): self.player.x -= STEPS
        if (pyxel.btn(pyxel.KEY_W)): self.player.y -= STEPS
        if (pyxel.btn(pyxel.KEY_D)): self.player.x += STEPS
        if (pyxel.btn(pyxel.KEY_S)): self.player.y += STEPS

Game()