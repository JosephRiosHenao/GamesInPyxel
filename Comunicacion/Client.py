import socket
import pyxel
import threading

class App:
    def __init__(self):
        self.Player1Y = 100
        self.Player2Y = 100
        self.Online = False
        self.ConfigurarCliente()
        #pyxel.mouse(True)
        pyxel.init(200,200)
        pyxel.run(self.update,self.draw)
    def update(self):
        if(pyxel.btn(pyxel.KEY_UP)):
            self.Player2Y -= 2

        if(pyxel.btn(pyxel.KEY_DOWN)):
            self.Player2Y += 2

        if(self.Online == False):
            if(pyxel.btnr(pyxel.KEY_0)):
                self.t1 = threading.Thread(target = self.Conectar()).start()

                #t2 = threading.Thread(target = self.RecibirDatos()).start()
                self.Online = True
        if(pyxel.btnr(pyxel.KEY_Q)):
            self.Cliente.close()
            self.Online = False

        if(self.Online == True):
            self.ComunicacionBasica()
            #self.Comunicacion = threading.Thread(target = self.ComunicacionBasica(), daemon = True).start()
            #Comunicacion.start()


    def draw(self):
        pyxel.cls(7)
        pyxel.rect(190,self.Player2Y,5,5,0)
        pyxel.rect(10,self.Player1Y,5,5,0)

    def ConfigurarCliente(self):
        self.Cliente = socket.socket()

    def Conectar(self):
        self.NombreDeLaMaquina  = socket.gethostname()
        self.IP = "192.168.0.105"#socket.gethostbyname(self.NombreDeLaMaquina) 
        self.Cliente.connect((self.IP,8080))

    def RecibirDatos(self):
        self.Player1Y = int(self.Cliente.recv(1000).decode('utf-8'))

    def EnviarDatos(self):
        self.Cliente.send(str(self.Player2Y).encode('utf-8'))

    def ComunicacionBasica(self):
        while(self.Online):
            self.RecibirDatos()
            self.EnviarDatos()
App()
