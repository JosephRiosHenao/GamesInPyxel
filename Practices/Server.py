
import threading
import socket

Conexion = socket.socket()
Host = '192.168.0.105'
Port = 8080
Conexion.bind((Host,Port))
Conexion.listen(1)


def Consultar():
    while(True):
        Usuario, adr = Conexion.accept()
        print("Nueva conexion...")
        print(str(adr))
        Usuario.send("hola".encode())
        print("Termino hilo")
        break

        
t1 = threading.Thread(name="Server", target= Consultar())
t1.start()
t1.join()
print("Termino Programa")