import pyxel
import math
import random

SEPARATE = 3


class Game():
    def __init__(self):
        self.paths = self.calculate()
        pyxel.init(192,128)
        pyxel.run(self.update, self.draw)
    def update(self):
        pass
    def draw(self):
        for path in self.paths:
            pyxel.rectb(path[0],path[1],SEPARATE,SEPARATE,random.randint(0,11))
    def calculate(self):
        newPaths = []
        for y in range(math.floor(128/SEPARATE)):
            for x in range(math.floor(192/SEPARATE)):
                newPaths.append([x*SEPARATE,y*SEPARATE])
        return newPaths
    
Game()