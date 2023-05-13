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
    queue = deque([city1, 0, None])

    while queue:
        cur, cost, parent = queue.popleft()

        if cur == city2:
            return cost

        for neighbour in graph[cur] and neighbour[0] != parent:
            new_cost = neighbour[1]
            queue.append([neighbour, cost + new_cost, cur])


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


def genetic_algorithm(population, percent):
    population = sort_population(population)
    amount = int(len(population) * percent)
    left = len(population) - amount

    if calculate_cost(population[0]) == 0:
        return population[0]

    population = population[:amount]

    children = []
    for _ in range(left):

        parent1, parent2 = pick_parents(population)

        index = randint(0, 19)
        child = parent1[:index] + parent2[index:]

        probability = uniform(0, 1)
        if probability < 0.1:
            index1 = randint(0, 19)
            index2 = randint(0, 19)
            child[index1], child[index2] = child[index2], child[index]

        probability = uniform(0, 1)
        if probability < 0.05:
            index1 = randint(0, 19)
            index2 = randint(0, 19)
            population[0][index1], population[0][index2] = population[0][index2], child[index]


        children.append(child)

    population += children


population = generate_population(cities, 100)
