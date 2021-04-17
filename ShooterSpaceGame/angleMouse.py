import math
import pyxel

class Pitagoras(): # CLASE PARA DETERMINAR POSICION RESPECTO A 2 VECTORES, SIENDO UNO DE ELLOS EL MOUSE
    def __init__(self,Ax,Ay): # CONSTRUCTOR DEL OBJETO, POSICION DEL OBJECTO DEL PRIMER VECTOR
        # INICIALIZAMOS DATOS
        # LADOS DEL TRIANGULO
        self.ca = 0 # Adyaciente
        self.co = 0 # Opuesto
        self.h  = 0 # Hipotenusa
        # ANGULO DE TIRO
        self.A = 0 # AnguloHallar
        # POSICION DEL VECTOR 1
        self.Ax = Ax # X Objeto
        self.Ay = Ay # Y Objeto
        # POSICION DEL VECTOR 2
        self.Bx = 0 # X Superior
        self.By = 0 # Y Superor
        # ESTADOS DEL LOS LADOS DEL TRIANGULO A LA VISTA
        self.stateUP   = False # Visibilidad de la hipotenusa 
        self.stateDOWN = False # Visibilidad de la opuesta
        self.stateLEFT = False # Visibilidad de la adyacente
    #-----------------------------------------------------------------------------------------------------------------------------
    def update(self,Ax,Ay): # METODO UPDATE PARA DETERMINAR VALORES DEL TRIANGULO
        # POSICION DEL VECTOR 1
        self.Ax = Ax # X Objeto
        self.Ay = Ay # Y Objeto
        # ACTUALIZAMOS POSICION DEL VECTOR 2
        self.Bx = pyxel.mouse_x # Capturando Posicion MouseX
        self.By = pyxel.mouse_y # Capturando Posicion MouseY
        # CALCULAMOS LADOS DEL TRIANGULO
        self.ca = self.Bx-self.Ax                                                 # Hallar tamaño de cateto adyaciente
        self.co = self.Ay-self.By                                                 # Hallar tamaño de cateto opuesto
        self.h  = round(math.sqrt(math.pow(self.ca, 2) + math.pow(self.co, 2)),2) # Hallar hipotenusa
        # CALCULAMOS ANGULO A HALLAR CON UNA EXEPCION DE ERRORES PARA EL GRADO DE 90°
        try:                                                             # COMPROBAMOS POSIBLIDAD
            self.A = round(math.degrees(math.atan((self.co/self.ca))),2) # Calculamos angulo con razones trigonometricas tan(a)
        except ZeroDivisionError as e:                                   # EN CAOS DE ERROR
            self.A = 90.00                                               # El cateto adyacente es 0, por ende angulo es 90°
        # COMPROBAMOS EL ESTADO DEL TRIANGULO, SEGUN EL TECLADO
        if (pyxel.btnp(pyxel.KEY_UP)):   self.stateUP   = not(self.stateUP)   # Flecha arriba cambiamos estado hipotenusa
        if (pyxel.btnp(pyxel.KEY_LEFT)): self.stateLEFT = not(self.stateLEFT) # Flecha iaquierda cambiamos estado adyacente
        if (pyxel.btnp(pyxel.KEY_DOWN)): self.stateDOWN = not(self.stateDOWN) # Flecha abajo cambiamos estado de opuesto
        if (self.ca<0 and self.co>0): self.Angulo = self.A # CUADRANTE 2 OK
        if (self.ca>0 and self.co<0): self.Angulo = self.A + 180 # CUADRANTE 4 OK
        if (self.ca<0 and self.co<0): self.Angulo = self.A  # CUADRANTE 3 OK
        if (self.ca>0 and self.co>0): self.Angulo = self.A - 180 *-1 # CUADRANTE 1 OK
        self.angle = 270-self.Angulo
    #----------------------------------------------------------------------------------------------------------------------------
    def draw(self): # METODO QUE DIBUJA EL TRIANGULO
        if self.stateUP:   pyxel.line(self.Ax,self.Ay,self.Bx,self.By,15) # Dibuja hipotenusa
        if self.stateLEFT: pyxel.line(self.Ax,self.Ay,self.Bx,self.Ay,14) # Dibuja adyacente
        if self.stateDOWN: pyxel.line(self.Bx,self.Ay,self.Bx,self.By,13) # Dibuja opuesto
        # pyxel.text(10,10,str(270-self.Angulo),15)