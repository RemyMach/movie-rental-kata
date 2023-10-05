from customer import Customer
from abc import ABC, abstractmethod

class FormatterStrategy(ABC):
    @abstractmethod
    def formatCustomer(self, customer: Customer):
        pass

class HtmlFormatterStrategy(FormatterStrategy):
    def formatCustomer(self, customer: Customer) -> str:
        totalAmount = 0
        frequentRenterPoints = 0
        result = self.formatHeader(customer.getName())
        for rental in customer._rentals:
            thisAmount = rental.getPrice()
            result += "\t<tr><td>" + rental.getMovie().getTitle() + "</td><td>" + str(thisAmount) + "</td></tr>\n"
            frequentRenterPoints += rental.getFrequentRenterPoints()
            totalAmount += thisAmount
        result += self.formatFooter(totalAmount, frequentRenterPoints)

        return result

    def formatHeader(self, customerName: str) -> str:
        result = "<h1>Rental Record for <em>" + customerName + "</em></h1>\n"
        result += "<table>\n"
        return result

    def formatFooter(self, totalAmount: int, frequentRenterPoints: int) -> str:
        result = "</table>\n"
        result += "<p>Amount owed is <em>" + str(totalAmount) + "</em></p>\n"
        result += "<p>You earned <em>" + str(frequentRenterPoints) + "</em> frequent renter points</p>\n"
        return result
        


class TextFormatterStrategy(FormatterStrategy):
    def formatCustomer(self, customer: Customer) -> str:
        totalAmount = 0
        frequentRenterPoints = 0
        result = self.formatHeader(customer.getName())

        for each in customer._rentals:
            thisAmount = each.getPrice()
            result += "\t" + each.getMovie().getTitle() + "\t" + str(thisAmount) + "\n"
            frequentRenterPoints += each.getFrequentRenterPoints()
            totalAmount += thisAmount

        result += self.formatFooter(totalAmount, frequentRenterPoints)

        return result
    
    def formatHeader(self, customerName: str) -> str:
        result = "Rental Record for " + customerName + "\n"
        return result

    def formatFooter(self, totalAmount: int, frequentRenterPoints: int) -> str:
        result = "Amount owed is " + str(totalAmount) + "\n"
        result += "You earned " + str(frequentRenterPoints) + " frequent renter points"
        return result