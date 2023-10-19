import zope
from hw02.Fabric.IGameItem import IGameItem


@zope.interface.implementer(IGameItem)
class GemReward:
    def open(self):
        print("Открыли сундук с изумрудом")
