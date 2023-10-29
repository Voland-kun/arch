from random import randint


class CashProvider:
    __card: str
    __isAuthorized: bool

    def __init__(self):
        self.__card = randint(1000_0000_0000_0000, 9999_9999_9999_9999)
        self.__isAuthorized = False

    def buy(self):
        pass

    def authorization(self):
        pass





#     def getCardNum(self):
#         return self.__card_num
#
#     def setCardNum(self, card_num):
#         self.__card_num = card_num
#
#     @icontract.require(lambda self: int(self.getCardNum()) % 10 > 5)
#     def authorize(self):  # Попытка запилить контракт с предусловием.
#         # Авторизуем карту при условии, что последняя цифра больше 5
#         self.isAuthorized = True
#         print(f'Карта подтверждена: {self.__card_num}')
#
#     def getAuth(self):
#         return self.isAuthorized
#
#     def __repr__(self):
#         return f"CashProvider(card_num: {self.__card_num}, isAuthorized: {self.isAuthorized})"
#
#
#
#
# class Javatpoint:
#     def __init__(self, year=27):
#         self._year = year
#
#     @property
#     def Aboutyear(self):
#         return self.__year
#
#     @Aboutyear.setter
#     def Aboutyear(self, x):
#         self.__year = x
#
# grad_obj = Javatpoint()
# print(grad_obj._year)
#
# grad_obj.year = 2020
# print(grad_obj.year)
# Источник: https: // pythonpip.ru / osnovy / gettery - settery - python