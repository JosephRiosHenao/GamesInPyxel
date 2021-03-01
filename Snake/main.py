import pyxel
import random
import enum

WIDTH = 192
HEIGHT = 128

RESOURCES = "Assets/resources.pyxres"
class Direction(enum.Enum):
    RIGHT = 0
    LEFT  = 1
    DOWN  = 2
    UP    = 3
class Coin():
    
    def __init__(self,x,y):
        
        self.x = x
        self.y = y
        
        self.w = 8
        self.h = 8

    def draw(self):
        pyxel.blt(self.x,self.y,0,16,0,self.w,self.h,0)
        
    def randomPosition(self):
        self.x = random.randint(0,pyxel.width)
        self.y = random.randint(0,pyxel.height)
        
class SnakeSection():
    def __init__(self,x,y,isHead=False):
        
        self.x = x
        self.y = y
        
        self.w = 8
        self.h = 8
        
        self.isHead = isHead
        
    def draw(self,direction):
        
        width = self.w
        height = self.h
        
        spriteX = 0
        spriteY = 0 
        
        if self.isHead:
            
            if direction == Direction.RIGHT:
                spriteX = 8
                spriteY = 8
            if direction == Direction.LEFT:
                spriteX = 8
                spriteY = 8
                width = width * -1
                
            if direction == Direction.UP:
                spriteX = 0
                spriteY = 8
            if direction == Direction.DOWN:
                spriteX = 0
                spriteY = 8
                height = height * -1
                
            
        
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
            self.coin.randomPosition()

    def draw(self):
        pyxel.cls(1)
        self.coin.draw()
        
App(WIDTH,HEIGHT)
        