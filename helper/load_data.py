import csv


def load(db):
    with open("data/streets.csv") as file:
        reader = csv.reader(file, delimiter=";")
        for row in reader:
            db.add_street(*row)
    with open("data/intersections.csv") as file:
        reader = csv.reader(file, delimiter=";")
        for row in reader:
            db.add_intersection(*row)
