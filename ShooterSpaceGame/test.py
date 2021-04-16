import pyxel
import math
from time import time

SCREEN_W, SCREEN_H = 120, 120  # screnn size
SIZE = 10  # Square size in pixels

# Rotate a point around origin with a given angle
def rotate(origin, point, angle):
    ox, oy = origin
    px, py = point
    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return [qx, qy]

# Rotate each point around shape center
# then move them to position
# and offset them so the shape center equal positon
def update_points(o_points, center, pos, angle):
    points = []
    ox, oy = center
    px, py = pos
    for i, p in enumerate(o_points):
        point = rotate(center, p, angle)
        point[0] += px - ox
        point[1] += py - oy
        points.append(point)
    return points

class App:
    def __init__(self):
        pyxel.init(SCREEN_W, SCREEN_H)

        self.a_shape = [
            [SIZE/2, SIZE/2],
            [0, 0],
            [0, SIZE],
        ]  # Points of shape, here a square
        self.center = [SIZE / 2, SIZE / 2]  # center of the shape

        self.points = [None for i in range(len(self.a_shape))]  # Points for drawings
        self.pos = [SCREEN_W / 2, SCREEN_H / 2]  # position
        self.angle = 0  # Rotation
        self.vel = [15, 8]  # Velocity: in pixels /seconds
        self.speed_rotation = 2  # Spin rotation in radians / second

        self.pt = time()  # previous time

        pyxel.run(self.update, self.draw)

    def update(self):

        # Delta time management
        t = time()
        dt = t - self.pt
        self.pt = t

        # Update rotation angle
        self.angle += self.speed_rotation * dt

        # Update drawing points
        self.points = update_points(self.a_shape, self.center, self.pos, self.angle)

    def draw(self):
        # Clear Screen
        pyxel.cls(0)
        # Draw the shape : draw a line betwenn each drawin points
        for p in range(1, len(self.points)):
            pyxel.line(*self.points[p - 1], *self.points[p], 7)
        pyxel.line(*self.points[p], *self.points[0], 7)


App()