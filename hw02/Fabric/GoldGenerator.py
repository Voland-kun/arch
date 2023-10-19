from hw02.Fabric.GoldReward import GoldItem
from hw02.Fabric.ItemFabric import ItemFabric


class GoldGenerator(ItemFabric):
    def create_item(self):
        print("Создали сундук(золото)")
        return GoldItem()
