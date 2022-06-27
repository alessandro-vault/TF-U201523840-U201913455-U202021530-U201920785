import random

from sqlalchemy import Integer, Column, ForeignKey, Float, ARRAY

from db.session import Base


class Intersection(Base):
    __tablename__ = 'intersections'
    id = Column(Integer, primary_key=True)
    street_id = Column(Integer, ForeignKey('streets.id'))
    start_id = Column(Integer)
    end_id = Column(Integer)
    start_intersection_id = Column(Integer)
    end_intersection_id = Column(Integer)
    distance = Column(Float)
    speed = Column(Float)
    start_lat = Column(Float)
    start_lon = Column(Float)
    end_lat = Column(Float)
    end_lon = Column(Float)

    def start_coords(self):
        return self.start_lat, self.start_lon

    def __repr__(self):
        return f"<Intersection {self.id}: {self.start_lat, self.start_lon} => {self.end_lat, self.end_lon}>"
