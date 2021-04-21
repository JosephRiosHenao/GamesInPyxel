import pyxel

class Button():
    def __init__(self,pos,scale,col,text):
        self.text = text
        self.pos = pos
        self.scale = scale
        self.col = col
        self.setCol = col[0]
        self.state = False
        
    def update(self):
        self.state = self.isColliding()
        
        if (self.state and pyxel.btn(pyxel.MOUSE_LEFT_BUTTON)):
            self.setCol = self.col[3]
        elif (self.state):
            self.setCol = self.col[1]
        else:
            self.setCol = self.col[0]
        
    def draw(self):
        pass
    #   CONTINUES DRAWING AND COLLISION AND TEXT 
        
    def isColliding(self):
        return True