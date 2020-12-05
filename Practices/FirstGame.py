import pyxel

class PongGame:

    def __init__(self):
        pyxel.init(256,175,caption="Pong",quit_key=pyxel.KEY_ESCAPE)
        self.x = 0;
        self.y = 0;
        #pyxel.show()
        pyxel.run(self.update,self.draw)

    def update(self):
        self.x = (self.x +1) % pyxel.width
        self.y = (self.y +1) % pyxel.height
        self.xMouse = pyxel.mouse_x
        self.yMouse = pyxel.mouse_y
    
    def draw(self):
        pyxel.cls(7)
        pyxel.rect(self.x,self.y,8,8,9)
        pyxel.circ(self.xMouse,self.yMouse,1,0)



PongGame()
    