import threading
import socket
class App:

    def contar(self):
        while (True):
            self.Usuario, adr = self.Comunicacion.accept()
            self.conexion = True
            self.Usuario.send("Hola".encode)
    def __init__(self):
        self.Comunicacion = socket.socket
        self.Comunicacion.bind(('localhost',8080))
        self.conexion = False
        hilo1 = threading.Thread(name="Hilo LAN",target=self.contar())
        hilo1.start()
        while(self.conexion!=True):
            print("1")
"""import threading, time
class App:
    vmax_hilos = {}
    self.Comunicacion = socket.socket
    self.Comunicacion.bind(('localhost',8080))
    self.conexion = False
    def contar(segundos):
        #Contar hasta un límite de tiempo
        global vmax_hilos
        contador = 0
        inicial = time.time()
        limite = inicial + segundos
        nombre = threading.current_thread().getName()
        while inicial<=limite:
            contador+=1
            inicial = time.time()
            print(nombre, contador)
            self.Usuario, adr = self.Comunicacion.accept()
            self.conexion = True
            self.Usuario.send("Hola".encode)
        vmax_hilos[nombre] = contador
        if threading.active_count()==2:
            print(vmax_hilos)
            print(threading.enumerate())

    segundos = 60
    hilo = threading.Thread(name='hilo Conexion',
                                target=contar, 
                                args=(segundos,))
    hilo.start()
    while(self.conexion!=True):
        print("1")"""
App()
