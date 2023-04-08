import random
from graph import *
from utils import generate_graph, generate_heuristic_function, benchmark


def generate_test_graphs():
    test_graphs = []

    for node_count in [10, 20, 30, 40]:
        for edge_probability in [0.2, 0.4, 0.6, 0.8]:
            graph = generate_graph(
                node_count, edge_probability, min_weight=1, max_weight=100)
            test_graphs.append(graph)

    return test_graphs


def generate_search_problems(graph):
    """Randomly selects 5 nodes from graph and pairs all of them them to create search problem"""

    selected_nodes = random.sample(graph.nodes, k=5)

    start_end_nodes = []

    for i in range(len(selected_nodes)):
        for j in range(i + 1, len(selected_nodes)):
            start_end_nodes.append((selected_nodes[i], selected_nodes[j]))

    return start_end_nodes


def test_performance(run_n_times=5):
    # generate test graph
    test_graphs = generate_test_graphs()

    # search algorithms to test
    search_algorithms = [(depth_first_search, {}),
                         (breadth_first_search, {}),
                         (uniform_cost_search, {}),
                         (iterative_deepening, {"max_depth_limit": 100}),
                         (greedy_search, {"heuristic_func": None}),
                         (a_star_search, {"heuristic_func": None})]

    # track algorithm performance
    algorithm_performance = {depth_first_search: [],
                             breadth_first_search: [],
                             uniform_cost_search: [],
                             iterative_deepening: [],
                             greedy_search: [],
                             a_star_search: []}

    for graph in test_graphs:
        search_problems = generate_search_problems(graph)

        for algorithm, args in search_algorithms:

            algorithm_running_time = 0

            for start_node, goal_node in search_problems:
                # generate heuristic function for this search problem
                heuristic_function = generate_heuristic_function(
                    graph, goal_node=goal_node)

                if "heuristic_func" in args:
                    args.update(
                        {
                            "graph": graph,
                            "start_node": start_node,
                            "end_node": goal_node,
                            "heuristic_func": heuristic_function
                        }
                    )

                else:
                    args.update(
                        {
                            "graph": graph,
                            "start_node": start_node,
                            "end_node": goal_node
                        }
                    )

                runtime, path_length = benchmark(
                    algorithm, args, run_n_times=run_n_times)
                algorithm_running_time += runtime

                algorithm_performance[algorithm].append(
                    {
                        "start": start_node,
                        "end": goal_node,
                        "node_count": len(graph.nodes),
                        "runtime": algorithm_running_time,
                        "path_length": path_length
                    }
                )

    return algorithm_performance
