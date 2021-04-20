import pyxel
import random
import socket

STEPS = 1

class Conection():
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_address = ('localhost', 4567)
        print('starting up on {} port {}'.format(*self.server_address))
        self.sock.bind(self.server_address)

    def update(self):
        self.sock.listen(1)
        # Wait for a connection
        print('waiting for a connection')
        connection, client_address = self.sock.accept()
        try:
            print('connection from', client_address)
            # Receive the data in small chunks and retransmit it
            data = connection.recv(16)
            print('received {!r}'.format(data))
            if data:
                print('sending data back to the client')
                connection.sendall(data)
            else:
                print('no data from', client_address)
        finally:
            # Clean up the connection
            connection.close()

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
        self.server = Conection()
        pyxel.run(self.update,self.draw)
        
    def update(self):
        self.keyboardUpdate()
        self.server.update()
        
    def draw(self):
        pyxel.cls(pyxel.COLOR_LIME)
        self.player.draw()

    def keyboardUpdate(self):
        if (pyxel.btn(pyxel.KEY_A)): self.player.x -= STEPS
        if (pyxel.btn(pyxel.KEY_W)): self.player.y -= STEPS
        if (pyxel.btn(pyxel.KEY_D)): self.player.x += STEPS
        if (pyxel.btn(pyxel.KEY_S)): self.player.y += STEPS

Game()