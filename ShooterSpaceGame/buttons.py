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
            self.setCol = self.col[2]
        elif (self.state):
            self.setCol = self.col[1]
        else:
            self.setCol = self.col[0]
        
    def draw(self):
        pyxel.rect( self.pos[0]-(self.scale[0]/2),
                    self.pos[1]-(self.scale[1]/2),
                    self.scale[0],self.scale[1],
                    self.setCol)
        pyxel.text( (self.pos[0])-(pyxel.FONT_WIDTH*len(self.text[0]))/2, self.pos[1]-(self.scale[1]/pyxel.FONT_HEIGHT), self.text[0], self.text[1] )
    #   CONTINUES DRAWING AND COLLISION AND TEXT 
        
    def isColliding(self):
        return  (self.pos[0]-(self.scale[0]/2)) < pyxel.mouse_x + 1 and \
                (self.pos[0]-(self.scale[0]/2)) + self.scale[0] > pyxel.mouse_x and \
                (self.pos[1]-(self.scale[1]/2)) < pyxel.mouse_y + 1 and \
                (self.pos[1]-(self.scale[1]/2)) + self.scale[1] > pyxel.mouse_y