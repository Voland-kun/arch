import zope
from IGameItem import IGameItem


@zope.interface.implementer(IGameItem)
class GemReward:
    def open(self):
        print("Открыли сундук с изумрудом")
