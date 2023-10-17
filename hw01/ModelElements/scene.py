from polygonalmodel import PoligonalModel
from flash import Flash
from camera import Camera


class Scene:
    id: int
    models: list[PoligonalModel]
    flashes: list[Flash]
    cameras: list[Camera]

    def __init__(self, id, models, flashes, cameras):
        self.id = id
        if len(models) > 0:
            self.models = models[:]
        else:
            raise ValueError
        self.flashes = flashes[:]
        if len(cameras) > 0:
            self.cameras = cameras[:]
        else:
            raise ValueError

    def method1(self, flash) -> Flash:
        pass

    def method2(self, flash, camera) -> Flash:
        pass
