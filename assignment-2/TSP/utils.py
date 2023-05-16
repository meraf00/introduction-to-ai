import os
import time
import random
from math import radians, cos, sqrt, asin
from graph import *
from heapq import heapify, heappop, heappush

cities = ['Oradea', 'Zerind', 'Arad', 'Timisoara', 'Lugoj', 'Mehadia', 'Drobeta', 'Craiova', 'Sibiu', 'Rimnicu Vilcea',
          'Fagaras', 'Pitesti', 'Giurgiu', 'Bucharest', 'Urziceni', 'Eforie', 'Hirsova', 'Vaslui', 'Iasi', 'Neamt']

def load_coords():

    romania_coord = os.path.join(os.path.dirname(
        __file__), "romania-data/romania-coords.txt")

    city_coords = {}

    with open(romania_coord) as file:
        for line in file.readlines()[1:]:
            city, lat, long = line.split("    ")
            lat = float(lat)
            long = float(long)

            city_coords[city] = [lat, long]

    return city_coords


def get_path_cost(city1, city2, graph):
    queue = []
    heappush(queue, [0, city1, None])
    while queue:

        cost, cur, parent = heappop(queue)

        if cur == city2:
            return cost

        for neighbour in graph.neighbours(cur):
            if neighbour[0] != parent:
                new_cost = neighbour[1]
                heappush(queue, ([cost + new_cost, neighbour[0], cur]))



def calculate_cost(chromosome, graph):

    cost = 0
    visited = set()

    
    for i in range(1, 20):

        city1, city2 = chromosome[i - 1], chromosome[i]
        
        visited.add(city1)
        
        path_cost = get_path_cost(city1=city1, city2=city2, graph=graph)

        cost += path_cost

        if city2 in visited:
            cost += 1000


    return cost


def load_city_graph(distance_unit="miles"):
    romania_file = os.path.join(os.path.dirname(
        __file__), "romania-data/romania-road-distance.txt")

    graph = UndirectedGraph()

    with open(romania_file) as file:
        for line in file.readlines()[1:]:
            city_1, city_2, distance = line.split("    ")

            distance = int(distance)

            if distance_unit == "km":
                distance *= 1.60934

            graph.add_edge(city_1, city_2, distance)

    return graph


def romania_coord_distance_km(city_1, city_2):
    """Returns the straight line distance in kilometers between two cities."""

    coord = load_coords()

    lat1, lon1 = map(radians, coord[city_1])
    lat2, lon2 = map(radians, coord[city_2])

    a = 0.5 - cos((lat2-lat1))/2 + cos(lat1) * \
        cos(lat2) * (1-cos((lon2-lon1)))/2
    return 12742 * asin(sqrt(a))  # 2*R*asin...


# def calculate_cost(graph, path):
#     if not path:
#         return float("inf")

#     cost = 0

#     for i in range(len(path) - 1):
#         node = path[i]

#         for neighbour, weight in graph.graph[node]:
#             if neighbour == path[i + 1]:
#                 cost += weight
#                 break

#     return cost


def benchmark(algorithm, args, run_n_times=10):
    """
    Calculate average runing time for given function

    Args:
        algorithm (Callable): the function to test
        args (Any): the arguments to pass to the function
        run_n_times (int): number of times to run the algorithm

    Return:
        tuple(float, int) : 
            mean_run_time   - average running time of algorithm        
            solution_length - path length
    """

    mean_run_time = 0
    solution_length = 0

    for _ in range(run_n_times):
        start_time = time.perf_counter()
        solution = algorithm(**args)
        mean_run_time += time.perf_counter() - start_time

        solution_length = len(solution)

    return (mean_run_time / run_n_times, solution_length)


