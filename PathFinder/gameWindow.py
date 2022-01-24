import pyxel
import settings
import pathsController

class Game():
    def __init__(self):
        print("Juego iniciado!")
        self.paths = pathsController.Paths()
    def start(self):
        pyxel.init( width=settings.initConfig["width"],
                    height=settings.initConfig["height"],
                    caption=settings.initConfig["caption"],
                    fps=settings.initConfig["fps"],
                    scale=settings.initConfig["scale"])
        pyxel.run(self.update,self.draw)
    def update(self):
        self.paths.update()
    def draw(self):
        pyxel.cls(5 )
        self.paths.draw()
    