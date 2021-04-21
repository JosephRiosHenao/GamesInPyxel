import keyboardInput
import player 
import mouseObject
import pyxel

class Game():
    def __init__(self,w,h):
        pyxel.init(
            width=w,
            height=h,
            caption='ShooterGame',
            fps=60
        )
        self.player = player.Player(5,3,(pyxel.width/2),(pyxel.height/2),1)
        self.mouse = mouseObject.Mouse()
        self.keyboard = keyboardInput.KeyboardInput()
        
        pyxel.run(self.update,self.draw)
        
    def update(self):
        self.player.update()
        self.mouse.update()
        self.keyboard.update()
    
    def draw(self):
        pyxel.cls(0)
        self.player.draw()
        self.mouse.draw()
        pyxel.text(20,20,self.keyboard.storage,1)
        
if __name__ == '__main__':
    Game(192,128)