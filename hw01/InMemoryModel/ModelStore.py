from ..ModelElements.polygonalmodel import PoligonalModel
from ..ModelElements.scene import Scene
from ..ModelElements.flash import Flash
from ..ModelElements.camera import Camera
from .IModelChanger import IModelChanger
from .IModelChangedObserver import IModelChangedObserver


class ModelStore(IModelChanger):
    models: list[PoligonalModel]
    scenes: list[Scene]
    flashes: list[Flash]
    cameras: list[Camera]
    i_model_changed_observer: list[IModelChangedObserver]

    def __init__(self, i_model_changed_observer):
        self.Models = []
        self.Scenes = []
        self.Flashes = []
        self.Cameras = []
        self.i_model_changed_observer = i_model_changed_observer[:]

        self.Models.append(PoligonalModel())
        self.Flashes.append(Flash())
        self.Cameras.append(Camera())
        self.Scenes.append(Scene(0, self.Models, self.Flashes, self.Cameras))

    def GetScene(self, id):
        for scene in self.Scenes:
            if scene.id == id:
                return scene
        return None

    def NotifyChange(self, sender):
        pass
