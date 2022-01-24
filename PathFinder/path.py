import pyxel
class Path():
    def __init__(self,x,y):
        self.info = {"pos": [x,y],
                    "scale": [0,0],
                    "color": 6}
    def update(self):
        pass
    def draw(self):
        pyxel.rectb(self.info["pos"][0],self.info["pos"][1],
                    self.info["scale"][0],self.info["scale"][1],self.info["color"]) 