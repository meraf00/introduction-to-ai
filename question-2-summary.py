average = {
        'breadth_first_search': [11597.167251477003, 0.0016057599972555178], 
        'depth_first_search': [11597.167251477003, 0.0008389200000237909], 
        'uniform_cost_search': [11597.167251477003, 0.0020438499996089377], 
        'iterative_deepening': [11597.167251477003, 0.003643350003767409], 
        'greedy_search': [11597.167251477003, 0.002197459998569684], 
        'a_star_search': [11597.167251477003, 0.005595749999702093]
    }

for i in average:
    print(i)
    speed = average[i][0] / average[i][1]
    average[i].append(speed)

