from helper.load_data import load
from classes.app import App


def main():
    app = App()
    app.directions(start="Plaza 2 de Mayo", end="Arequipa")


if __name__ == "__main__":
    load()
    main()
