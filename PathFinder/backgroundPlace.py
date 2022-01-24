from importlib.resources import path
from path import Path
import math
import settings
class Engine():
    def __init__(self):
        self.paths = [Path(0,0)]
        self.separateX = settings.initConfig["width"]/settings.initConfig["scaleBG"]
        self.separateY = settings.initConfig["height"]/settings.initConfig["scaleBG"]
    def calculate(self,oldPath):
        newPath = Path(oldPath.info["pos"][0]+settings.initConfig["scaleBG"],oldPath.info["pos"][1]+settings.initConfig["scaleBG"])
        self.paths.append(newPath)
    def place(self):
        for i in range(1,math.floor(self.separateY+self.separateY)):
            self.calculate(self.paths[i-1])
            print("Path created in (",self.paths[i].info["pos"][0],",",self.paths[i].info["pos"][1],")")
        return self.paths
            