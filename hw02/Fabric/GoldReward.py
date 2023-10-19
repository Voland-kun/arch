import zope.interface
from IGameItem import IGameItem


@zope.interface.implementer(IGameItem)
class GoldItem:
    def open(self):
        print("Открыли сундук с золотом")
