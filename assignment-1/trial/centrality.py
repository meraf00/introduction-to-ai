from collections import defaultdict
from search_algorithms import breadth_first_search, uniform_cost_search
from heapq import heappop, heappush


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

    for node in graph.nodes:
        degree_centrality[node] = len(graph.neighbours(node))

    return degree_centrality


def closeness_centrality(graph):
    closeness_centrality = {}

    for node in graph.nodes:

        path_cost_sum = 0

        for other_node in graph.nodes:
            if node != other_node:
                shortest_path = uniform_cost_search(graph, node, other_node)
                path_cost_sum += get_path_cost(graph, shortest_path)

        closeness_centrality[node] = (len(graph.nodes) - 1) / path_cost_sum

    return closeness_centrality


def betweeness_centrality(graph):
    betweeness_centrality = {}

    for node in graph.nodes:
        betweeness_centrality[node] = node_betweeness_centrality(graph, node)

    return betweeness_centrality


def node_betweeness_centrality(graph, target_node):
    betweeness = 0

    for start_node in graph.nodes:
        if start_node == target_node:
            continue
        
        shortest_paths = find_best_paths_to_all_nodes(graph, start_node)
        
        for dest_node in shortest_paths.keys():
            if dest_node == target_node:
                continue
            
            total_shortest_path_from_s_to_d_paths = len(shortest_paths[dest_node])

            short_paths_from_s_to_d_containing_target = 0

            for paths in shortest_paths.values():                
                for path in paths:
                    if target_node in path:
                        short_paths_from_s_to_d_containing_target += 1

            betweeness += short_paths_from_s_to_d_containing_target / total_shortest_path_from_s_to_d_paths
    
    return betweeness


def find_best_paths_to_all_nodes(graph, start_node):
    paths = defaultdict(list)
    paths[start_node].append([start_node])

    path_cost = {}
    # best_path_count = defaultdict(int)
    # best_path_count[start_node] = 1

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
                    # best_path_count[neighbour] = best_path_count[current_node]

                elif prev_cost == cost + weight:
                    paths[neighbour].extend(
                        [path[:] + [neighbour] for path in paths[current_node]])
                    # best_path_count[neighbour] += best_path_count[current_node]

    return paths


def eigenvector_centrality(graph):
    pass