import pyxel
import KeyboardStateGame
class Game():
    def __init__(self):
        pyxel.init(
            width=192,
            height=128,
            caption='Painxelt',
            fps=60,
            scale=3
        )
        self.state = 0
    def init(self): 
        pyxel.run(self.update,self.draw)
    def update(self):
        self.state = KeyboardStateGame.Keyboard().detect()
        if self.state == 0:
            pass
    def draw(self):
        if self.state == 0:
            pyxel.cls(8)
        if self.state == 1:
            pyxel.cls(6)

if(__name__ == "__main__"):
    print("Ejecutando...")
    game = Game()
    game.init()
else:
    print("Error de ejecucion, archivo mal iniciado")