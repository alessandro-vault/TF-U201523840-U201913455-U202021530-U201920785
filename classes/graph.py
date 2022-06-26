import matplotlib.pyplot as plt
from classes.node import Node
from data import intersections


class Graph:
    nodes = dict()
    adj = dict()

    def __init__(self, points):
        fig, ax = plt.subplots()
        ax.set_aspect("equal", adjustable="datalim")
        ax.set_box_aspect(1)
        ax.autoscale()
        plt.title('Mapa')
        # 0 => start_intersection_id
        # 1 => start_coords, lon
        # 2 => start_coords, lat
        # 3 => end_intersection_id
        # 4 => end_coords, lon
        # 5 => end_coords, lat
        for idx, i in enumerate(intersections):
            a = Node(*i.start_coords)
            if idx == 3:
                print(a)
            self.nodes[i.start_intersection_id] = Node(*i.start_coords)
        for idx, i in enumerate(points):
            a = Node(i[1], i[2])
            if idx == 3:
                print(a)
            self.nodes[i[0]] = Node(i[1], i[2])
            self.nodes[i[3]] = Node(i[4], i[5])
            if i[0] not in self.adj:
                self.adj[i[0]] = list()
            self.adj[i[0]].append(i[3])
        # inserta nodos a la grafica
        for i in list(self.nodes.values()):
            ax.add_patch(plt.Circle(i.pos(), 0.0001))
        # grafica las aristas
        for i in self.adj:
            for j in self.adj[i]:
                x, y = self.nodes[i].line(self.nodes[j])
                plt.plot(x, y)
        plt.show()

    # def _find(self, a, b, distance):
    #     h = self.nodes[a].h(self.nodes[b])
    #     for i in self.adj[a]
    #     return False

    def find(self, a, b):
        fig, ax = plt.subplots()
        found = False
        while not found:
            if self.nodes[a].pos() == self.nodes[b].pos():
                found = True
            else:
                next_node = -1
                min = -1.0
                for i in self.adj[a]:
                    distance = self.nodes[i].h(self.nodes[b])
                    if distance > min:
                        min = distance
                        next_node = i
                if next_node == -1: return next_node

    #     plt.show()