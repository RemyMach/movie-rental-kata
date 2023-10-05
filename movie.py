from enum import Enum
from abc import ABC, abstractmethod

class Movie(ABC):
    @abstractmethod
    def getStandardPrice(self):
        pass
    
    @abstractmethod
    def getTitle(self):
        pass

    @abstractmethod
    def getAmountDependingDaysRented(self, days_rented: int) -> float:
        pass

    @abstractmethod
    def getFrequentRenterPointsDependingDaysRented(self, days_rented: int) -> int:
        pass


class RegularMovie(Movie):
    
    def __init__(self, title: str):
        self.title = title
        self.REGULAR_FILM_INCREASE_DAY_THRESHOLD = 2
        self.REGULAR_FILM_INCREASE_PRICE = 1.5

    def getStandardPrice(self):
        return 2.0
    
    def getTitle(self):
        return self.title
    
    def getAmountDependingDaysRented(self, days_rented: int) -> float:
        thisAmount = self.getStandardPrice()
        if days_rented > self.REGULAR_FILM_INCREASE_DAY_THRESHOLD:
            thisAmount += (days_rented - self.REGULAR_FILM_INCREASE_DAY_THRESHOLD) * self.REGULAR_FILM_INCREASE_PRICE
        return thisAmount
    
    def getFrequentRenterPointsDependingDaysRented(self, days_rented: int) -> int:
        return 1

class NewReleaseMovie(Movie):
    def __init__(self, title: str):
        self.title = title

    def getStandardPrice(self):
        return 3.0
    
    def getTitle(self):
        return self.title
    
    def getAmountDependingDaysRented(self, days_rented: int) -> float:
        return days_rented * self.getStandardPrice()
    
    def getFrequentRenterPointsDependingDaysRented(self, days_rented: int) -> int:
        if days_rented > 1:
            return 2
        return 1
    
class ChildrenMovie(Movie):

    def __init__(self, title: str):
        self.title = title
        self.CHILD_FILM_INCREASE_DAY_THRESHOLD = 3
        self.CHILD_FILM_INCREASE_PRICE = 1.5

    def getStandardPrice(self):
        return 1.5
    
    def getTitle(self):
        return self.title

    def getAmountDependingDaysRented(self, days_rented: int) -> float:
        thisAmount = self.getStandardPrice()
        if days_rented > self.CHILD_FILM_INCREASE_DAY_THRESHOLD:
            thisAmount += (days_rented - self.CHILD_FILM_INCREASE_DAY_THRESHOLD) * self.CHILD_FILM_INCREASE_PRICE
        return thisAmount
    
    def getFrequentRenterPointsDependingDaysRented(self, days_rented: int) -> int:
        return 1