class Street:
    def __init__(self, _id, name, intersection_count):
        self.identifier = int(_id)
        self.name = str(name)
        self.intersection_count = int(intersection_count)

    def __repr__(self):
        return f"<Street: @id={self.identifier} @name={self.name} @intersection_count={self.intersection_count}>"


class Streets:
    def __init__(self):
        self.streets = []

    def add_street(self, *args):
        self.streets.append(Street(*args))

    def find(self, identifier):
        for street in self.streets:
            if street.identifier == identifier:
                return street

    def find_by(self, name):
        for street in self.streets:
            if street.name == name:
                return street

    def __repr__(self):
        return f"<Streets @street_count={len(self.streets)}>"
