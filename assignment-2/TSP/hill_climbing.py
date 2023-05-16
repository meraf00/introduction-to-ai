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


def generateSuccessors(tour):
	N = len(tour)        
	
	# generate 2 random sequences
	randomSequence1 = list(range(N))
	random.shuffle(randomSequence1)
	randomSequence2 = list(range(N))
	random.shuffle(randomSequence2)
	
	# this generates all successors of the initial tour and yields them    
	for i in randomSequence1:
		for j in randomSequence2:
			
			#to avoid swapping same pair twice
			if i<j:
				temp = list(tour)
				temp[i],temp[j] = tour[j],tour[i]
				yield temp

def hill_climbing(cities, generation):
    path = cities
    random.shuffle(path)

    bestTour = path
    bestValue = utils.calculate_cost(path, graph)

    for _ in range(generation):

        moved = False
	
        for successor in generateSuccessors(bestTour):
            successorValue = utils.calculate_cost(successor, graph=graph)
            print(successor, successorValue)
			
			# moving uphill if successir is better than current value
            if successorValue < bestValue:
                bestTour  = successor
                bestValue = successorValue
                moved = True
                break
                        
        if moved == False:
            break
    
    return (bestTour, bestValue)
    # return best_path, best_cost

best_path, best_cost = hill_climbing(cities=utils.cities, generation=100)
print(best_path, best_cost)
    