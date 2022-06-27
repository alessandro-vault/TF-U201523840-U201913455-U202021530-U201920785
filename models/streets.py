from sqlalchemy import Integer, Column, String

from db.session import Base


class Street(Base):
    __tablename__ = "streets"
    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String)
    intersection_count = Column(Integer)

    def __repr__(self):
        return f"<Street: @id={self.id} @name={self.name} @intersection_count={self.intersection_count}>"

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
