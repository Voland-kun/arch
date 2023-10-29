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
