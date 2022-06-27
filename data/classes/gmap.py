import gmplot
import os
import platform

from services.intersections import get_all as intersections


class Map:
    def __init__(self):
        self.intersections = intersections()
        self.gmap = gmplot.GoogleMapPlotter(-12.046619, -77.043157, 18)
        self.file_name = "map.html"
        self.coordinates = zip(
            *list(map(lambda x: (x.start_lat, x.start_lon), self.intersections))
        )
        self.labels = list(map(lambda x: x.id, self.intersections))
        self.load()

    def load(self):
        self.scatter()
        for i in self.intersections:
            self.add_plot(
                (i.start_lat, i.start_lon),
                (i.end_lat, i.end_lon)
            )

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
