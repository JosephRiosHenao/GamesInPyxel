import pyxel

class App:
    def __init__(self):
        pyxel.init(160, 120, caption="Moving Character")
        pyxel.load("FlappyResources.pyxres")
        self.coconut = Coconut(20, 20)
        pyxel.run(self.update, self.draw)
    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        self.coconut.update()
    def draw(self):
        pyxel.cls(0)
        pyxel.blt(self.coconut.x,self.coconut.y,0,0,0,16,16) # (x, y, img, u, v, width, height)

class Coconut:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def update(self):
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.x += 2
        if pyxel.btn(pyxel.KEY_LEFT):
            self.x -= 2
        if pyxel.btn(pyxel.KEY_UP):
            self.y -= 2
        if pyxel.btn(pyxel.KEY_DOWN):
            self.y += 2


App()