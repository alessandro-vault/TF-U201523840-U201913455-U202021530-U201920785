class Node:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

    def pos(self):
        return self.lat, self.lon

    def line(self, node):
        return [self.lat, node.lat], [self.lon, node.lon]

    def distance_between(self, node):
        return (float(self.lat - node.lat) ** 2 + float(self.lon - node.lon) ** 2) ** 0.5

    def __repr__(self):
        return f'<Node lat:{self.lat}, lon:{self.lon}>'
