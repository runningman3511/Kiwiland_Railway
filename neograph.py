import sys
from node import Node

class Neograph:
    def __init__(self):

        self.node_list = {}
        self.node_count = 0

    def add_node(self, name):
        self.node_count = self.node_count+1

        node = Node(name)
        self.node_list[name] = node

        return node

    def add_edge(self, start, end, weight=0):

        if start not in self.node_list:
            self.add_node(start)

        if end not in self.node_list:
            self.add_node(end)
        self.node_list[start].neighbour_add(self.node_list[end], weight)

    def solve_distance(self,input_data):
        distance=0
        input=input_data.split('-')
        start_town=self.node_list[input[0]]
        input.pop(0) # Remove start town from list
        
        for next_stop in input:
            next_stop_object=self.node_list[next_stop]
            try:
                length_to_next_stop=start_town.one_way_connections_to[next_stop_object]
            except:
                return f'NO SUCH ROUTE' 
            distance=distance+length_to_next_stop
            start_town=next_stop_object

        
        return distance

    def solve_same_start_stop_maximum(self, original_town, end_town, max_stops):
        routes_found=self.solve_same_start_stop_maximum_recursive(original_town, end_town, max_stops, 0)
        return routes_found

    def solve_same_start_stop_maximum_recursive(self, original_town, end_town, max_stops, routes_found, start_town=None, number_of_stops=-1,path=''):

        if number_of_stops > max_stops:
            return routes_found
        if start_town is None:
            start_town=self.node_list[original_town]
        else:
            start_town=self.node_list[start_town]
        path=path+start_town.name

        for next_stop in start_town.one_way_connections_to:
            number_of_stops=number_of_stops+1
            if next_stop.name == end_town and max_stops >= number_of_stops and number_of_stops > 0:
                path=path+next_stop.name
                routes_found = routes_found + 1
                return routes_found
            
            routes_found = self.solve_same_start_stop_maximum_recursive(original_town, end_town, max_stops, routes_found,next_stop.name, number_of_stops,path)
        return routes_found
        
    def solve_start_stop_exact(self, original_town, end_town, max_stops):
        routes_found=self.solve_start_stop_exact_recursive(original_town, end_town, max_stops, 0)
        return routes_found

    def solve_start_stop_exact_recursive(self, original_town, end_town, max_stops, routes_found, start_town=None, number_of_stops=-1,path=''):

        if len(path) > max_stops:
            return routes_found
        if start_town is None:
            start_town=self.node_list[original_town]
        else:
            start_town=self.node_list[start_town]
        path=path+start_town.name

        for next_stop in start_town.one_way_connections_to:
            number_of_stops=number_of_stops+1
            path_len=len(path)
            if next_stop.name == end_town and max_stops == path_len and number_of_stops > 0:
                path=path+next_stop.name
                routes_found = routes_found + 2
                return routes_found
            routes_found = self.solve_start_stop_exact_recursive(original_town, end_town, max_stops, routes_found,next_stop.name, number_of_stops,path)
        return routes_found
  
    def solve_shortest_routev2(self, original_town, end_town):
        paths_fond=self.solve_shortest_route_recursivev2(original_town, end_town)
        distance_list = []
        for path in paths_fond:
            distance_list.append(self.get_lengh_of_route(path))
        distance_list=sorted(distance_list)
        return distance_list[0]

    def solve_shortest_route_recursivev2(self, original_town, end_town, start_town=None,path='',paths_fond=[]):
        first_itteration = False
        if start_town is None:
            start_town=self.node_list[original_town]
            first_itteration=True
        else:
            start_town=self.node_list[start_town]
        path=path+start_town.name

        if len(path) > 50:
            return paths_fond

        for next_stop in start_town.one_way_connections_to:
            next_stop_path=path+next_stop.name
            if next_stop.name == end_town  and len(path)  > 0:
                path=path+next_stop.name
                paths_fond.append(path)
                return paths_fond
            
            min_distance = self.solve_shortest_route_recursivev2(original_town, end_town,next_stop.name,path,paths_fond)
        return paths_fond

    def solve_route_calculation_recursive_v3(self, original_town, end_town, start_town=None,path='',paths_fond=[]):
        first_itteration = False
        if start_town is None:
            start_town=self.node_list[original_town]
            first_itteration=True
        else:
            start_town=self.node_list[start_town]
        path=path+start_town.name

        if len(path) > 50:
            return paths_fond

        for next_stop in start_town.one_way_connections_to:
            next_stop_path=path+next_stop.name
            if self.get_lengh_of_route(next_stop_path) > 30:
                return paths_fond
            if next_stop.name == end_town  and len(path)  > 0:
                paths_fond.append(path+next_stop.name)
            
            min_distance = self.solve_route_calculation_recursive_v3(original_town, end_town,next_stop.name,path,paths_fond)
        return paths_fond

    def solve_number_of_different_routes(self,original_town, end_town,max_distance):
        paths_fond=self.solve_route_calculation_recursive_v3(original_town, end_town)
        distance_list = []
        distance_list_less_then_desired =0
        distance_list_less_then_desired_list =[]
        for path in paths_fond:
            lenght = self.get_lengh_of_route(path)
            if lenght < max_distance:
                distance_list_less_then_desired = distance_list_less_then_desired + 1
        return distance_list_less_then_desired

    def get_lengh_of_route(self,path):
        i=0
        size_of_path=len(path)
        distance = 0 
        while i < (size_of_path-1):
            start_node = self.node_list[path[i]]
            next_node = self.node_list[path[i+1]]
            distance = distance + start_node.one_way_connections_to[next_node]
            i=i+1
        return distance

    def print_nodes(self):
        for node in self.node_list:
            connected_to=self.node_list[node].connected_to
            print(self.node_list[node].name)