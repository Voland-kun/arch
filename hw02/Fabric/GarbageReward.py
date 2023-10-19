import zope
from IGameItem import IGameItem


@zope.interface.implementer(IGameItem)
class LootReward:
    def open(self):
        print("Открыли сундук с мусором")

