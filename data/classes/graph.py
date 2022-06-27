import matplotlib.pyplot as plt
from data.classes.node import Node
from collections import defaultdict

from services.intersections import find_all as intersections


class Graph:
    def __init__(self):
        self.nodes = defaultdict(Node)
        self.adj = defaultdict(list)
        self.draw_plot()

    def draw_plot(self):
        fig, ax = plt.subplots()
        ax.set_aspect("equal", adjustable="datalim")
        ax.set_box_aspect(1)
        ax.autoscale()
        ax.invert_yaxis()
        plt.title('Mapa')

        for intersection in intersections():
            self.add_nodes(intersection)
            self.add_edge(intersection)

        for i in list(self.nodes.values()):
            ax.add_patch(
                plt.Circle(
                    tuple(reversed(i.pos())),
                    0.0005
                )
            )

        for i in self.adj:
            for j in self.adj[i]:
                x, y = self.nodes[i].line(self.nodes[j['to']])
                plt.plot(y, x)
        print(self.adj)
        plt.show()

    def add_nodes(self, intersection):
        self.nodes[intersection.start_intersection_id] = Node(intersection.start_lat, intersection.start_lon)
        self.nodes[intersection.end_intersection_id] = Node(intersection.end_lat, intersection.end_lon)

    def add_edge(self, intersection):
        self.adj[intersection.start_intersection_id].append(
            {
                "to": intersection.end_intersection_id,
                "distance": intersection.distance,
                "speed": intersection.speed
            }
        )

    def find_by(self, coords):
        for i in self.nodes:
            if self.nodes[i].pos() == coords:
                return i
        return None

    def locate(self, coords):
        self.find_by(coords)

    def __repr__(self):
        return repr(self.adj)

    def __iter__(self):
        return iter(self.adj)
