from hw02.Fabric.GarbageGenerator import GarbageGenerator
from hw02.Fabric.GemGenerator import GemGenerator
from hw02.Fabric.GoldGenerator import GoldGenerator
import random


gem = GemGenerator()
gold = GoldGenerator()
garbage = GarbageGenerator()
loot_list = [gem, gold, garbage]

for i in range(1, 20):
    chest = random.choice(loot_list).create_item()
    chest.open()
