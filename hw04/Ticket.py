from datetime import datetime
from decimal import Decimal
from random import randint


class Ticket:
    __dateTime: datetime
    __priceTicket: Decimal
    __place: int
    __rootNumber: int
    __isValid = True
    __count = 0

    def __init__(self):
        self.__dateTime = datetime.now()
        self.__priceTicket = Decimal(randint(1000, 100000))/100
        self.__place = randint(1, 100)
        Ticket.__count += 1
        self.__rootNumber = Ticket.__count
        self.__isValid = Ticket.__isValid

    def __repr__(self):
        return (f"Билет:\n"
                f"дата: {self.__dateTime}\n"
                f"цена: {self.__priceTicket}\n"
                f"место: {self.__place}\n"
                f"номер: {self.__rootNumber:06d}\n"   
                f"валидность: {self.__isValid}\n")

    @property
    def is_valid(self):
        return self.__isValid

    @is_valid.setter
    def is_valid(self, new: bool):
        self.__isValid = new

    @property
    def root_number(self):
        return self.__rootNumber

    @property
    def ticket_date(self):
        return self.__dateTime
