import socket
import threading

class Conection():
    def __init__(self,ip,port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        self.ip = ip
        self.port = port
        self.online = False
        
        self.threadConection = threading.Thread(target=self.connect)
        self.threadConection.start()
        
        self.myPos = [0,0,0]
        self.otherPos = [0,0,0]
        
    def connect(self):
        print('Conectando...')
        self.sock.connect((str(self.ip),self.port))
        print('Conexion establecida con exito!')
        self.online = True
        while (True):
            # RECIBIR DATOS
            response = self.sock.recv(1024).decode()
            response = response.split('-')
            try:
                self.otherPos[0] = float(response[0])
                self.otherPos[1] = float(response[1])
                self.otherPos[2] = float(response[2])
            except: 
                try:
                    self.otherPos[0] = float(response[1])
                    self.otherPos[1] = float(response[2])
                    self.otherPos[2] = float(response[3])
                except: 
                    print(response)
            
            # ENVIAR DATOS
            self.sock.send("{}-{}-{}-".format(self.myPos[0],self.myPos[1],self.myPos[2]).encode())