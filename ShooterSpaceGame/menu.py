import pyxel
import buttons

class Menu():
    def __init__(self):
        self.state = 0
        self.buttons = [
            buttons.Button([pyxel.width/2,80 ],[100,10],[12,5,1],['ENTRENAMIENTO LOCAL',6] ), # LOCAL
            buttons.Button([pyxel.width/2-pyxel.width/4,100 ],[70,10],[12,5,1],['CREAR SERVIDOR',6] ), # CLIENT
            buttons.Button([pyxel.width/2+pyxel.width/4,100],[80,10],[12,5,1],['UNIRSE A SERVIDOR',6] ), # SERVER
        ]
        
    def update(self):
        for button in self.buttons:
            button.update()
            
        for i in range(len(self.buttons)):
            if (self.buttons[i].isColliding() and pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON)): self.actionButton(i)
        
    def draw(self):
        pyxel.cls(6)
        pyxel.text(((pyxel.width/2)-((len('ASTEROID ONLINE LAN')*pyxel.FONT_WIDTH)/2)),25,'ASTEROID ONLINE LAN',5)
        pyxel.text(((pyxel.width/2)-((len('POR JOSEPH RIOS H')*pyxel.FONT_WIDTH)/2)),32,'POR JOSEPH RIOS H',12)
        for button in self.buttons:
            button.draw()
            
    def actionButton(self,index):
        if (index == 0): self.state = 1
            