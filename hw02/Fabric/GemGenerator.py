from hw02.Fabric.GemReward import GemReward
from hw02.Fabric.ItemFabric import ItemFabric


class GemGenerator(ItemFabric):
    def create_item(self):
        print("Создали сундук(изумруд)")
        return GemReward()
