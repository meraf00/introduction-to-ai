import os
import time
import random
from math import radians, cos, sqrt, asin
from graph import *


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


def calculate_cost(graph, path):
    if not path:
        return float("inf")

    cost = 0

    for i in range(len(path) - 1):
        node = path[i]

        for neighbour, weight in graph.graph[node]:
            if neighbour == path[i + 1]:
                cost += weight
                break

    return cost


def generate_graph(n_nodes: int, edge_probability: float, min_weight: float, max_weight: float, allow_edge_loop: bool = False) -> UndirectedGraph:
    """
    Generates graph with specified number of nodes.

    Args:
        n_nodes (int) - number of nodes
        edge_probability (float) - probability of finding edge between two nodes (range [0 - 1])
        min_weight (float) - minimum weight to assign per generated edges between nodes
        max_weight (float) - maximum weight to assign per generated edges between nodes
        loop (bool) - allow edge loop on nodes


    Returns:
        UndirectedGraph
    """

    graph = UndirectedGraph()

    for node in range(n_nodes):
        graph.add_node(node)

    i = j = 0
    nodes = graph.nodes

    random.seed(time.time())

    for i in range(n_nodes):
        for j in range(i, n_nodes):

            if not allow_edge_loop and i == j:
                continue

            if random.random() <= edge_probability:
                graph.add_edge(nodes[i], nodes[j], round(
                    random.uniform(min_weight, max_weight), 2))

    return graph


def generate_heuristic_function(graph, goal_node, estimation_error: float = 0.2):
    """Generates random admissible heuristic function for given graph.

    Args:
        graph - Graph
        goal_node - for which goal node are we are estimating cost
        estimation_error (float) - percentage error for heuristic estimation

    Returns:
        Function (node -> estimation) - a function that returns heuristic estimation for given node 
    """

    estimations = {}

    nodes = graph.nodes

    random.seed(time.time())

    for node in range(len(nodes)):
        if node == goal_node:
            estimations[node] = 0
            continue

        # a star would have been faster but we dont have heuristic function
        path = uniform_cost_search(graph, node, goal_node)

        real_cost = calculate_cost(graph, path)

        # underestimate to make it admissible
        estimated_cost = real_cost - real_cost * \
            random.uniform(0, estimation_error)

        estimations[node] = estimated_cost

    return lambda node: estimations[node]


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
