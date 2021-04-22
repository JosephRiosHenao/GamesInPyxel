import pyxel
import buttons

class Menu():
    def __init__(self):
        self.buttons = [
            [ buttons.Button([pyxel.width,10 ],[20,10],[1,2,3],['HOLA 1',1] )], # LOCAL
            [ buttons.Button([pyxel.width,100],[20,10],[1,2,3],['HOLA 2',1] )], # SERVER
            [ buttons.Button([pyxel.width,150],[20,10],[1,2,3],['HOLA 3',1] )], # CLIENT
        ]
        
    def update(self):
        pass
        
    def draw(self):
        for target in self.buttons:
            target.draw()
            