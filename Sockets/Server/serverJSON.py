import pyxel
import random
import socket
import threading
import json

STEPS = 1.5

class Conection():
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind(('localhost', 8000))
        self.sock.listen(1)
        
        self.threadConection = threading.Thread(target=self.newConexion)
        self.threadConection.start()
        
        self.my = {
            "pos" : [0,0],
        }
        self.other = {
            "pos" : [0,0],
        }
    def newConexion(self):
        print('Escuchando...')
        while (True):
            conexion, addr = self.sock.accept()
            print('Nueva conexion {}'.format(addr))
            while (True):
                # ENVIAR DATOS
                conexion.send(json.dumps(self.my).encode())
                # RECIBIR DATOS
                response = conexion.recv(1024).decode()
                self.other = json.loads(response)
class Cube():
    def __init__(self,x,y):
        self.pos = [x,y]
        self.col = random.randint(0,15)
    def draw(self):
        pyxel.rect(self.pos[0],self.pos[1],10,10,self.col)
        
class Game():
    def __init__(self):
        pyxel.init(180,120)
        self.player = Cube(pyxel.width/2,pyxel.height/2)
        self.online = False
        pyxel.run(self.update,self.draw)
        
    def update(self):
        self.keyboardUpdate()
        if (pyxel.btnp(pyxel.KEY_SPACE)):
            self.server = Conection()
            self.online = True
            self.otherPlayer = Cube(pyxel.width/2,pyxel.height/2)
            
        if (self.online):
            
            self.server.my["pos"][0] = self.player.pos[0]
            self.server.my["pos"][1] = self.player.pos[1]
            
            self.otherPlayer.pos[0] = self.server.other["pos"][0]
            self.otherPlayer.pos[1] = self.server.other["pos"][1]
        
    def draw(self):
        pyxel.cls(pyxel.COLOR_LIGHTBLUE)
        self.player.draw()
        if (self.online):
            self.otherPlayer.draw()
        
    def keyboardUpdate(self):
        if (pyxel.btn(pyxel.KEY_A)): self.player.pos[0] -= STEPS
        if (pyxel.btn(pyxel.KEY_W)): self.player.pos[1] -= STEPS
        if (pyxel.btn(pyxel.KEY_D)): self.player.pos[0] += STEPS
        if (pyxel.btn(pyxel.KEY_S)): self.player.pos[1] += STEPS

Game()