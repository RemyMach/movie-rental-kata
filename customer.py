from rental import Rental

class Customer:
    def __init__(self, name: str):
        self.rentals = []
        self.name = name

    def getName(self) -> str:
        return self.name
    
    def getRentals(self) -> list[Rental]:
        return self.rentals

    def addRental(self, param):
        self.rentals.append(param)