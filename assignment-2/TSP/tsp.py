import argparse
from graph import UndirectedGraph
from collections import defaultdict
from hill_climbing import hill_climbing
# from simulated_annealing import simulated_annealing
from genetic_algorithm import genetic_algorithm


# Define the command-line arguments
parser = argparse.ArgumentParser(description='Solve the TSP using a specified algorithm')
parser.add_argument('--algorithm', type=str, choices=['hill_climbing', 'simulated_annealing', 'ga'], default='hill_climbing',
                    help='the algorithm to use (default: hill_climbing)')
parser.add_argument('--file', type=str, required=True,
                    help='the path to the file containing the TSP data')


args = parser.parse_args()
graph = UndirectedGraph()


with open(args.file) as file:
    cities = set()
    for line in file.readlines()[1:]:
        city_1, city_2, distance = line.split("    ")

        distance = int(distance)


        graph.add_edge(city_1, city_2, distance)
        cities.add(city_1)
        cities.add(city_2)

    cities = list(cities)



# Solve the TSP using the specified algorithm
if args.algorithm == 'hill_climbing':
    tour, dist = hill_climbing(cities=cities, graph=graph, generation=1000)

# elif args.algorithm == 'simulated_annealing':
#     tour, dist = simulated_annealing(cities, max_iter=10000)

else:
    tour, dist = genetic_algorithm(cities=cities, 
                                   graph=graph, 
                                   population_size=100, 
                                   percent=0.7, 
                                   generation=100)




print("Algorithm:", args.algorithm)
print("Best tour found:", tour)
print("Total distance:", dist)