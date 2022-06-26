class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def pos(self):
        return self.x, self.y

    def line(self, node):
        return [self.x, node.x], [self.y, node.y]

    def distance_between(self, node):
        return ((self.x - node.x) ** 2 + (self.y - node.y) ** 2) ** 0.5

    def __repr__(self):
        return f'<Node lat:{self.x}, lon:{self.y}>'
