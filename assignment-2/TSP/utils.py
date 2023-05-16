import os
import time
import random
from math import radians, cos, sqrt, asin
from graph import *
from heapq import heappop, heappush


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
        path_cost = get_path_cost(city1=city1, city2=city2, graph=graph)
        cost += path_cost

        if city1 in visited:
            cost += 10000
        visited.add(city1)

    if city2 in visited:
        cost += 1000

    return cost



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
