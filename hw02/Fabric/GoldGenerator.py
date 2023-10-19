from ItemFabric import ItemFabric
from GoldReward import GoldItem


class GoldGenerator(ItemFabric):
    def create_item(self):
        print("Создали сундук(золото)")
        return GoldItem()
