
from movie import Movie, MovieCategory

class Rental:
    def __init__(self, movie: Movie, daysRented: int):
        self.daysRented = daysRented
        self.movie = movie

    def getPrice(self):
        REGULAR_FILM_INCREASE_DAY_THRESHOLD = 2
        REGULAR_FILM_INCREASE_PRICE = 1.5

        CHILD_FILM_INCREASE_DAY_THRESHOLD = 3
        CHILD_FILM_INCREASE_PRICE = 1.5

        thisAmount = 0.0
        if self.movie.getMovieCategory() == MovieCategory.REGULAR:
            thisAmount += self.movie.getStandardPrice()
            if self.daysRented > REGULAR_FILM_INCREASE_DAY_THRESHOLD:
                thisAmount += (self.daysRented - REGULAR_FILM_INCREASE_DAY_THRESHOLD) * REGULAR_FILM_INCREASE_PRICE
        elif self.movie.getMovieCategory() == MovieCategory.NEW_RELEASE:
            thisAmount += self.daysRented * self.movie.getStandardPrice()
        elif self.movie.getMovieCategory() == MovieCategory.CHILDREN:
            thisAmount += self.movie.getStandardPrice()
            if self.daysRented > CHILD_FILM_INCREASE_DAY_THRESHOLD:
                thisAmount += (self.daysRented - CHILD_FILM_INCREASE_DAY_THRESHOLD) * CHILD_FILM_INCREASE_PRICE
        return thisAmount
    


    def getFrequentRenterPoints(self):
        if (self.movie.getMovieCategory() == MovieCategory.NEW_RELEASE) and self.daysRented > 1:
            return 2
        return 1


    def getDaysRented(self):
        return self.daysRented

    def getMovie(self):
        return self.movie
