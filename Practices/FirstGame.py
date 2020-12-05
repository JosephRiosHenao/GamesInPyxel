import pyxel

class PongGame:

    def __init__(self):
        pyxel.init(256,175,caption="Pong",quit_key=pyxel.KEY_ESCAPE)
        self.x = 0;
        self.y = 0;  
        self.colorElegido = 0
        self.x1 = 0
        self.x2 = 0
        self.y1 = 0
        self.y2 = 0
        pyxel.load("FlappyResources.pyxres")
        pyxel.run(self.update,self.draw)

    def update(self):
        self.xMouse = pyxel.mouse_x
        self.yMouse = pyxel.mouse_y
        if pyxel.btn(pyxel.KEY_0):
            self.colorElegido = 0
        if pyxel.btn(pyxel.KEY_1):
            self.colorElegido = 1
        if pyxel.btn(pyxel.KEY_2):
            self.colorElegido = 2
        if pyxel.btn(pyxel.KEY_3):
            self.colorElegido = 3
        if pyxel.btn(pyxel.MOUSE_RIGHT_BUTTON):
            self.x1 = pyxel.mouse_x
            self.y1 = pyxel.mouse_y
        if pyxel.btn(pyxel.MOUSE_LEFT_BUTTON):
            self.x2 = pyxel.mouse_x
            self.y2 = pyxel.mouse_y
            

    def draw(self):
        pyxel.cls(7)
        pyxel.bltm(0,0,0,0,0,80,50,0)
        pyxel.blt(128,87,0,0,0,16,16,0)
        pyxel.line(self.x1,self.y1,self.x2,self.y2,self.colorElegido)
        pyxel.circ(self.xMouse,self.yMouse,1,self.colorElegido)



PongGame()
    