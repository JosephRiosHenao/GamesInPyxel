import socket
import threading

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
        
        self.myPos = [0,0,0]
        self.otherPos = [0,0,0]
        
        
    def newConexion(self):
        print('Escuchando...')
        while (self.disconect == False):
            conexion, addr = self.sock.accept()
            print('Nueva conexion {}'.format(addr))
            self.online = True
            while (self.disconect == False):
                #ENVIAR DATOS
                conexion.send("{}-{}-{}-".format(self.myPos[0],self.myPos[1],self.myPos[2]).encode())
                
                # RECIBIR DATOS
                response = conexion.recv(1024).decode()
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
                if (self.disconect):
                    conexion.close()
        print('Desconectado')
    
    def closeConection(self):
        self.disconect = True
