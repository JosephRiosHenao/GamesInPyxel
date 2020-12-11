import socket
import pyxel
import threading

class App:

    def __init__(self):
        self.Player1Y = 100
        self.Player2Y = 100
        self.Online = False
        self.ConfigurarServer()
        pyxel.init(200,200)
        pyxel.run(self.update,self.draw)

    def update(self):
        if(pyxel.btn(pyxel.KEY_W)):
            self.Player1Y -= 2

        if(pyxel.btn(pyxel.KEY_S)):
            self.Player1Y += 2
        if (self.Online == False):
            if(pyxel.btnr(pyxel.KEY_0)):
                t1 = threading.Thread(target=self.AceptarCliente()).start()
                self.Online = True

            if(pyxel.btnr(pyxel.KEY_Q)):
                self.Cliente.close()
                self.Online = False

            if (self.Online == True):
                #self.RecibirDatos()
                self.EnviarDatos()

    def draw(self):
        pyxel.cls(0)
        pyxel.rect(10,self.Player1Y,5,5,7)
        pyxel.rect(90,self.Player2Y,5,5,7)

    def ConfigurarServer(self):
        self.NombreDeLaMaquina = socket.gethostname()
        self.HOST = socket.gethostbyname(self.NombreDeLaMaquina)
        print(self.HOST)
        self.Server = socket.socket()
        self.Server.bind((self.HOST,8080))
        self.Server.listen(1)
        
    def AceptarCliente(self):
        self.Cliente, adr = self.Server.accept()

    #def RecibirDatos(self):
    #    self.Player2Y = int(self.Cliente.recv(1024).decode('utf-8'))
    
    def EnviarDatos(self):
        self.Cliente.send(str(self.Player1Y).encode())


App()