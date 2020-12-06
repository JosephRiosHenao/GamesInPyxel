import pyxel

class Rect:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        
    def is_colliding(self, other):
        return self.x < other.x + other.w and \
            self.x + self.w > other.x and \
            self.y < other.y + other.h and \
            self.y + self.h > other.y
        
    def draw(self, col, label=None):
        pyxel.rectb(self.x, self.y, self.w, self.h, col)
        
        if label:
            pyxel.text(self.x+2, self.y+2, label, col)

class App:
    def __init__(self):
        pyxel.init(90, 90, caption="Rect Test", scale=4, fps=15)
        
        pyxel.mouse(True)
        
        self.rect_a = Rect(52, 52, 30, 10)
        self.rect_b = Rect(4, 4, 32, 20)
        
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
            
        self.rect_b.x = pyxel.mouse_x - self.rect_b.w * 0.5
        self.rect_b.y = pyxel.mouse_y - self.rect_b.h * 0.5
            
    def draw(self):
        pyxel.cls(0)
        
        if self.rect_a.is_colliding(self.rect_b):
            pyxel.text(4, 4, "Rects are colliding.", 7)
            self.rect_a.draw(8, "Rect A") # red
            self.rect_b.draw(8, "Rect B") # red
        else:
            self.rect_a.draw(2, "Rect A") # purple
            self.rect_b.draw(3, "Rect B") # green

App()