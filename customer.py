class Customer:
    def __init__(self, name):
        self._rentals = []
        self.name = name

    def getName(self):
        return self.name

    def addRental(self, param):
        self._rentals.append(param)