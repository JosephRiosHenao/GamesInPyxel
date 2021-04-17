import pyxel

class Mouse():
    
    def update(self):
        self.x = pyxel.mouse_x
        self.y = pyxel.mouse_y
        self.col = 15
        self.margin = 2
        
    def draw(self):
        pyxel.pset(self.x+self.margin,self.y,self.col) # RIGHT
        pyxel.pset(self.x-self.margin,self.y,self.col) # LEFT
        
        pyxel.pset(self.x,self.y+self.margin,self.col) # RIGHT
        pyxel.pset(self.x,self.y-self.margin,self.col) # LEFT
        
        pyxel.pset(self.x,self.y,self.col) # CENTER