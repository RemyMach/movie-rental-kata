from enum import Enum
from abc import ABC, abstractmethod

class MovieCategory(Enum):
    REGULAR = "REGULAR"
    NEW_RELEASE = "NEW_RELEASE"
    CHILDREN = "CHILDREN"

class Movie(ABC):
    @abstractmethod
    def getStandardPrice(self):
        pass

    @abstractmethod
    def getMovieCategory(self):
        pass
    
    @abstractmethod
    def getTitle(self):
        pass


class RegularMovie(Movie):
    
    def __init__(self, title: str):
        self.title = title

    def getStandardPrice(self):
        return 2

    def getMovieCategory(self):
        return MovieCategory.REGULAR
    
    def getTitle(self):
        return self.title


class NewReleaseMovie(Movie):
    def __init__(self, title: str):
        self.title = title

    def getStandardPrice(self):
        return 3

    def getMovieCategory(self):
        return MovieCategory.NEW_RELEASE
    
    def getTitle(self):
        return self.title
    
class ChildrenMovie(Movie):
    def __init__(self, title: str):
        self.title = title

    def getStandardPrice(self):
        return 1.5

    def getMovieCategory(self):
        return MovieCategory.CHILDREN
    
    def getTitle(self):
        return self.title