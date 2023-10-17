from ..Stuff.angle3d import Angle3D
from ..Stuff.point3d import Point3D


class Camera:
    location: Point3D
    angle: Angle3D

    def __init__(self, location, angle):
        self.location = location
        self.angle = angle

    def rotate(self, angle) -> None:
        pass

    def move(self, location) -> None:
        pass
