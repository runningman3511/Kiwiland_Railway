class Node:
    def __init__(self, name):
        self.name = name
        self.one_way_connections_to = {}

    def neighbour_add(self, neighbour, weight=0):
        weight=int(weight)
        self.one_way_connections_to[neighbour] = weight

    def get_connections(self):
        return self.one_way_connections_to.keys()

    def get_weight(self, neighbor):
        return self.one_way_connections_to[neighbor]