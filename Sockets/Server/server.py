import pyxel
import random
import socket
import threading

STEPS = 1.5

class Conection():
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind(('localhost', 8000))
        self.sock.listen(1)
        print('Escuchando...')
        self.threadConection = threading.Thread(target=self.newConexion)
        self.threadConection.start()
        
        self.state = False
        self.myPos = [0,0]
        
    def update(self):
        pass
        
    def newConexion(self):
        while (True):
            conexion, addr = self.sock.accept()
            print('Nueva conexion {}'.format(addr))
            self.state = True
            while (True):
                conexion.send('{} {}'.format(self.myPos[0],self.myPos[1]).encode())
            
class Cube():
    def __init__(self,x,y):
        self.pos = [x,y]
        self.col = random.randint(0,15)
    def draw(self):
        pyxel.rect(self.pos[0],self.pos[1],2,2,self.col)
        
class Game():
    def __init__(self):
        pyxel.init(180,120)
        self.player = Cube(pyxel.width/2,pyxel.height/2)
        self.server = Conection()
        self.online = False
        pyxel.run(self.update,self.draw)
        
    def update(self):
        self.keyboardUpdate()
        if (self.server.state == True):
            self.online = True
            self.server.state = False
            self.otherPlayer = Cube(pyxel.width/2,pyxel.height/2)
            
        if (self.online):
            self.server.myPos[0] = self.player.pos[0]
            self.server.myPos[1] = self.player.pos[1]
        
    def draw(self):
        pyxel.cls(pyxel.COLOR_LIME)
        self.player.draw()
        if (self.server.state):
            self.otherPlayer.draw()
        
    def keyboardUpdate(self):
        if (pyxel.btn(pyxel.KEY_A)): self.player.pos[0] -= STEPS
        if (pyxel.btn(pyxel.KEY_W)): self.player.pos[1] -= STEPS
        if (pyxel.btn(pyxel.KEY_D)): self.player.pos[0] += STEPS
        if (pyxel.btn(pyxel.KEY_S)): self.player.pos[1] += STEPS

Game()