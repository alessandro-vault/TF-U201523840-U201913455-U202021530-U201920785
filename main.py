from helper.load_data import load
from data import streets, intersections
import graphviz as gv


def main():
    print(intersections.first())
    print(streets.find(intersections.first().street_id))


if __name__ == "__main__":
    load()
    main()
