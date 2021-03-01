from VAR import *
import pyxel

class Snake():
    def __init__(self,feed):
        pass
    
class App():
    
    def __init__(self,WIDHT,HEIGHT):
        
        pyxel.init( width      = WIDHT,
                    height     = HEIGHT,
                    caption    = "Snake",
                    fps        = 60,
                    fullscreen = True, 
                    scale      = 8 )
        
        pyxel.load(RESOURCES)
        
        pyxel.mouse(True)
        pyxel.run(self.update,self.draw)
        
    def update(self):        
        pass


    def draw(self):
        pyxel.cls(1)
        
App(WIDTH,HEIGHT)
        