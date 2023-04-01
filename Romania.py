from Graph import UndirectedGraph
from search_algorithms import (
    a_star,
    depth_first_search,
    breadth_first_search,
    greedy,
    uniform_cost_search,
    depth_limited_search,
    iterative_deepening
)


road_map = UndirectedGraph()

road_map.add_edge("Oradea", "Zerind", 71)
road_map.add_edge("Oradea", "Sibiu", 151)
road_map.add_edge("Zerind", "Arad",   75)
road_map.add_edge("Arad", "Sibiu", 140)
road_map.add_edge("Timisoara", "Arad", 118)
road_map.add_edge("Sibiu", "Rimnicu Vilcea", 80)
road_map.add_edge("Sibiu", "Fagaras", 99)
road_map.add_edge("Timisoara", "Lugoj", 111)
road_map.add_edge("Fagaras", "Bucharest", 211)
road_map.add_edge("Rimnicu Vilcea", "Pitesti", 97)
road_map.add_edge("Rimnicu Vilcea", "Craiova", 146)
road_map.add_edge("Lugoj", "Mehadia", 70)
road_map.add_edge("Craiova", "Pitesti", 138)
road_map.add_edge("Craiova", "Drobeta", 120)
road_map.add_edge("Mehadia", "Drobeta", 75)
road_map.add_edge("Bucharest", "Pitesti", 101)
road_map.add_edge("Bucharest", "Giurgiu", 90)
road_map.add_edge("Bucharest", "Urziceni", 85)
road_map.add_edge("Urziceni", "Hirsova", 98)
road_map.add_edge("Hirsova", "Eforie", 86)
road_map.add_edge("Urziceni", "Vaslui", 142)
road_map.add_edge("Vaslui", "Iasi", 92)
road_map.add_edge("Iasi", "Neamt", 87)

print(road_map)
print(road_map.nodes)
print(len(road_map.nodes))

for k, v in road_map._graph.items():
    print(f"{k}, Degree: {len(v)}, {[v for n,  v in v]}")


print("<<<<<<<<<<<<<<<< Depth first search >>>>>>>>>>>>>")
path = depth_first_search(road_map, "Arad", "Arad")
print(path)
path = depth_first_search(road_map, "Arad", "Zerind")
print(path)
path = depth_first_search(road_map, "Arad", "Fagaras")
print(path)
path = depth_first_search(road_map, "Arad", "Neamt")
print(path)


print("<<<<<<<<<<<<<<<< Breadth first search >>>>>>>>>>>>>")
path = breadth_first_search(road_map, "Arad", "Arad")
print(path)
path = breadth_first_search(road_map, "Arad", "Zerind")
print(path)
path = breadth_first_search(road_map, "Arad", "Fagaras")
print(path)
path = breadth_first_search(road_map, "Arad", "Neamt")
print(path)


print("<<<<<<<<<<<<<<<< Uniform cost search >>>>>>>>>>>>>")
path = uniform_cost_search(road_map, "Arad", "Arad")
print(path)
path = uniform_cost_search(road_map, "Arad", "Zerind")
print(path)
path = uniform_cost_search(road_map, "Arad", "Fagaras")
print(path)
path = uniform_cost_search(road_map, "Arad", "Neamt")
print(path)


print("<<<<<<<<<<<<<<<< Depth limited search >>>>>>>>>>>>>")
path = depth_limited_search(road_map, "Arad", "Arad")
print(path)
path = depth_limited_search(road_map, "Arad", "Zerind", depth_limit=1)
print(path)
path = depth_limited_search(road_map, "Arad", "Fagaras", depth_limit=3)
print(path)
path = depth_limited_search(road_map, "Arad", "Arad", 0)
print(path)


print("<<<<<<<<<<<<<<<< Iterative deepening >>>>>>>>>>>>>")
path = iterative_deepening(road_map, "Arad", "Arad")
print(path)
path = iterative_deepening(road_map, "Arad", "Zerind")
print(path)
path = iterative_deepening(road_map, "Arad", "Fagaras")
print(path)
path = iterative_deepening(road_map, "Arad", "Neamt")
print(path)


def h_straight_line_distance(node):
    # sld to Bucharest
    distances = {
        "Oradea":  380,
        "Zerind":  374,
        "Sibiu": 253,
        "Arad":  366,
        "Timisoara":  329,
        "Rimnicu Vilcea":  193,
        "Fagaras":  176,
        "Lugoj":  244,
        "Bucharest":  0,
        "Pitesti":  100,
        "Craiova": 160,
        "Mehadia":  241,
        "Drobeta":  242,
        "Giurgiu":  77,
        "Urziceni":  80,
        "Hirsova":  151,
        "Eforie":  161,
        "Vaslui": 199,
        "Iasi":  226,
        "Neamt": 234
    }

    return distances[node]

print("<<<<<<<<<<<<<<<< Greedy >>>>>>>>>>>>>")
path = greedy(road_map, "Arad", "Bucharest", h_straight_line_distance)
print(path)
path = greedy(road_map, "Craiova", "Bucharest", h_straight_line_distance)
print(path)


print("<<<<<<<<<<<<<<<< A star search >>>>>>>>>>>>>")
path = a_star(road_map, "Arad", "Bucharest", h_straight_line_distance)
print(path)
path = a_star(road_map, "Craiova", "Bucharest", h_straight_line_distance)
print(path)
path = a_star(road_map, "Neamt", "Bucharest", h_straight_line_distance)
print(path)
path = a_star(road_map, "Pitesti", "Bucharest", h_straight_line_distance)
print(path)
path = a_star(road_map, "Bucharest", "Bucharest", h_straight_line_distance)
print(path)

print("<<<<<<<<<<<<<<<< Uniform cost search to Bucharest >>>>>>>>>>>>>")
path = uniform_cost_search(road_map, "Arad", "Bucharest")
print(path)
path = uniform_cost_search(road_map, "Craiova", "Bucharest")
print(path)
path = uniform_cost_search(road_map, "Neamt", "Bucharest")
print(path)
path = uniform_cost_search(road_map, "Pitesti", "Bucharest")
print(path)
path = uniform_cost_search(road_map, "Bucharest", "Bucharest")
print(path)
