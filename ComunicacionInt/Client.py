#!/usr/bin/python
# -*- coding: utf-8 -*-

# Programa Cliente
# www.pythondiario.com

import socket

# Creando un socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecta el socket en el puerto cuando el servidor esté escuchando
server_address = ('localhost', 10000)
print ('conectando a %s puerto %s' % server_address)
sock.connect(server_address)
try:
    
    # Enviando datos
    message = 'Este es el mensaje.  Se repitio.'
    print ('enviando "%s"' % message)
    sock.sendall(message.encode())

    # Buscando respuesta
    amount_received = 0
    amount_expected = len(message)
    
    while amount_received < amount_expected:
        data = sock.recv(19).decode()
        amount_received += len(data)
        print ('recibiendo "%s"' % data)

finally:
    print ('cerrando socket')
    sock.close()