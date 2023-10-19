import zope.interface
from hw02.Fabric.IGameItem import IGameItem


@zope.interface.implementer(IGameItem)
class GoldItem:
    def open(self):
        print("Открыли сундук с золотом")
