import csv
import os

from data.classes.graph import Graph
from models.intersections import Intersection
from models.streets import Street
from data.classes.gmap import Map
from db import db, session


def load():
    load_map()
    load_graph()


def load_database():
    session.Base.metadata.create_all(session.engine)
    for file_name in ["streets", "intersections"]:
        with open(f"data/{file_name}.csv", mode="r", encoding="utf-8-sig") as file:
            reader = csv.reader(file, delimiter=";")
            for row in reader:
                row = list(map(lambda x: parse_float(x), row))
                if file_name == "streets":
                    if not db.query(Street).filter(Street.id == int(row[0])).first():
                        new_street = Street(
                            id=int(row[0]),
                            name=row[1],
                            intersection_count=int(row[2]),
                        )
                        db.add(new_street)
                        db.commit()
                else:
                    if not db.query(Intersection).filter(Intersection.id == int(row[0])).first():
                        new_intersection = Intersection(
                            id=int(row[0]),
                            street_id=int(row[1]),
                            start_id=int(row[3]),
                            end_id=int(row[4]),
                            start_intersection_id=int(row[5]),
                            end_intersection_id=int(row[6]),
                            distance=float(row[7]),
                            speed=float(row[8]),
                            start_lat=float(row[11]),
                            start_lon=float(row[12]),
                            end_lat=float(row[13]),
                            end_lon=float(row[14]),
                        )
                        db.add(new_intersection)
                        db.commit()


def load_map():
    gmap = Map()
    gmap.draw()


def load_graph():
    graph = Graph()
    return graph


def parse_float(value):
    try:
        return float(value)
    except ValueError:
        return str(value)
