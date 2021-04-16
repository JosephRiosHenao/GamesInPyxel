import player 
import pyxel

class Game():
    def __init__(self,w,h):
        pyxel.init(
            width=w,
            height=h,
            caption='ShooterGame',
        )
        self.player = player.Player(5,5,(pyxel.width/2),(pyxel.height/2),1)
        pyxel.run(self.update,self.draw)
        
    def update(self):
        self.player.update()
        
    
    def draw(self):
        pyxel.cls(0)
        self.player.draw()
        
if __name__ == '__main__':
    Game(192,128)