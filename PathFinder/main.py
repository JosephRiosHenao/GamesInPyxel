import pyxel
import pathsController

class Game():
    def __init__(self):
        self.manager = pathsController.Controller()
        pyxel.init(192,128)
        pyxel.mouse(True)
        pyxel.run(self.update, self.draw)
    def update(self):
        self.manager.update()
    def draw(self):
        self.manager.draw()

if __name__ == '__main__':
    print("Init game...")
    Game()
    