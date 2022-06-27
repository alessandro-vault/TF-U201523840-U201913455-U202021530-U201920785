import matplotlib.pyplot as plt
from classes.node import Node
from collections import defaultdict


class Graph:
    def __init__(self):
        self.intersections = []
        self.nodes = defaultdict(Node)
        self.adj = defaultdict(list)

    def build(self, intersections):
        self.intersections = intersections
        self.draw_plot()

    def draw_plot(self):
        fig, ax = plt.subplots()
        ax.set_aspect("equal", adjustable="datalim")
        ax.set_box_aspect(1)
        ax.autoscale()
        ax.invert_yaxis()
        plt.title('Mapa')
        for i in self.intersections:
            self.add_node(i.start_intersection_id, Node(*i.start_coords))
            self.add_node(i.end_intersection_id, Node(*i.end_coords))
            self.adj[i.start_intersection_id].append(i.end_intersection_id)

        for i in list(self.nodes.values()):
            ax.add_patch(plt.Circle(i.pos(), 0.0001))

        for i in self.adj:
            for j in self.adj[i]:
                x, y = self.nodes[i].line(self.nodes[j])
                plt.plot(x, y)

    def add_node(self, _id, node):
        self.nodes[_id] = node

    def __repr__(self):
        return repr(self.adj)

    def __iter__(self):
        return iter(self.adj)

