import time
import pyxel

class Snake():
    def __init__(self,feed):
    
class SnakeGame():
    
    def __init__(self,WIDHT,HEIGHT):
        
        self.x = 0
        self.y = 0
        #self.table = []
        
        pyxel.init( width   = WIDHT,
                    height  = HEIGHT,
                    caption = "Snake",
                    fps     = 60 )
        pyxel.mouse(True)
        pyxel.run(self.update,self.draw)
        
    def update(self):        
        # if self.y != pyxel.height:
        #     self.x += 5
        #     self.table.append([self.x,self.y])
        #     if self.x == pyxel.width: 
        #         self.x = 0
        #         self.y += 5
        # else:   print(self.table)


    def draw(self):
        pyxel.cls(1)
        #pyxel.rectb(self.x, self.y, 5, 5, 9)
        
SnakeGame(240,150)
        