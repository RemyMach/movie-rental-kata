
from movie import Movie

class Rental:
    def __init__(self, movie: Movie, daysRented: int):
        self.daysRented = daysRented
        self.movie = movie

    def getPrice(self) -> float:
        return self.movie.getAmountDependingDaysRented(self.daysRented)

    def getFrequentRenterPoints(self) -> int:
        return self.movie.getFrequentRenterPointsDependingDaysRented(self.daysRented)

    def getDaysRented(self) -> int:
        return self.daysRented

    def getMovie(self) -> Movie:
        return self.movie
