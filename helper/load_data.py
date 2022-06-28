import csv

from data import streets, intersections, graph
from classes.gmap import Map


def load():
    for file_name in ["streets", "intersections"]:
        with open(f"data/{file_name}.csv", mode="r", encoding="utf-8-sig") as file:
            reader = csv.reader(file, delimiter=";")
            for row in reader:
                row = list(map(lambda x: parse_float(x), row))
                if file_name == "streets":
                    streets.add_street(*row)
                else:
                    if intersection_condition(row):
                        continue
                    else:
                        intersections.add_intersection(*row)

    load_map()
    graph.build(intersections)  # build graph


def load_map():
    gmap = Map()
    gmap.draw()


def intersection_condition(line):
    return float(line[11]) > -11.0 or float(line[11]) < -13.0 or float(line[12]) > -76 or float(
        line[12]) < -77.4 or float(line[13]) > -11.0 or float(line[13]) < -13.0 or float(
        line[14]) > -76 or float(line[14]) < -77.4


def parse_float(value):
    try:
        return float(value)
    except ValueError:
        return str(value)
