import socket
import threading
import json

class Conection():
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ip = socket.gethostbyname(socket.gethostname())
        self.sock.bind((str(self.ip), 8000))
        self.sock.listen(1)
        
        self.disconect = False
        self.port = str(self.sock.getsockname()[1])
        self.online = False
        
        self.threadConection = threading.Thread(target=self.newConexion)
        self.threadConection.start()
        
        self.my = {
            "name" : "player",
            "pos" : [0,0],
            "angle" : 0,
            "shoot" : 0,
            "heal" : 100
        }
        self.other = {
            "name" : "player",
            "pos" : [0,0],
            "angle" : 0,
            "shoot" : 0,
            "heal" : 100
        }
        
    def newConexion(self):
        print('Escuchando...')
        while (self.disconect == False):
            conexion, addr = self.sock.accept()
            print('Nueva conexion {}'.format(addr))
            self.online = True
            while (self.disconect == False):
                #ENVIAR DATOS
                conexion.send(json.dumps(self.my).encode())
                # RECIBIR DATOS
                response = conexion.recv(1024).decode()
                self.other = json.loads(response)     
                if (self.disconect):
                    conexion.close()
        print('Desconectado')
    
    def closeConection(self):
        self.disconect = True
