import pyxel
import pathsController

class Game():
    def __init__(self):
        self.manager = pathsController.Controller()
        pyxel.init(192,128)
        pyxel.run(self.update, self.draw)
    def update(self):
        pass
    def draw(self):
        self.manager.draw()

if __name__ == '__main__':
    print("Init game...")
    Game()
    