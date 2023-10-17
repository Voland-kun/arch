from ..Stuff.point3d import Point3D
from ..Stuff.angle3d import Angle3D
from ..Stuff.color import Color


class Flash:
    location: Point3D
    angle: Angle3D
    color: Color
    power: float

    def __init__(self, location, angle, color, power):
        self.location = location
        self.angle = angle
        self.color = color
        self.power = power

    def rotate(self, angle) -> None:
        pass

    def move(self, point) -> None:
        pass
