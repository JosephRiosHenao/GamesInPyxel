import socket
import threading
import json

class Conection():
    def __init__(self,ip,port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        self.ip = ip
        self.port = port
        self.online = False
        
        self.threadConection = threading.Thread(target=self.connect)
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
        
    def connect(self):
        print('Conectando...')
        self.sock.connect((str(self.ip),self.port))
        print('Conexion establecida con exito!')
        self.online = True
        while (True):
            # RECIBIR DATOS
            response = self.sock.recv(1024).decode()
            self.other = json.loads(response)
            # ENVIAR DATOS
            self.sock.send(json.dumps(self.my).encode())
