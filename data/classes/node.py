class Node:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

    def pos(self):
        return self.lon, self.lat

    def line(self, node):
        return [self.lon, node.lon], [self.lat, node.lat]

    def distance_between(self, node):
        return ((self.lon - node.lon) ** 2 + (self.lat - node.lat) ** 2) ** 0.5

    def __repr__(self):
        return f'<Node lat:{self.lat}, lon:{self.lon}>'
