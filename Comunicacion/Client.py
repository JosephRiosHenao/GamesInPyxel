import socket
import pyxel
import threading

class App:
    def __init__(self):
        self.Player1Y = 100
        self.Player2Y = 100
        self.Online = False
        self.ConfigurarCliente()
        pyxel.init(200,200)
        pyxel.run(self.update,self.draw)
    def update(self):
        if(pyxel.btn(pyxel.KEY_UP)):
            self.Player2Y -= 2
        if(pyxel.btn(pyxel.KEY_DOWN)):
            self.Player2Y += 2
        if(self.Online == False):
            if(pyxel.btnr(pyxel.KEY_0)):
                t1 = threading.Thread(target = self.Conectar()).start()
                tr = threading.Thread(target = self.RecibirDatos(), daemon = True).start()
                #t2 = threading.Thread(target = self.RecibirDatos()).start()
                self.Online = True
        if(pyxel.btnr(pyxel.KEY_Q)):
            self.Cliente.close()
            self.Online = False

        if(self.Online == True):
            #tr = threading.Thread(target = self.RecibirDatos(), daemon = True).start()
            te = threading.Thread(target = self.EnviarDatos(), daemon = True).start()            
            #self.RecibirDatos()
            #self.EnviarDatos()


    def draw(self):
        pyxel.cls(7)
        pyxel.rect(190,self.Player2Y,5,5,0)
        pyxel.rect(10,self.Player1Y,5,5,0)

    def ConfigurarCliente(self):
        self.Cliente = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    def Conectar(self):
        
        self.NombreDeLaMaquina  = socket.gethostname()
        self.IP = "192.168.0.105"#socket.gethostbyname(self.NombreDeLaMaquina) 
        try:
            self.Cliente.connect((self.IP,1234))
        except ConnectionRefusedError:
            print("No se puede conectar")


    def RecibirDatos(self):
        while (self.Online == True):
            self.Player1Y = int(self.Cliente.recv(128).decode('utf-8'))

    def EnviarDatos(self):
        self.Cliente.send(str(self.Player2Y).encode('utf-8'))
        #
if  __name__ == "__main__":
    App()
