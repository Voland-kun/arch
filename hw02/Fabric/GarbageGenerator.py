from ItemFabric import ItemFabric
from GarbageReward import LootReward


class GarbageGenerator(ItemFabric):
    def create_item(self):
        print("Создали сундук(мусор)")
        return LootReward()
