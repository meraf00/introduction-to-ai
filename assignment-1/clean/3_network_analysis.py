import os
import utils
from graph import *
from collections import defaultdict


def compute_centralities(graph):
    centrality_algorithms = (
        degree_centrality,
        closeness_centrality,
        betweeness_centrality,
        eigenvector_centrality,
        katz_centrality
    )

    centralitites = {}

    for alg in centrality_algorithms:
        centralitites[alg] = alg(graph)

    return centralitites


romania_file = os.path.join(os.path.dirname(
    __file__), "romania-data/romania-road-distance.txt")

romania_map = utils.load_city_graph(romania_file)

centralities = compute_centralities(romania_map)
 
with open("output.csv", "w") as f:
    f.write("Algorithm,")
    f.write(",".join([city for city in romania_map.nodes]))
    f.write("\n")

    for alg in centralities:
        f.write(alg.__name__)
        f.write(",")

        f.write(",".join(["%.4f" % centralities[alg][city]
                for city in romania_map.nodes]))
        f.write("\n")
