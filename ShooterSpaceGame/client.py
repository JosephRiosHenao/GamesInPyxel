import socket
import threading

class Conection():
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        self.threadConection = threading.Thread(target=self.connect)
        self.threadConection.start()
        
        self.myPos = [0,0]
        self.otherPos = [0,0]
        
    def connect(self):
        print('Conectando...')
        self.sock.connect(('localhost', 8000))
        print('Conexion establecida con exito!')
        while (True):
            # RECIBIR DATOS
            response = self.sock.recv(1024).decode()
            response = response.split('-')
            try:
                self.otherPos[0] = float(response[0])
                self.otherPos[1] = float(response[1])
            except: 
                try:
                    self.otherPos[0] = float(response[1])
                    self.otherPos[1] = float(response[2])
                except: 
                    print(response)
            
            # ENVIAR DATOS
            self.sock.send("{}-{}-".format(self.myPos[0],self.myPos[1]).encode())