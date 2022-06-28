from db import db
from models.intersections import Intersection
from models.streets import Street


def find_all():
    return db.query(Intersection).all()


def find_by(street_name=None, coords=None):
    if street_name:
        street = db.query(Street).filter_by(name=street_name).first()
        return db.query(Intersection).filter_by(street_id=street.id).all()
    elif coords:
        lat, lon = coords
        return db.query(Intersection).filter_by(start_lat=lat, start_lon=lon).first()
