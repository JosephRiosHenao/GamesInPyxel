from path import Path
import math
from settings import CONFIG

class Controller():
    def __init__(self):
        self.paths = self.generatePaths()
    def generatePaths(self):
        newPaths = []
        for y in range(math.floor(128/CONFIG["scaleBG"])):
            for x in range(math.floor(192/CONFIG["scaleBG"])):
                newPaths.append(Path(x*CONFIG["scaleBG"],y*CONFIG["scaleBG"]))
        return newPaths
    def draw(self):
        for path in self.paths:
            path.draw()