import socket

mySocket = socket.socket()
mySocket.connect(('localhost',8080))

mySocket.send("hola desde cliente".encode())
respuesta = mySocket.recv(1024)

print(respuesta.decode())
mySocket.close()