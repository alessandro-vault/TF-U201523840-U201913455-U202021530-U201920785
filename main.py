from helper.load_data import load
from data import streets, intersections


def main():
    print(streets)
    print(streets.find(4827828))
    print(streets.find_by(name="Alfonso Ugarte"))
    print(intersections.first)


if __name__ == "__main__":
    load()
    main()
