import pyxel
import socket

# Crear servidor
class Server:
    def __init__(self):
        self.server = None
        self.client = None   
        self.client_address = None 
        self.client_port = None # Cliente conectado 
        self.client_socket = None # Socket del cliente
        self.client_socket_file = None # Socket del cliente

    def create_server(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(('', PORT))
        self.server.listen(1)
        self.client_socket, self.client_address = self.server.accept()
        self.client_socket_file = self.client_socket.makefile()
        self.client_port = self.client_address[1] 
        self.client_socket.setblocking(0)
        self.client_socket.settimeout(0.5)
        print("Cliente conectado desde: {}:{}".format(self.client_address[0], self.client_port))
        self.client = Client(self.client_socket_file, self.client_socket, self.client_address)
        self.client.start()
        self.client.join()
        self.client_socket.close()
        self.server.close()
        print("Server closed")


# Crear cliente
class Client:
    def __init__(self, client_socket_file, client_socket, client_address):
        self.client_socket_file = client_socket_file
        self.client_socket = client_socket
        self.client_address = client_address
        self.client_socket_file.write("HELICOPTER:CONNECTED\n")
        self.client_socket_file.flush()
        self.client_socket.setblocking(0)
        self.client_socket.settimeout(0.5)

    
    def start(self):
        while True:
            try:
                data = self.client_socket.recv(1024)
                if not data:
                    break
                self.client_socket_file.write(data)
                self.client_socket_file.flush()
            except socket.timeout:
                pass
            except socket.error:
                break
        self.client_socket.close()
        print("Client closed")
        pyxel.quit()
        sys.exit()