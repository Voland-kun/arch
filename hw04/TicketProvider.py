from datetime import datetime, timedelta
from Ticket import Ticket


class TicketProvider:
    def updateTicket(self, ticket: Ticket):
        result = True
        if ticket.ticket_date + timedelta(days=30) < datetime.now():
            ticket.is_valid = False
            result = False
        return result


    def getTicket(self, input_number, ticket: Ticket) -> bool:
        result = False
        if ticket.root_number == input_number:
            result = True
        return result
