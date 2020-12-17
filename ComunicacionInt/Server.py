
#!/usr/bin/python
# -*- coding: utf-8 -*-

# Programa Servidor
# www.pythondiario.com

import socket

# Creando el socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Enlace de socket y puerto
server_address = ('localhost', 10000)
print ('empezando a levantar %s puerto %s' % server_address)
sock.bind(server_address)

# Escuchando conexiones entrantes
sock.listen(1)

while True:
    # Esperando conexion
    print ('Esperando para conectarse')
    connection, client_address = sock.accept()

    try:
        print ('concexion desde', client_address)

        # Recibe los datos en trozos y reetransmite
        while True:
            data = connection.recv(19).decode()
            print ('recibido "%s"' % data)
            if data:
                print ('enviando mensaje de vuelta al cliente')
                connection.sendall(data.encode())
            else:
                print ('no hay mas datos', client_address)
                break
            
    finally:
        # Cerrando conexion
        connection.close()