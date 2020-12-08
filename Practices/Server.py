import socket

mySocket = socket.socket()
mySocket.bind(('localhost',8080))
mySocket.listen(5)

while(True):
    conexion, addr = mySocket.accept()
    print("Nueva conexion establecida")
    print(addr)

    Mensaje = conexion.recv(1024)
    print(Mensaje.decode())

    conexion.send("Hola desde el sv".encode())
    conexion.close()
