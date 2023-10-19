from hw02.Fabric.GarbageReward import GarbageReward
from hw02.Fabric.ItemFabric import ItemFabric


class GarbageGenerator(ItemFabric):
    def create_item(self):
        print("Создали сундук(мусор)")
        return GarbageReward()
