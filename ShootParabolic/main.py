# IMPORTAMOS LIBRERIAS
import pyxel #
import random
import math
import time
import tabulate
import os 
import enum

class TypeSimulator(enum.Enum):
    Simulator     = 0
    SimulatorData = 1
    
G           = 9.81
PYXELWIDHT  = 0.1    

class Pixel():
    def __init__(self,x,y,col):
        self.x   = x
        self.y   = y
        self.col = col
    def draw(self):
        pyxel.pset(self.x,self.y,self.col)
class BallMathV():
    #-----------------------------------------------------------------------------------------------------------------------------
    def __init__(self,x,y,r,col,a,xMax): # CONSTRUCTOR DEL OBJETO DE PELOTA RESPECTO A DATOS INSUFICIENTES
        # INICIALIZANDO VARIABLES DE NUESTRO OBJETO
        self.x    = x     # X ubicacion 
        self.xi   = x     # X ubicancion para determinar posicion incial
        self.y    = y     # Y ubicacion 
        self.yi   = y     # Y ubicacion para determinar altura inicial
        self.a    = a     # Angulo
        self.xMax = xMax  # Distancia total recorrida
        self.t    = 0     # Restablecemos tiempo
        self.r    = r     # Radio
        self.col  = col   # Color
        # INICIALIZANDO OTROS FACTORES INDEPENDIENTES
        self.listPixel      = []                     # Lista de objetos que almacena el recorrido de la trayectoria
        self.starting_point = time.time()            # Calcula el tiempo respecto a la inicializacion del objeto
        self.dif            = pyxel.height - self.yi # Calcula la diferencia del objeto respecto al suelo
        # CALCULAMOS DATOS
        # Velocidad Inicial = hipotenusa o Fuerza lanzamiento respuesta a problema
        self.vi     = round( math.sqrt(((G)*self.xMax)/math.sin(math.radians(2*self.a))),2)
        # DATOS COMPLEMENTARIOS
        self.viY    = round( math.sin(math.radians(self.a))*self.vi,2 ) # Velocidad Inicial Y - Componente rectangular Y
        self.vX     = round( math.cos(math.radians(self.a))*self.vi,2 ) # Velocidad vector X constante - Componente rectangular X
        self.ts     = round( self.viY/G,2 )                             # Tiempo de subida al punto mas alto
        self.yMax   = round( math.pow(self.viY,2)/(2*(G)),2 )           # Altura maxima alcanzada
        self.tTotal = round( 2*self.ts,2 )                              # Tiempo total de vuelo, el doble de subida
        self.xTotal = round( self.vX*self.tTotal,2 )                    # Despazamiento en X total
        self.vFy    = round( (-G)*self.tTotal+9.19,2 )                  # Velocidad final Y - Componente rectangular Y
        self.vF     = round( self.vX + self.vFy,2 )                     # Velocidad final
    #-----------------------------------------------------------------------------------------------------------------------------
    def update(self): # METODO UPDATE QUE ACTUALIZA LA POSICION RESPECTO AL TIEMPO
        if self.t < self.tTotal: # CALCULAMOS SI PUEDE CALCULAR MAS TIEMPO, SIMULA LA GRAVEDAD EN FUNCION DEL TIEMPO
            self.elapsed_time = round(time.time()-self.starting_point,2) # Diferencia del tiempo actual con el de inicio
            self.t            = self.elapsed_time                        # Determinamos tiempo actual desde la creacion del balon
            # CALCULAMOS DESPLAZAMIENTO CON RELACION AL TIEMPO
            self.x = self.xi+self.vX*self.t                                                   # Calculando posixion en eje X
            self.y = (self.viY*self.t+(-1/2*G)*math.pow(self.t,2))*-1+(pyxel.height-self.dif) # Calucalndo posicion en eje Y
            # TRAYECTORIA
            self.listPixel.append(Pixel(self.x,self.y,self.col)) # Añade a la lista de objetos la posicion actual de trayectoria
    #-----------------------------------------------------------------------------------------------------------------------------
    def draw(self): # METODO DE DIBUJO DE PROYECTIL Y TRAYECTORIA
        pyxel.circ(self.x,self.y,self.r,self.col) # Dibujando proyectil respecto a la posicion calculada
        for pixel in self.listPixel:              # Iteramos sobre los objetos de la trayectoria    
            pixel.draw()                          # Dibujamos objeto en pantalla
        
class Ball():
        
    def __init__(self,x,y,r,col,a,vi):
        
        self.x = x # X ubicacion
        self.xi = x # X ubicancion para determinar posicion incial
        self.y = y # Y ubicacion
        self.yi = y # Y ubicacion para determinar altura inicial
        
        self.a = a # Angulo
        self.vi = vi # Velocidad Inicial = hipotenusa - Fuerza lanzamiento
                
        self.t = 0
        self.starting_point = time.time() # Tiempo
        
        self.r = r # Radio
        self.col = col # Color
        
        self.dif = + pyxel.height - self.yi
        
        self.listPixel = []
        
        self.starting_point = time.time() # Tiempo

        self.viY = round((math.sin(math.radians(self.a)))*self.vi,2) # Velocidad Inicial Y
        self.vX = round((math.cos(math.radians(self.a)))*self.vi,2) # Velocidad vector X constante
        self.ts = round(self.viY/G,2)  # Tiempo de subida al punto mas alto, multiplico por -1 por el signo
        self.yMax = round(math.pow(self.viY,2) / (2 * (G)),2)  # Altura maxima alcanzada
        self.tTotal = round(2*self.ts,2) # Tiempo total de vuelo el doble de subida
        self.xTotal = round(self.vX*self.tTotal,2) # Despazamiento en X total
        self.vFy = round((-G)*self.tTotal + 9.19,2)
        self.vF = round(self.vX + self.vFy,2)
        
        # print("---------------------DATOS--------------------")
        # print("Velocidad inicial:",self.vi,"m/s")
        # print("Componente rectangular Y inicial:",self.viY,"m/s")
        # print("Componente rectangular X constante:",self.vX,"m/s")
        # print("Altura maxima:",self.yMax,"m")
        # print("Tiempo para altura maxima:",self.ts,"s")
        # print("Tiempo total de vuelo:",self.tTotal,"s")
        # print("Dezplazamiento total:",self.xTotal,"m")
        # print("Velocidad final:",self.vF,"m/s")
        # print("Componente rectangular Y final:",self.vFy,"m/s")
        # print("----------------------------------------------")

        
        
    def update(self):
        
        if self.t < self.tTotal:
            self.elapsed_time = round(time.time () - self.starting_point,2)
            self.t = self.elapsed_time
            
            self.x = self.xi + self.vX * self.t # multiplica la constante por el timepo para saber la poscicion
            
            self.y = (self.viY*self.t+(-1/2)*G*math.pow(self.t,2))  * -1 + (pyxel.height - self.dif)
            
            self.listPixel.append(Pixel(self.x,self.y,self.col))


    def draw(self):
        pyxel.circ(self.x,self.y,self.r,self.col) # Dibujando
        for pixel in self.listPixel:
            pixel.draw()
        
class Pitagoras():
    def __init__(self,Ax,Ay):
        
        self.ca = 0 # Adyaciente
        self.co = 0 # Opuesto
        self.h = 0 # hipotenusa
        
        self.A = 0 # AnguloHallar

        self.Ax = Ax # X Objeto
        self.Ay = Ay # Y Objeto
        
        self.Bx = 0 # X Superior
        self.By = 0 # Y Superor
        
        self.stateUP = True
        self.stateDOWN = True
        self.stateLEFT = True
        
        
    def update(self):
        self.Bx = pyxel.mouse_x # Capturando Posicion MouseX
        self.By = pyxel.mouse_y # Capturando Posicion MouseY
        #self.MouseXVelocity = -pyxel.mouse_x*0.2 # Mejorando presicion de velocidad actual: 38.2
        
        self.ca = self.Bx - self.Ax # Hallar tamaño de cateto adyaciente (Mouse - Triangulo)
        self.co = self.Ay - self.By # Hallar tamaño de cateto opuesto (Triangulo - mouse)
        self.h = round(math.sqrt(math.pow(self.ca, 2) + math.pow(self.co, 2)),2) # Hallar hipotenusa
        try:
            self.A = round(math.degrees(math.atan((self.co/self.ca))),2) # Angulo
        except ZeroDivisionError as e:
            self.A = 90.00
        
        if (pyxel.btnp(pyxel.KEY_UP)):
            self.stateUP = not(self.stateUP)
        if (pyxel.btnp(pyxel.KEY_LEFT)):
            self.stateLEFT = not(self.stateLEFT)
        if (pyxel.btnp(pyxel.KEY_DOWN)):
            self.stateDOWN = not(self.stateDOWN)
            
            
        
    def draw(self):
        if self.stateUP: pyxel.line(self.Ax,self.Ay,self.Bx,self.By,15) # Hipotenusa
        if self.stateLEFT: pyxel.line(self.Ax,self.Ay,self.Bx,self.Ay,14) # Adyacente
        if self.stateDOWN: pyxel.line(self.Bx,self.Ay,self.Bx,self.By,13) # Opuesto
        
class App():
    

    def __init__(self):
        self.clearConsole()
        inputState = input("Desea usar el simulador? y/n:  ")
        if inputState == "y": self.state = TypeSimulator.Simulator
        else: self.state = TypeSimulator.SimulatorData
        pyxel.init( width      = 192,
                    height     = 128,
                    caption    = "MoveParabolist",
                    fps        = 60,
                    fullscreen = False )
        
        self.listBalls = []
        self.Triangulo = Pitagoras(10,120) 
        self.Data = [
            ["a","V0 (m/s)","V0y (m/s)","V0x (m/s)","Ymax (m)","Ts (seg)","Tmax (seg)","Xmax (m)","Vf (m/s)","Vfy (m/s)"]
        ]    
        
        pyxel.run(self.update,self.draw)
        
    def update(self):
        self.checkInput()
        if self.state == TypeSimulator.Simulator: self.Triangulo.update()
        for ball in self.listBalls:
            ball.update()
    
    def draw (self):
        
        pyxel.cls(0) # Fondo
        
        for ball in self.listBalls: # Array de objetos
            ball.draw() # Dibujar Objeto
        if self.state == TypeSimulator.Simulator:
            self.Triangulo.draw()
            pyxel.text(5,5,"Angulo: "+str(self.Triangulo.A)+"°",15)
            pyxel.text(5,10,"Fuerza: "+str(self.Triangulo.h)+"m/s",15)

    
    def checkInput(self): 
        if (pyxel.btnp(pyxel.KEY_SPACE)):
            if self.state == TypeSimulator.SimulatorData:
                self.clearConsole()
                self.aInput = float(input("Digite el angulo de disparo: "))
                self.XmaxInput = float(input("Digite la distancia(m): ")) 
            self.generateBall() # Space -> generar bola
        if (pyxel.btnp(pyxel.KEY_R)): self.clearListBall() # R -> Resetear todo
        
    def generateBall(self):
        color = random.randint(1, 14) # Colores random
        
        if self.state == TypeSimulator.Simulator: self.listBalls.append(Ball(10,120,2,color,self.Triangulo.A,self.Triangulo.h)) # Agregar objecto a la lista
        else: self.listBalls.append(BallMathV(10,120,2,color,self.aInput,self.XmaxInput)) # Agregar objecto a la lista

        
        if len(self.listBalls)==0:    
            self.Data.append([self.listBalls[0].a,self.listBalls[0].vi,self.listBalls[0].viY,self.listBalls[0].vX,
                            self.listBalls[0].yMax,self.listBalls[0].ts,self.listBalls[0].tTotal,
                            self.listBalls[0].xTotal,self.listBalls[0].vF,self.listBalls[0].vFy])
        else:
            self.Data.append([self.listBalls[-1].a,self.listBalls[-1].vi,self.listBalls[-1].viY,self.listBalls[-1].vX,
                            self.listBalls[-1].yMax,self.listBalls[-1].ts,self.listBalls[-1].tTotal,
                            self.listBalls[-1].xTotal,self.listBalls[-1].vF,self.listBalls[-1].vFy])
        self.clearConsole()
        print(tabulate.tabulate(self.Data,headers="firstrow",showindex=True,tablefmt="fancy_grid",numalign="center"))

        

    def clearListBall(self):
        self.listBalls.clear() # Limpiar lista de objetos
        self.Data.clear()
        self.clearConsole()
        self.Data = [
            ["a","V0 (m/s)","V0y (m/s)","V0x (m/s)","Ymax (m)","Ts (seg)","Tmax (seg)","Xmax (m)","Vf (m/s)","Vfy (m/s)"]
        ]
        print(tabulate.tabulate(self.Data,headers="firstrow",showindex=True,tablefmt="fancy_grid",numalign="center"))

    
    def clearConsole(self):
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
            


App()