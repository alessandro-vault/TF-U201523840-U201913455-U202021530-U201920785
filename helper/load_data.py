import csv

from data import streets, intersections


def load():
    for file_name in ["streets", "intersections"]:
        with open(f'data/{file_name}.csv', mode='r', encoding='utf-8-sig') as file:
            reader = csv.reader(file, delimiter=';')
            for row in reader:
                row = map(lambda x: parse_float(x), row)
                if file_name == "streets":
                    streets.add_street(*row)
                else:
                    intersections.add_intersection(*row)


def parse_float(value):
    try:
        return float(value)
    except ValueError:
        return str(value)
