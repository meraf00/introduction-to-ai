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
    visited = set()
    for i in range(1, 20):
        city1, city2 = chromosome[i - 1], chromosome[i]
        path_cost = get_path_cost(city1=city1, city2=city2)
        cost += path_cost

        if city1 in visited:
            cost += 10000
        visited.add(city1)

    return cost



def sort_population(population):
    population.sort(key=lambda i: calculate_cost(i))

    return population


def pick_parents(population):
    index1 = randint(0, len(population) - 1)
    index2 = randint(0, len(population) - 1)

    return population[index1], population[index2]



def cross_over(parent1, parent2):
    index = random.randint(1, 19)

    child = parent1[:index] + parent2[index:]
    return child


def mutate(chromosome):
    index1 = random.randrange(20)
    index2 = random.randrange(20)

    chromosome[index1], chromosome[index2] = chromosome[index2], chromosome[index1]

    return chromosome




def genetic_algorithm(population, percent, generation):
    
    for _ in range(generation):
    
    
        population = sort_population(population)
        print(population[0], calculate_cost(population[0]))
        amount = int(len(population) * percent)
        left = len(population) - amount


        population = population[:amount]

        children = []
        for _ in range(left):
            parent1, parent2 = pick_parents(population)

            child = cross_over(parent1=parent1, parent2=parent2)

            probability = uniform(0, 1)
            if probability < 0.1:
                mutate(child)


            probability = uniform(0, 1)
            if probability < 0.05:
                mutate(population[0])
                

            children.append(child)

        population += children

    sort_population(population)

    return population[0]


population = generate_population(cities, 1000)
path = genetic_algorithm(population=population, percent=0.7, generation=300)
print(path, calculate_cost(path))





