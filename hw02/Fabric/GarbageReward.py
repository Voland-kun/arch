import zope
from hw02.Fabric.IGameItem import IGameItem


@zope.interface.implementer(IGameItem)
class GarbageReward:
    def open(self):
        print("Открыли сундук с мусором")
