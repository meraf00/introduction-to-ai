from random import sample
from Romania import h_longitude_latitude_distance, road_map
from utils import benchmark
from search_algorithms import (
    a_star_search,
    depth_first_search,
    breadth_first_search,
    greedy_search,
    uniform_cost_search,
    iterative_deepening
)


selected_cities = sample(road_map.nodes, 10)


algorithms = {}
algorithms[0] = breadth_first_search
algorithms[1] = depth_first_search
algorithms[2] = uniform_cost_search
algorithms[3] = iterative_deepening
algorithms[4] = greedy_search
algorithms[5] = a_star_search



with open('result.csv', 'w') as res:
    res.write("Algorithm,City One,City Two,Average Time,Path Length\n")
    
    for idx1 in range(len(selected_cities)):
        for idx2 in range(idx1 + 1, len(selected_cities)):

            city_one, city_two = selected_cities[idx1], selected_cities[idx2]

            for i in range(6):
                args = {
                    'graph': road_map,
                    'start_node': city_one,
                    'end_node': city_two
                }

                if i >= 4:
                    args['heuristic_func'] = lambda node: h_longitude_latitude_distance(node, city_two)

                benchmark_result = benchmark(algorithm=algorithms[i],args=args)

                res.write(f'{algorithms[i].__name__},{city_one},{city_two},{benchmark_result[0]},{benchmark_result[1]-1}\n')


    res.close()
                


