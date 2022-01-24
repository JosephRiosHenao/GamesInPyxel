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
    def update(self):
        for path in self.paths:
            path.update()
            if path.stateMouse:
                self.distance(path)
            
    def draw(self):
        for path in self.paths:
            path.draw()
    def distance(self, path):
        for pathFinish in self.paths:
            distance = pathFinish.pos[0]-path.pos[0]
            print(distance)
            if (distance >= -20 and distance <= 20): pathFinish.distanceSet(0)
            