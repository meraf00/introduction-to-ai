import utils
import random


def generateSuccessors(tour):
	N = len(tour)        
	
	randomSequence1 = list(range(N))
	random.shuffle(randomSequence1)
	randomSequence2 = list(range(N))
	random.shuffle(randomSequence2)
	

	for i in randomSequence1:
		for j in randomSequence2:
			
			#to avoid swapping same pair twice
			if i<j:
				temp = list(tour)
				temp[i],temp[j] = tour[j],tour[i]
				yield temp


def hill_climbing(cities, graph, generation):
    path = cities
    random.shuffle(path)

    bestTour = path
    bestValue = utils.calculate_cost(path, graph)

    for _ in range(generation):

        moved = False
	
        for successor in generateSuccessors(bestTour):
            successorValue = utils.calculate_cost(successor, graph=graph)
			
			# moving uphill if successir is better than current value
            if successorValue < bestValue:
                bestTour  = successor
                bestValue = successorValue
                moved = True
                        
        if moved == False:
            break
    
    return (bestTour, bestValue)

    