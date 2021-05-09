import pyxel
from buttons import Button

class Game():
    def __init__(self):
        pyxel.init(180,120,caption= "Keymusic Py",scale=4)
        self.keys = [
            Button([11,3],[20,100],4,[0,1,"A2"],pyxel.KEY_A),
            Button([10,9],[40,100],4,[1,2,"B2"],pyxel.KEY_S),
            Button([12,5],[60,100],4,[2,3,"C2"],pyxel.KEY_F),
            Button([15,14],[80,100],4,[3,4,"D2"],pyxel.KEY_G),
        ]
        pyxel.run(self.update,self.draw)
    def update(self):
        for button in self.keys:
            button.update()
    def draw(self):
        pyxel.cls(0)
        for button in self.keys:
            button.draw()
            # a
Game()