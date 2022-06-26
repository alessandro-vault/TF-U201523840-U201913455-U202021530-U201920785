import csv

from helper.load_data import load
from classes.graph import Graph
from data import intersections


def main():
    points = list()
    with open('data/intersections.csv', 'r') as csvfile:
        csv_file_reader = csv.reader(csvfile, delimiter=',')
        for row in csv_file_reader:
            line = row[0].split(';')
            if float(line[11]) > -11.0 or float(line[11]) < -13.0 or float(line[12]) > -76 or float(
                    line[12]) < -77.4 or float(line[13]) > -11.0 or float(line[13]) < -13.0 or float(
                line[14]) > -76 or float(line[14]) < -77.4: continue
            points.append(
                [float(line[5]), float(line[12]), float(line[11]), float(line[6]), float(line[14]), float(line[13])])
    # points = [[1,1,2,2,3,4],[2,3,4,3,5,7],[3,5,7,4,5,2],[4,5,2,5,1,1],[5,1,1,1,1,2],[2,3,4,4,5,2]]
    graph = Graph(points)
    # new_map.find(1, 2)
    print('ok')  # bandera


if __name__ == "__main__":
    load()
    main()
