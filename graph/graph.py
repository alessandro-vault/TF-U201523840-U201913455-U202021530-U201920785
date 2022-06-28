import time
import matplotlib.pyplot as plt
import numpy as np
import random
import csv

#clase nodo
class Node:
    posx = 0
    posy = 0
    id = 0
    def __init__(self, posx, posy):
        self.posx = posx
        self.posy = posy
    
    #retorna las coordenadas en forma de una tupla
    def coords(self):
        return (self.posx, self.posy)
    
    #retorna una linea entre este y otro nodo
    def line(self, obj):
        x = [self.posx, obj.posx]
        y = [self.posy, obj.posy]
        return x, y

    #distancia entre este nodo y el nodo objetivo 
    def h(self, obj):
        distance = (float(self.posx - obj.posx)**2.0 + float(self.posy - obj.posy)**2.0)**0.5
        return distance


class Edge:
    id1 = 0
    id2 = 0
    def __init__(self, id1, id2):
        self.id1 = id1
        self.id2 = id2


class graph:
    nodes = dict()
    adj = dict()
    
    
    def __init__(self, points, a, b):
        fig, ax = plt.subplots()
        ax.set_aspect("equal", adjustable="datalim")
        ax.set_box_aspect(0.5)
        ax.autoscale()
        plt.title('Mapa')
        #añade nodos y arista  
        for i in points:
            self.nodes[i[0]] = Node(i[1], i[2])
            self.nodes[i[3]] = Node(i[4], i[5])
            if i[0] not in self.adj:
                self.adj[i[0]] = list()
            self.adj[i[0]].append(i[3])
        #inserta nodos a la grafica
        for i in list(self.nodes.values()):
            ax.add_patch(plt.Circle(i.coords(), 0.0001))
        #grafica las aristas
        for i in self.adj:
            for j in self.adj[i]:
                x, y = self.nodes[i].line(self.nodes[j])
                plt.plot(x, y, 'green')
        path, paths = self.find(a, b)
        for item in paths:
            j = 0
            while j < len(item) - 2:
                x, y = self.nodes[item[j]].line(self.nodes[item[j + 1]])
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
        #evita el error al intentar acceder a la lista de adj de un nodo que no lo tiene
        try: self.adj[a]
        except:
            ban_list.append(a)
            path.append(next_node)
            return path, ban_list
        #busca el siguiente nodo mas cercano al objetivo
        for i in self.adj[a]:
            if h > self.nodes[i].h(self.nodes[b]) and not i in ban_list:
                h = self.nodes[i].h(self.nodes[b])
                next_node = i
        if next_node == b:
            path.append(b)
        elif next_node != -1:
            path.append(next_node)
            path, ban_list = self._next(next_node, b, path, ban_list)
        else:
            ban_list.append(a)
            path.append(next_node)
            return path, ban_list
        return path, ban_list
    

    def _find(self,a, b, ban_list):
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


def run():
    points = list()
    with open('intersections.csv' , 'r') as csvfile:
        csv_file_reader = csv.reader(csvfile,delimiter=',')
        for row in csv_file_reader:
            line = row[0].split(';')
            if float(line[11]) > -11.0 or float(line[11]) < -13.0 or float(line[12]) > -76 or float(line[12]) < -77.4 or float(line[13]) > -11.0 or float(line[13]) < -13.0 or float(line[14]) > -76 or float(line[14]) < -77.4: continue
            points.append([float(line[5]),float(line[12]),float(line[11]),float(line[6]),float(line[14]),float(line[13])])
    a, b = 1, 210
    new_map = graph(points, a, b)
    pass


if __name__ == '__main__':
    run()
