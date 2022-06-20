import gmplot
import os
import platform
from data import intersections


class Map:
    def __init__(self):
        self.gmap = gmplot.GoogleMapPlotter(-12.046619, -77.043157, 18)
        self.file_name = "map.html"
        self.coordinates = zip(
            *list(map(lambda x: x.start_coords, intersections)))
        self.labels = list(map(lambda x: x.identifier, intersections))
        self.load()

    def load(self):
        self.scatter()
        for intersection in intersections:
            self.add_plot(intersection.start_coords, intersection.end_coords)

    def scatter(self):
        self.gmap.scatter(*self.coordinates,
                          color="#FF0000", label=self.labels)

    def add_plot(self, start_coords, end_coords):
        self.gmap.plot(*(zip(*[start_coords, end_coords])),
                       "#6495ED", edge_width=3.0)

    def draw(self):
        system_os = platform.system()
        if system_os == "Windows":
            file_path = f'{os.getcwd()}\\{self.file_name}'
        elif system_os == "Linux" or system_os == "Darwin":
            file_path = f'{os.getcwd()}/{self.file_name}'
        if not os.path.exists(file_path):
            self.gmap.draw(file_path)
