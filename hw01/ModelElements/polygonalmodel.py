from ..Stuff.point3d import Point3D
from poligon import Poligon
from texture import Texture



class PoligonalModel:
    poligons: list[Poligon]
    textures: list[Texture]

    def __init__(self, textures):
        self.textures = []
        self.poligons = []
        self.textures = textures[:]
        self.poligons.append(Poligon(Point3D()))
