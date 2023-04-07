from math import cos, acos, sin, radians, asin, sqrt
from functools import partial
from Graph import UndirectedGraph
from search_algorithms import (
    a_star_search,
    depth_first_search,
    breadth_first_search,
    greedy_search,
    uniform_cost_search,
    depth_limited_search,
    iterative_deepening
)

from centrality import *


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


def h_longitude_latitude_distance(node1, node2):
    long_lat = {
        "Oradea": [47.0465, 21.9189],
        "Zerind": [46.6225, 21.5174],
        "Sibiu": [45.7936, 24.1213],
        "Arad": [46.1866, 21.3123],
        "Timisoara": [45.7489, 21.2087],
        "Rimnicu Vilcea": [45.0997, 24.3693],
        "Fagaras": [45.8416, 24.9731],
        "Lugoj": [45.6910, 21.9035],
        "Bucharest": [44.4268, 26.1025],
        "Pitesti": [44.8565, 24.8692],
        "Craiova": [44.3302, 23.7949],
        "Mehadia": [44.9041, 22.3645],
        "Drobeta": [44.6369, 22.6597],
        "Giurgiu": [43.9037, 25.9699],
        "Urziceni": [44.7181, 26.6453],
        "Hirsova": [44.6893, 27.9457],
        "Eforie": [44.0491, 28.6527],
        "Vaslui": [46.6407, 27.7276],
        "Iasi": [47.1585, 27.6014],
        "Neamt": [46.9759, 26.3819]
    }

    lat1, lon1 = map(radians, long_lat[node1])
    lat2, lon2 = map(radians, long_lat[node2])

    # return acos(sin(lat1)*sin(lat2)+cos(lat1)*cos(lat2)*cos(lon2-lon1))*6371
    a = 0.5 - cos((lat2-lat1))/2 + cos(lat1) * \
        cos(lat2) * (1-cos((lon2-lon1)))/2
    return 12742 * asin(sqrt(a))  # 2*R*asin...


def h_straight_line_distance_to_bucharest(node):
    # straight line distance from node to Bucharest
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


if __name__ == "__main__":
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

    print("<<<<<<<<<<<<<<<< Greedy >>>>>>>>>>>>>")
    path = greedy_search(road_map, "Arad", "Bucharest",
                         h_straight_line_distance_to_bucharest)
    print(path)
    path = greedy_search(road_map, "Craiova", "Bucharest",
                         h_straight_line_distance_to_bucharest)
    print(path)

    print("<<<<<<<<<<<<<<<< A star search >>>>>>>>>>>>>")
    path = a_star_search(road_map, "Arad", "Bucharest",
                         h_straight_line_distance_to_bucharest)
    print(path)
    path = a_star_search(road_map, "Craiova", "Bucharest",
                         h_straight_line_distance_to_bucharest)
    print(path)
    path = a_star_search(road_map, "Neamt", "Bucharest",
                         h_straight_line_distance_to_bucharest)
    print(path)
    path = a_star_search(road_map, "Pitesti", "Bucharest",
                         h_straight_line_distance_to_bucharest)
    print(path)
    path = a_star_search(road_map, "Bucharest",
                         "Bucharest", h_straight_line_distance_to_bucharest)
    print(path)

    bucharest_long_lat = partial(h_longitude_latitude_distance, "Bucharest")

    print(sorted([(bucharest_long_lat(node), h_straight_line_distance_to_bucharest(
        node), node) for node in road_map.nodes]))

    print("<<<<<<<<<<<<<<<< A star search [long-lat]>>>>>>>>>>>>>")
    path = a_star_search(road_map, "Arad", "Bucharest",
                         bucharest_long_lat)
    print(path)
    path = a_star_search(road_map, "Craiova", "Bucharest",
                         bucharest_long_lat)
    print(path)
    path = a_star_search(road_map, "Neamt", "Bucharest",
                         bucharest_long_lat)
    print(path)
    path = a_star_search(road_map, "Pitesti", "Bucharest",
                         bucharest_long_lat)
    print(path)
    path = a_star_search(road_map, "Bucharest",
                         "Bucharest", bucharest_long_lat)
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

    print("\n\nCentrality\n")
    print("Closeness\n", closeness_centrality(road_map))

    # road_map = UndirectedGraph()
    # road_map.add_edge("a", "b", 100)
    # road_map.add_edge("a", "c", 50)
    # road_map.add_edge("c", "b", 50)
    # road_map.add_edge("b", "d", 1)
    # road_map.add_edge("c", "d", 1)
    # road_map.add_edge("d", "e", 1)
    # road_map.add_edge("c", "e", 52)
    # road_map.add_node("f")
    # road_map.add_edge("k", "m", 1)
    print(betweeness_centrality(road_map))
