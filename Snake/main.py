import pyxel
import random

WIDTH = 192
HEIGHT = 128

RESOURCES = "Assets/resources.pyxres"

class Coin():
    
    def __init__(self,x,y):
        
        self.x = x
        self.y = y
        
        self.w = 8
        self.h = 8

    def draw(self):
        pyxel.blt(self.x,self.y,0,16,0,self.w,self.h,0)
class App():
    
    def __init__(self,WIDHT,HEIGHT):
        
        pyxel.init( width      = WIDHT,
                    height     = HEIGHT,
                    caption    = "Snake",
                    fps        = 60,
                    fullscreen = True, 
                    scale      = 8 )
        
        pyxel.load(RESOURCES)
        
        self.coin = Coin(WIDHT/2,HEIGHT/2)
        
        pyxel.mouse(True)
        pyxel.run(self.update,self.draw)
        
    def update(self):        
        if (pyxel.btnp(pyxel.KEY_SPACE==True)):
            self.coin.x = random.randint(0,pyxel.width)
            self.coin.y = random.randint(0,pyxel.height)


    def draw(self):
        pyxel.cls(1)
        self.coin.draw()
        
App(WIDTH,HEIGHT)
        