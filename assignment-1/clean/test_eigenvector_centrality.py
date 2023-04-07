from graph import eigenvector_centrality, UndirectedGraph

graph = UndirectedGraph()
graph.add_edge(1, 2)
graph.add_edge(2, 3)
graph.add_edge(2, 4)
graph.add_edge(3, 6)
graph.add_edge(4, 6)
graph.add_edge(4, 5)
graph.add_edge(5, 6)
print(eigenvector_centrality(graph))
