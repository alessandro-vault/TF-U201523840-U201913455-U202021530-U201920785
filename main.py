from helper.load_data import load
from classes.gmap import Map
from data import intersections


def main():
    print(intersections)
    print(len(intersections.start_coords()))


if __name__ == "__main__":
    load()
    main()
