
from helper.load_data import load
from services.intersections import find_by_street_name


def main():
    print(find_by_street_name('Plaza 2 de Mayo'))


if __name__ == "__main__":
    load()
    main()
