
from helper.load_data import load
from services import intersections
from random import sample


def main():
    distance("Plaza 2 de Mayo", "Avenida Tupac Amaru")


def distance(start, end):
    if start == end:
        return
    start_intersection = sample(intersections.find_by(street_name=start), 1)
    end_intersection = sample(intersections.find_by(street_name=end), 1)
    print(start_intersection, end_intersection)


if __name__ == "__main__":
    load()
    main()
