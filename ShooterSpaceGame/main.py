import player 
import mouseObject
import pyxel
import menu

class Game():
    def __init__(self,w,h):
        pyxel.init(
            width=w,
            height=h,
            caption='ShooterGame',
            fps=60
        )
        self.player = player.Player(5,3,(pyxel.width/2),(pyxel.height/2),1)
        self.mouse = mouseObject.Mouse(3,14,1)
        self.menu = menu.Menu()
        self.state = 0
        
        # 0 = MENU
        # 1 = GAME
        
        pyxel.run(self.update,self.draw)
        
    def update(self):
        
        self.mouse.update()
        if (self.state == 0):
            self.mouse.setColDefault(8)
            self.menu.update()
        if (self.state == 1):
            self.mouse.setColDefault(14)
            self.player.update(self.mouse.stateShoot)
    
    def draw(self):
        pyxel.cls(0)
        if (self.state == 0):
            self.menu.draw()
        if (self.state == 1):
            self.player.draw()
        self.mouse.draw()
        
if __name__ == '__main__':
    Game(192,128)