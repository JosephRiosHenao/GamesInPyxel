import player 
import mouseObject
import pyxel

class Game():
    def __init__(self,w,h):
        pyxel.init(
            width=w,
            height=h,
            caption='ShooterGame',
        )
        self.player = player.Player(10,5,(pyxel.width/2),(pyxel.height/2),1)
        self.mouse = mouseObject.Mouse()
        pyxel.run(self.update,self.draw)
        
    def update(self):
        self.player.update()
        self.mouse.update()
    
    def draw(self):
        pyxel.cls(0)
        self.player.draw()
        self.mouse.draw()
        
if __name__ == '__main__':
    Game(192,128)