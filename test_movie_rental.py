from rental import Rental
from customer import Customer
from movie import Movie, MovieCategory, RegularMovie, NewReleaseMovie, ChildrenMovie
from formatter_strategy import HtmlFormatterStrategy, TextFormatterStrategy


def testsText():
    customer = Customer("Bob")
    customer.addRental(Rental(RegularMovie("Jaws"), 2))
    customer.addRental(Rental(RegularMovie("Golden Eye"), 3))
    customer.addRental(Rental(NewReleaseMovie("Short New"), 1))
    customer.addRental(Rental(NewReleaseMovie("Long New"), 2))
    customer.addRental(Rental(ChildrenMovie("Bambi"), 3))
    customer.addRental(Rental(ChildrenMovie("Toy Story"), 4))

    expected = "Rental Record for Bob\n"
    expected += "\tJaws\t2.0\n"
    expected += "\tGolden Eye\t3.5\n"
    expected += "\tShort New\t3.0\n"
    expected += "\tLong New\t6.0\n"
    expected += "\tBambi\t1.5\n"
    expected += "\tToy Story\t3.0\n"
    expected += "Amount owed is 19.0\n"
    expected += "You earned 7 frequent renter points"

    formatterStrategy = TextFormatterStrategy()
    assert expected == formatterStrategy.formatCustomer(customer)

def tests_whenHaveOneFilm_shouldPrintOneRentalMovieInHTMLFormat():
    customer = Customer("martin")
    customer.addRental(Rental(RegularMovie("Ran"), 3))

    expected = "<h1>Rental Record for <em>martin</em></h1>\n"
    expected += "<table>\n"
    expected += "\t<tr><td>Ran</td><td>3.5</td></tr>\n"
    expected += "</table>\n"
    expected += "<p>Amount owed is <em>3.5</em></p>\n"
    expected += "<p>You earned <em>1</em> frequent renter points</p>\n"


    formatterStrategy = HtmlFormatterStrategy()
    assert expected == formatterStrategy.formatCustomer(customer)

def tests_whenHaveMultipleFilms_shouldPrintMultipleRentalMoviesInHTMLFormat():
    customer = Customer("Bob")
    customer.addRental(Rental(RegularMovie("Jaws"), 2))
    customer.addRental(Rental(RegularMovie("Golden Eye"), 3))
    customer.addRental(Rental(NewReleaseMovie("Short New"), 1))
    customer.addRental(Rental(NewReleaseMovie("Long New"), 2))
    customer.addRental(Rental(ChildrenMovie("Bambi"), 3))
    customer.addRental(Rental(ChildrenMovie("Toy Story"), 4))

    expected = "<h1>Rental Record for <em>Bob</em></h1>\n"
    expected += "<table>\n"
    expected += "\t<tr><td>Jaws</td><td>2.0</td></tr>\n"
    expected += "\t<tr><td>Golden Eye</td><td>3.5</td></tr>\n"
    expected += "\t<tr><td>Short New</td><td>3.0</td></tr>\n"
    expected += "\t<tr><td>Long New</td><td>6.0</td></tr>\n"
    expected += "\t<tr><td>Bambi</td><td>1.5</td></tr>\n"
    expected += "\t<tr><td>Toy Story</td><td>3.0</td></tr>\n"
    expected += "</table>\n"
    expected += "<p>Amount owed is <em>19.0</em></p>\n"
    expected += "<p>You earned <em>7</em> frequent renter points</p>\n"


    formatterStrategy = HtmlFormatterStrategy()
    assert expected == formatterStrategy.formatCustomer(customer)