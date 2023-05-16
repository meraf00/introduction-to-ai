import random
import utils
from collections import deque



graph = utils.load_city_graph()


def generate_population(cities, size):
    population = []

    for _ in range(size):
        chromosome = cities
        random.shuffle(chromosome)
        population.append(chromosome)

    return population



def sort_population(population):
    population.sort(key=lambda i: utils.calculate_cost(i, graph=graph))

    return population


def pick_parents(population):
    index1 = random.randint(0, len(population) - 1)
    index2 = random.randint(0, len(population) - 1)

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
        print(population[0], utils.calculate_cost(population[0], graph=graph))
        amount = int(len(population) * percent)
        left = len(population) - amount


        population = population[:amount]

        children = []
        for _ in range(left):
            parent1, parent2 = pick_parents(population)

            child = cross_over(parent1=parent1, parent2=parent2)

            probability = random.uniform(0, 1)
            if probability < 0.1:
                mutate(child)


            probability = random.uniform(0, 1)
            if probability < 0.05:
                mutate(population[0])
                

            children.append(child)

        population += children

    sort_population(population)

    return population[0]


population = generate_population(utils.cities, 2000)
path = genetic_algorithm(population=population, percent=0.7, generation=300)
print(path, utils.calculate_cost(path, graph=graph))






