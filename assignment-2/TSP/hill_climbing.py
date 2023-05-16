import utils
import random


graph = utils.load_city_graph()


def swap(path, i, j):
    new_path = path[:i] + path[i:j+1][::-1] + path[j+1:]
    return new_path


def get_neighbours(state):
    neighbours = []

    for i in range(len(state)):
        for j in range(i+1, len(state)):
            new_state = swap(state, i, j)

            neighbours.append(new_state)

    return neighbours


def hill_climbing(cities, generation):
    path = cities
    random.shuffle(path)

    best_path = path
    best_cost = utils.calculate_cost(path, graph)

    for _ in range(generation):

        neighbours = get_neighbours(path)
        neighbours_cost = [utils.calculate_cost(neighbour, graph) for neighbour in neighbours]
        no_better = True
        for i in range(len(neighbours)):
            if neighbours_cost[i] < best_cost:
                best_path = neighbours[i]
                best_cost = neighbours_cost[i]

                no_better = False

        if no_better:
            break
    
    return best_path, best_cost

best_path, best_cost = hill_climbing(cities=utils.cities, generation=100)
print(best_path, best_cost)
    