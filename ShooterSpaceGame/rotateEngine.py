import math

# MATRIZ DE ROTACION
def rotate(origin, point, angle):
    ox, oy = origin
    px, py = point
    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return [qx, qy]

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