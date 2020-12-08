import pyxel

class Menu:
    def __init__(self):
        pyxel.init(150,200,caption="MenuPrincipal",fullscreen=True)
        pyxel.mouse(True)
        pyxel.load(/Resources/BG.pyxres)
        pyxel.run(self.update,self.draw)
    def update(self):
        a = 0
    def draw(self):
        pyxel.cls(7)
        pyxel.bltm(0,0,0,0,0,100,100)
Menu()
