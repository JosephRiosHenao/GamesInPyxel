import pyxel

class PongGame:

    def __init__(self):
        pyxel.init(256,175,caption="Pong",quit_key=pyxel.KEY_ESCAPE,fps=30)
        self.xMouse = 0
        self.yMouse = 0  
        self.PlayerY = 0
        self.Gravity = 2
        self.jump = True
        self.GroundX = 0
        self.x = 0
        self.Skin = 0
        pyxel.load("FlappyResources.pyxres")
        pyxel.run(self.update,self.draw)

    def update(self):
        self.jump = True 
        self.xMouse = pyxel.mouse_x
        self.yMouse = pyxel.mouse_y
        if self.PlayerY<140:
            self.PlayerY += self.Gravity
        if (pyxel.btn(pyxel.KEY_SPACE) or pyxel.btn(pyxel.KEY_W) or pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.GAMEPAD_1_A))and self.jump and self.PlayerY>-5:
            i = 0
            while i<5:
                self.Skin = 16     
                self.PlayerY -= 1
                i = i+1
        else:
            self.GroundX += 5
            self.Skin = 0
        self.jump = False
        self.fps = str(pyxel.frame_count)
        self.x = (pyxel.frame_count % 276) - 128




    def draw(self):
        pyxel.cls(6)
        #pyxel.bltm(0,0,0,0,0,80,50,0)
        offset = pyxel.frame_count % 256
        for i in range(2):
            pyxel.blt(i * 256 - offset,151,0,0,16,256,24)
        pyxel.blt(25,self.PlayerY,0,self.Skin,0,16,16,0)
        pyxel.circ(self.xMouse,self.yMouse,1,0)


PongGame()
    