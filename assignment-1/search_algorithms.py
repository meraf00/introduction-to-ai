from collections import deque, defaultdict
from heapq import heappop, heappush


def build_path(path_map: dict, start_node, end_node):    
    path = []
        
    current = end_node
    while True:
        path.append(current)

        if current == start_node:
            break

        current = path_map[current]
    
    path.reverse()

    return path
    

def depth_first_search(graph, start_node, end_node): 
    path_map = {}

    stack = [start_node]

    visited = set()

    while stack:
        current_node = stack.pop()

        if current_node == end_node:
            return build_path(path_map, start_node, end_node)

        visited.add(current_node)

        for neighbour, _ in graph.neighbours(current_node):
            if neighbour not in visited:
                stack.append(neighbour)
                path_map[neighbour] = current_node

    return []

 
def breadth_first_search(graph, start_node, end_node):
    path_map = {}
    path_cost = {}

    queue = deque([(0, start_node)])

    visited = set()

    while queue:
        cost, current_node = queue.popleft()

        if current_node == end_node:
            return build_path(path_map, start_node, end_node)

        visited.add(current_node)

        for neighbour, _ in graph.neighbours(current_node):
            if neighbour not in visited:
                queue.append((cost + 1, neighbour))
                
                if path_cost.get(neighbour, float("inf")) > cost + 1:
                    path_map[neighbour] = current_node
                    path_cost[neighbour] = cost + 1

    return []


def uniform_cost_search(graph, start_node, end_node):
    path_map = {}
    path_cost = {}

    priority_queue = [(0, start_node)]

    visited = set()

    while priority_queue:
        cost, current_node = heappop(priority_queue)

        if current_node == end_node:
            return build_path(path_map, start_node, end_node)

        visited.add(current_node)

        for neighbour, weight in graph.neighbours(current_node):
            if neighbour not in visited:
                heappush(priority_queue, (cost + weight, neighbour))

                if path_cost.get(neighbour, float("inf")) > cost + weight:
                    path_map[neighbour] = current_node
                    path_cost[neighbour] = cost + weight

    return []


def depth_limited_search(graph, start_node, end_node, depth_limit=0):
    current_path = [start_node]

    visited = set(current_path)

    path = []

    def backtrack(node, depth_limit):
        nonlocal path

        # path found
        if node == end_node:
            path = current_path[:]
            return

        # path not found
        if depth_limit == 0:
            return

        # expand
        for neighbour, _ in graph.neighbours(node):
            # avoid cycle
            if neighbour in visited:
                continue

            current_path.append(neighbour)
            visited.add(neighbour)

            backtrack(neighbour, depth_limit - 1)

            visited.remove(neighbour)
            current_path.pop()

    backtrack(start_node, depth_limit)

    return path


def iterative_deepening(graph, start_node, end_node, max_depth_limit=30):
    for depth in range(max_depth_limit):
        solution = depth_limited_search(
            graph, start_node, end_node, depth_limit=depth)

        if solution:
            return solution

    return []


def greedy(graph, start_node, end_node, heuristic_func):
    """
    Args:
        graph - graph to traverse
        start_node - inital node
        end_node - goal node
        heuristic_func - function to estimate cost


    Returns:
        list - path form start_node to end_node

    `heuristic_func` - will be called with node. It should return
    estimated cost of path from `current_node` to `end_node`.
    """

    if start_node == end_node:
        return [start_node]

    # choose the best node from alternative (min of cost estimated by heuristic_func)
    best_node = None
    best_cost = float("inf")

    for neighbour, _ in graph.neighbours(start_node):
        estimated_cost = heuristic_func(neighbour)

        if estimated_cost < best_cost:
            best_cost = estimated_cost
            best_node = neighbour

    return [start_node] + greedy(graph, best_node, end_node, heuristic_func)


def a_star(graph, start_node, end_node, heuristic_func):
    # alias
    h = heuristic_func

    path_map = {}
    path_cost = {}

    priority_queue = [(h(start_node), start_node)]

    visited = set()

    while priority_queue:

        # est_total_cost = cost incurred so far + estimated future cost
        est_total_cost, current_node = heappop(priority_queue)

        current_incurred_cost = est_total_cost - h(current_node)

        if current_node == end_node:
            return build_path(path_map, start_node, end_node)

        visited.add(current_node)

        for neighbour, weight in graph.neighbours(current_node):

            if neighbour not in visited:

                neighbour_est_total_cost = \
                    current_incurred_cost + weight + h(neighbour)

                heappush(priority_queue, (neighbour_est_total_cost, neighbour))

                if path_cost.get(neighbour, float("inf")) > neighbour_est_total_cost:
                    path_map[neighbour] = current_node
                    path_cost[neighbour] = neighbour_est_total_cost

    return []
