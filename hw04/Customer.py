from datetime import datetime
from cashProvider import CashProvider
from TicketProvider import TicketProvider
from Ticket import Ticket


class Customer:
    __id: int
    __tickets: list[Ticket] = []
    __cashProvider: CashProvider
    __ticketProvider: TicketProvider
    __count = 0

    def __init__(self):
        Customer.__count += 1
        self.__id = Customer.__count
        self.__tickets = Customer.__tickets
        self.__cashProvider = CashProvider()
        self.__ticketProvider = TicketProvider()

    def buyTicket(self):
        pass

    def searchTicket(self, date: datetime.date):
        # вероятно предусловие
        # -/-/-
        if not self.get_tickets:
            raise Exception('Нет билетов')
        # -/-/-
        result = []
        for ticket in self.get_tickets:
            if ticket.ticket_date.date == date:
                result.append(ticket)

    def buyTicket(self, ticket: Ticket):
        # вероятно предусловие
        # -/-/-
        if not ticket.is_valid:
            raise Exception('Билет просрочен')
        # -/-/-
        result = False
        if self.get_cash_provider.authorization() and self.get_ticket_provider.getTicket():
            self.get_cash_provider.buy()
            result = True
        return result

    @property
    def get_tickets(self):
        return self.__tickets

    @property
    def get_cash_provider(self):
        return self.__cashProvider

    @property
    def get_ticket_provider(self):
        return self.__ticketProvider
