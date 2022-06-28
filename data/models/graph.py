import matplotlib.pyplot as plt
from classes.node import Node
from collections import defaultdict


class Graph:
    def __init__(self, a, b):
        self.intersections = []
        self.nodes = defaultdict(Node)
        self.adj = defaultdict(list)
        self.start_node = a
        self.destination_node = b

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
                plt.plot(x, y, 'green')
        path, paths = self.find(self.start_node, self.destination_node)
        for i in paths:
            j = 0
            while j < len(i) - 2:
                x, y = self.nodes[i[j]].line(self.nodes[i[j + 1]])
                j = j + 1
                plt.plot(x, y, 'red')
            j = 0
        while i < len(path) - 2:
            x, y = self.nodes[path[i]].line(self.nodes[path[i + 1]])
            i = i + 1
            plt.plot(x, y, 'blue')
        plt.show()

    def _next(self, a, b, path, ban_list):
        next_node = -1
        h = 1.0

        try:
            self.adj[a]
        except KeyError:
            ban_list.append(a)
            path.append(next_node)
            return path, ban_list
        for i in self.adj[a]:
            if h > self.nodes[i].distance_between(self.nodes[b]) and i not in ban_list:
                h = self.nodes[i].distance_between(self.nodes[b])
                next_node = i
            if next_node == b:
                path.append(b)
            elif next_node != -1:
                path, ban_list = self._next(next_node, b, path, ban_list)
            else:
                ban_list.append(a)
                path.append(next_node)
                return path, ban_list
            return path, ban_list

    def _find(self, a, b, ban_list):
        path = [a]
        path, ban_list = self._next(a, b, path, ban_list)
        return path, ban_list

    def find(self, a, b):
        paths = []
        path = [-1]
        ban_list = []
        while -1 in path:
            path, ban_list = self._find(a, b, ban_list)
            paths.append(path)
        return path, paths

    def add_node(self, _id, node):
        self.nodes[_id] = node

    def __repr__(self):
        return repr(self.adj)

    def __iter__(self):
        return iter(self.adj)

