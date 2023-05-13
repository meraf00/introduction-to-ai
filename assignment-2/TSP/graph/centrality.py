from collections import defaultdict
from heapq import heappop, heappush
import math
from .search_algorithms import uniform_cost_search


def get_path_cost(graph, path):
    if not path:
        return float("inf")

    current = path[0]

    cost = 0

    for i in range(1, len(path)):
        node = path[i]
        for neighbour, weight in graph.neighbours(current):
            if neighbour == node:
                cost += weight
                current = neighbour
                break

    return cost


def degree_centrality(graph):
    degree_centrality = {}

    number_of_nodes = len(graph)

    for node in graph.nodes:
        degree_centrality[node] = len(
            graph.neighbours(node)) / (number_of_nodes - 1)

    return degree_centrality


def closeness_centrality(graph):
    number_of_nodes = len(graph)

    closeness_centrality = {}

    for node in graph.nodes:

        path_cost_sum = 0

        for other_node in graph.nodes:
            if node != other_node:
                shortest_path = uniform_cost_search(graph, node, other_node)
                path_cost_sum += get_path_cost(graph, shortest_path)

        closeness_centrality[node] = (number_of_nodes - 1) / path_cost_sum

    return closeness_centrality


def betweeness_centrality(graph):
    betweeness_centrality = {}

    number_of_nodes = len(graph)

    scale = 2 / ((number_of_nodes - 1) * (number_of_nodes - 2))

    for node in graph.nodes:
        betweeness_centrality[node] = node_betweeness_centrality(
            graph, node) * scale

    return betweeness_centrality


# betweeness centrality helper
def node_betweeness_centrality(graph, target_node):
    # target_node is the intercepting node

    betweeness = 0

    for start_node in graph.nodes:
        if start_node == target_node:
            continue

        shortest_paths = find_best_paths_to_all_nodes(graph, start_node)

        for dest_node in shortest_paths.keys():
            if dest_node == target_node:
                continue

            total_shortest_path_from_s_to_d_paths = len(
                shortest_paths[dest_node])

            short_paths_from_s_to_d_containing_target = 0

            for path in shortest_paths[dest_node]:
                if target_node in path:
                    short_paths_from_s_to_d_containing_target += 1

            betweeness += short_paths_from_s_to_d_containing_target / \
                total_shortest_path_from_s_to_d_paths

    return betweeness


# betweeness centrality helper
def find_best_paths_to_all_nodes(graph, start_node):
    paths = defaultdict(list)
    paths[start_node].append([start_node])

    path_cost = {}

    priority_queue = [(0, start_node)]

    visited = set()

    while priority_queue:
        cost, current_node = heappop(priority_queue)

        visited.add(current_node)

        for neighbour, weight in graph.neighbours(current_node):
            if neighbour not in visited:
                heappush(priority_queue, (cost + weight, neighbour))

                prev_cost = path_cost.get(neighbour, float("inf"))

                if prev_cost > cost + weight:
                    paths[neighbour] = [path[:] + [neighbour]
                                        for path in paths[current_node]]
                    path_cost[neighbour] = cost + weight

                elif prev_cost == cost + weight:
                    paths[neighbour].extend(
                        [path[:] + [neighbour] for path in paths[current_node]])

    return paths


def eigenvector_centrality(graph, max_iter=100, tolerance=1.0e-5):

    nodes_init = {v: 1 for v in graph.nodes}

    nodes_init_sum = sum(nodes_init.values())

    iteration = {node: centrality / nodes_init_sum for node,
                 centrality in nodes_init.items()}

    number_of_nodes = len(graph)

    for _ in range(max_iter):
        last_iter = iteration
        iteration = last_iter.copy()

        for node in iteration:
            for nbr, _ in graph.neighbours(node):
                iteration[nbr] += last_iter[node]

        norm = math.hypot(*iteration.values()) or 1
        iteration = {node: centrality / norm for node,
                     centrality in iteration.items()}

        if sum(abs(iteration[n] - last_iter[n]) for n in iteration) < number_of_nodes * tolerance:
            return iteration


def katz_centrality(graph, alpha=0.1, beta=1.0, max_iter=100, tolerance=1.0e-5):
    iteration = {v: 0 for v in graph.nodes}

    number_of_nodes = len(graph)

    for _ in range(max_iter):
        last_iter = iteration

        iteration = dict.fromkeys(last_iter, 0)

        for node in iteration:
            for nbr, _ in graph.neighbours(node):
                iteration[nbr] += last_iter[node]

        for node in iteration:
            iteration[node] = alpha * iteration[node] + beta

        error = sum(abs(iteration[n] - last_iter[n]) for n in iteration)
        if error < number_of_nodes * tolerance:
            try:
                s = 1.0 / math.hypot(*iteration.values())
            except ZeroDivisionError:
                s = 1.0

            # normalize
            for node in iteration:
                iteration[node] *= s

            return iteration
