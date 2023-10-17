from abc import ABC, abstractmethod


class IModelChangedObserver(ABC):
    @abstractmethod
    def ApplyUpdateModel(self):
        pass
