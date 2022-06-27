from data import intersections, streets, graph


class App:
    def __init__(self):
        pass

    def directions(self, start, end):
        start_node = graph.locate(
            intersections.find_by(street=streets.find_by(start))
            .start_coords
        )
        print(start_node)


