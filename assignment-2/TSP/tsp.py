import argparse

# Define the command-line arguments
parser = argparse.ArgumentParser(description='Solve the TSP using a specified algorithm')
parser.add_argument('--algorithm', type=str, choices=['hill_climbing', 'simulated_annealing', 'ga'], default='hill_climbing',
                    help='the algorithm to use (default: hill_climbing)')
parser.add_argument('--file', type=str, required=True,
                    help='the path to the file containing the TSP data')

# Parse the command-line arguments
args = parser.parse_args()

# Load the TSP data from the file
with open(args.file, 'r') as f:
    cities = []
    for line in f:
        x, y = map(float, line.split())
        cities.append((x, y))

# Solve the TSP using the specified algorithm
if args.algorithm == 'hill_climbing':
    from hill_climbing import hill_climbing
    tour, dist = hill_climbing(cities, max_iter=1000)
elif args.algorithm == 'simulated_annealing':
    from simulated_annealing import simulated_annealing
    tour, dist = simulated_annealing(cities, init_temp=1000, cooling_rate=0.99, max_iter=10000)
else:
    from genetic_algorithm import genetic_algorithm
    tour, dist = genetic_algorithm(cities, pop_size=50, elite_size=10, mutation_rate=0.01, max_iter=100)

# Print the results
print("Algorithm:", args.algorithm)
print("File:", args.file)
print("Best tour found:", tour)
print("Total distance:", dist)