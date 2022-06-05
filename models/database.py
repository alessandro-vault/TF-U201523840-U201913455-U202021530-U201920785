from .street import Street
from .intersection import Intersection


class Database:
    def __init__(self):
        self.streets = []
        self.intersections = []

    def add_street(self, *args):
        self.streets.append(Street(*args))

    def add_intersection(self, *args):
        self.intersections.append(Intersection(*args))
