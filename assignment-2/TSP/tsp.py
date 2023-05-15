import random
import utils
from random import randint, shuffle, uniform
from collections import deque


cities = ['Oradea', 'Zerind', 'Arad', 'Timisoara', 'Lugoj', 'Mehadia', 'Drobeta', 'Craiova', 'Sibiu', 'Rimnicu Vilcea',
          'Fagaras', 'Pitesti', 'Giurgiu', 'Bucharest', 'Urziceni', 'Eforie', 'Hirsova', 'Vaslui', 'Iasi', 'Neamt']
graph = utils.load_city_graph()


def generate_population(cities, size):
    population = []

    for _ in range(size):
        chromosome = cities
        shuffle(chromosome)
        population.append(chromosome)

    return population


def get_path_cost(city1, city2):
    queue = deque([[city1, 0, None]])

    while queue:

        cur, cost, parent = queue.popleft()

        if cur == city2:
            return cost

        for neighbour in graph.neighbours(cur):
            if neighbour[0] != parent:
                new_cost = neighbour[1]
                queue.append([neighbour[0], cost + new_cost, cur])


def calculate_cost(chromosome):

    cost = 0

    for i in range(1, 20):
        city1, city2 = chromosome[i - 1], chromosome[i]
        path_cost = get_path_cost(city1=city1, city2=city2)
        cost += path_cost

    return cost


def sort_population(population):
    population.sort(key=lambda i: calculate_cost(i))

    return population


def pick_parents(population):
    index1 = randint(0, len(population) - 1)
    index2 = randint(0, len(population) - 1)

    return population[index1], population[index2]



def convert_tour(tour, city_indices):
    """Converts a tour from a list of city strings to a list of integers"""
    return [city_indices[city] for city in tour]


def erx(parent1, parent2):
    global cities

    # Create dictionary that maps each city to a unique integer index
    cities = set(cities)
    city_indices = {city: i for i, city in enumerate(cities)}

    # Convert parent tours to lists of integers
    parent_index1 = convert_tour(parent1, city_indices)
    parent_index2 = convert_tour(parent2, city_indices)


    # Initialize offspring tours
    offspring1 = [-1] * len(parent1)
    offspring2 = [-1] * len(parent2)

    # Initialize list of neighboring cities for each city
    neighbors = [set(graph.neighbours(city)) for city in parent1]

    # Build edge list for each parent
    edges1 = [(parent1[i], parent1[(i+1)%len(parent1)]) for i in range(len(parent1))]
    edges2 = [(parent2[i], parent2[(i+1)%len(parent2)]) for i in range(len(parent2))]

    # Initialize sets of unused cities for each offspring
    unused1 = set(parent_index1)
    unused2 = set(parent_index2)

    # Choose a random starting city for each offspring
    current_city1 = random.choice(parent_index1)
    current_city2 = random.choice(parent_index2)

    # Construct offspring tours by selecting neighboring cities that form a cycle
    while len(unused1) > 0:
        print('current_city1: ', current_city1, 'current_city2: ', current_city2)
        # Select neighboring cities for offspring 1
        offspring1[current_city1] = current_city2
        unused1.discard(current_city1)
        unused2.discard(current_city2)
        neighbors1 = neighbors[current_city1] & unused1
        neighbors2 = neighbors[current_city2] & unused2

        # Choose next city for offspring 1
        if len(neighbors1) > 0:
            # Choose a neighbor that has the fewest neighbors in common with offspring 2
            shared_neighbors = {n: len(neighbors[graph.adjacency_list.index(n)] & neighbors2) for n in neighbors1}
            next_city1 = min(shared_neighbors, key=shared_neighbors.get)
        else:
            # Choose a random unused city
            next_city1 = random.choice(list(unused1))

        # Select neighboring cities for offspring 2
        offspring2[current_city2] = current_city1
        neighbors1 = neighbors[current_city1] & unused1
        neighbors2 = neighbors[current_city2] & unused2

        # Choose next city for offspring 2
        if len(neighbors2) > 0:
            # Choose a neighbor that has the fewest neighbors in common with offspring 1
            shared_neighbors = {n: len(neighbors[graph.adjacency_list.index(n)] & neighbors1) for n in neighbors2}
            next_city2 = min(shared_neighbors, key=shared_neighbors.get)
        else:
            # Choose a random unused city
            next_city2 = random.choice(list(unused2))

        # Update current cities for both offspring
        current_city1 = next_city1
        current_city2 = next_city2



    # Fix remaining unassigned edges
    for i in range(len(parent1)):
        if offspring1[i] == -1:
            next_city = parent1[i]
            while next_city in offspring1:
                next_city = parent2[parent1.index(next_city)]
            offspring1[i] = next_city

        if offspring2[i] == -1:
            next_city = parent2[i]
            while next_city in offspring2:
                next_city = parent1[parent2.index(next_city)]
            offspring2[i] = next_city

    return offspring1, offspring2





def genetic_algorithm(population, percent, generation):
    
    for i in range(generation):
        print(population[0], 666666666666666666666)
    
    
        population = sort_population(population)
        amount = int(len(population) * percent)
        left = len(population) - amount


        population = population[:amount]

        children = []
        for _ in range(left):
            parent1, parent2 = pick_parents(population)

            child1, child2 = erx(parent1=parent1, parent2=parent2)

            probability = uniform(0, 1)
            if probability < 0.1:
                index1 = randint(0, 19)
                index2 = randint(0, 19)
                child1[index1], child1[index2] = child1[index2], child1[index1]
                child2[index1], child2[index2] = child2[index2], child2[index1]

            probability = uniform(0, 1)
            if probability < 0.05:
                index1 = randint(0, 19)
                index2 = randint(0, 19)
                population[0][index1], population[0][index2] = population[0][index2], population[0][index1]


            children.append(child1)
            children.append(child2)

        population += children

    return population[0]


population = generate_population(cities, 5)
path = genetic_algorithm(population=population, percent=0.7, generation=10)
print(path, calculate_cost(path))





