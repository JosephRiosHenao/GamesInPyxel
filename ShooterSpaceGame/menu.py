import pyxel
import buttons

class Menu():
    def __init__(self):
        self.buttons = [
            buttons.Button([pyxel.width/2,80 ],[100,10],[1,2,3],['ENTRENAMIENTO LOCAL',pyxel.COLOR_WHITE] ), # LOCAL
            buttons.Button([pyxel.width/2-pyxel.width/4,100 ],[70,10],[1,2,3],['CREAR SERVIDOR',pyxel.COLOR_WHITE] ), # CLIENT
            buttons.Button([pyxel.width/2+pyxel.width/4,100],[80,10],[1,2,3],['UNIRSE A SERVIDOR',pyxel.COLOR_WHITE] ), # SERVER
        ]
        
    def update(self):
        for button in self.buttons:
            button.update()
        
    def draw(self):
        pyxel.cls(pyxel.COLOR_PEACH)
        pyxel.text(((pyxel.width/2)-((len('ASTEROID ONLINE LAN')*pyxel.FONT_WIDTH)/2)),25,'ASTEROID ONLINE LAN',1)
        pyxel.text(((pyxel.width/2)-((len('POR JOSEPH RIOS H')*pyxel.FONT_WIDTH)/2)),32,'POR JOSEPH RIOS H',1)
        for button in self.buttons:
            button.draw()
            