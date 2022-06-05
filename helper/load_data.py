import csv


def load(db):
    for file_name in ["streets", "intersections"]:
        with open(f'data/{file_name}.csv') as file:
            reader = csv.reader(file, delimiter=';')
            for row in reader:
                if file_name == "streets":
                    db.add_street(*row)
                else:
                    db.add_intersection(*row)
