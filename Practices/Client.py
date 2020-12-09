import threading
import socket

Host = "192.168.0.105"
Port = 8080
Comunicacion = socket.socket()
Comunicacion.connect((Host,Port))
Texto = Comunicacion.recv(1024).decode()
print (str(Texto))