import backgroundPlace
class Paths():
    def __init__(self):
        self.paths = []
        self.engineBackground = backgroundPlace.Engine()
        self.placePath()
    def placePath(self):
        self.paths = self.engineBackground.place()
    def update(self):
        pass
    def draw(self):
        for path in self.paths:
            path.draw()
    