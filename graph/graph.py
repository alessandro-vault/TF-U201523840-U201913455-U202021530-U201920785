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
    
    
    def __init__(self, points):
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
            if self.nodes[a].coords() == self.nodes[b].coords():
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


def run():
    points = list()
    with open('intersections.csv' , 'r') as csvfile:
        csv_file_reader = csv.reader(csvfile,delimiter=',')
        for row in csv_file_reader:
            line = row[0].split(';')
            if float(line[11]) > -11.0 or float(line[11]) < -13.0 or float(line[12]) > -76 or float(line[12]) < -77.4 or float(line[13]) > -11.0 or float(line[13]) < -13.0 or float(line[14]) > -76 or float(line[14]) < -77.4: continue
            points.append([float(line[5]),float(line[12]),float(line[11]),float(line[6]),float(line[14]),float(line[13])])
    #points = [[1,1,2,2,3,4],[2,3,4,3,5,7],[3,5,7,4,5,2],[4,5,2,5,1,1],[5,1,1,1,1,2],[2,3,4,4,5,2]]
    new_map = graph(points)
    #new_map.find(1, 2)
    print('ok') #bandera
    pass


if __name__ == '__main__':
    run()