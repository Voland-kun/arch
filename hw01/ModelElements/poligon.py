from ..Stuff.point3d import Point3D


class Poligon:
    points: list[Point3D]

    def __init__(self, points):
        self.points = []
        self.points = points[:]
