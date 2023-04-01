from search_algorithms import breadth_first_search


def closeness(node_1, node_2):
    path = breadth_first_search(node_1, node_2)

    if len(path) == 0:
        return float("inf")
    
    return len(path) - 1