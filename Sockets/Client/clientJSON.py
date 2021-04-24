import pyxel
import random
import socket
import threading
import json

STEPS = 1.5

class Conection():
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        self.threadConection = threading.Thread(target=self.connect)
        self.threadConection.start()
        
        self.my = {
            "pos" : [0,0],
        }
        self.other = {
            "pos" : [0,0],
        }
    def connect(self):
        print('Conectando...')
        self.sock.connect(('localhost', 8000))
        print('Conexion establecida con exito!')
        while (True):
            # RECIBIR DATOS
            response = self.sock.recv(1024).decode()
            self.other = json.loads(response)
            # ENVIAR DATOS
            self.sock.send(json.dumps(self.my).encode())
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
            self.client = Conection()
            self.online = True
            self.otherPlayer = Cube(pyxel.width/2,pyxel.height/2)
            
        if (self.online):

            self.client.my["pos"][0] = self.player.pos[0]
            self.client.my["pos"][1] = self.player.pos[1]  
            
            self.otherPlayer.pos[0] = self.client.other["pos"][0]
            self.otherPlayer.pos[1] = self.client.other["pos"][1]
        
    def draw(self):
        pyxel.cls(pyxel.COLOR_LIME)
        self.player.draw()
        if (self.online):
            self.otherPlayer.draw()
            
    def keyboardUpdate(self):
        if (pyxel.btn(pyxel.KEY_A)): self.player.pos[0] -= STEPS
        if (pyxel.btn(pyxel.KEY_W)): self.player.pos[1] -= STEPS
        if (pyxel.btn(pyxel.KEY_D)): self.player.pos[0] += STEPS
        if (pyxel.btn(pyxel.KEY_S)): self.player.pos[1] += STEPS

Game()