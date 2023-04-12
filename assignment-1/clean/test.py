from graph import *
from utils import *

print(romania_coord_distance_km("Arad", "Bucharest"))
print(romania_coord_distance_km("Arad", "Neamt"))
print(romania_coord_distance_km("Lugoj", "Neamt"))
print(romania_coord_distance_km("Lugoj", "Arad"))




graph = load_city_graph()

for src in ["Arad", "Neamt", "Bucharest", "Rimnicu Vilcea", "Timisoara", "Sibiu", "Zerind", "Oradea"]:
    for dest in ["Arad", "Neamt", "Bucharest", "Rimnicu Vilcea", "Timisoara", "Sibiu", "Zerind", "Oradea"]:
        
        path = greedy_search(graph, src, dest, lambda src_: romania_coord_distance_km(src_, dest))
        print(path)

path = greedy_search(graph, "Arad", "Bucharest", lambda src_: romania_coord_distance_km(src_, dest))
print(path)

print("Aarad" in graph)