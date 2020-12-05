import pyxel


init(self, x, y, angle, launched):
    self.x = x
    self.y = y
    self.vx = V0 * cos(angle)
    self.vy = V0 * sin(angle)
    self.launched = launched

update(self):
    if self.launched:  # Stays in place until it is set to launched, vx and vy keep the information about the angle
        self.vy += g # += because in pyxel the y axis goes down
        self.x += self.vx
        self.y += self.vy

draw(self):
    pyxel.blt(self.x, self.y, .......)
    # Preview
    x_future = self.x
    y_future = self.y
    vx_future = self.vx
    vy_future = self.vy
    for i in range(0, 30, 3): # To be fine tuned, I suggest to use an iteration step greater than one for performance reasons
    vy_future_plus1 = vy_future + g
    x_future_plus1 = x_future + vx_future
    y_future_plus1 = y_future + vy_future
    pyxel.line(x_future, y_future, x_future_plus1, y_future_plus1, 7)
    vy_future = vy_future_plus1
    x_future = x_future_plus1
    y_future = y_future_plus1