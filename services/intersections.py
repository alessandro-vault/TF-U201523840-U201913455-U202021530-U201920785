from db import db
from models.intersections import Intersection
from models.streets import Street


def get_all():
    return db.query(Intersection).all()


def find_by_street_name(street_name):
    street = db.query(Street).filter_by(name=street_name).first()
    return db.query(Intersection).filter_by(street_id=street.id).all()
