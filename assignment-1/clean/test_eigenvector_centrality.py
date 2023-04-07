from graph import eigenvector_centrality, katz_centrality, UndirectedGraph, DirectedGraph

graph = UndirectedGraph()
graph.add_edge(1, 2)
graph.add_edge(2, 3)
graph.add_edge(2, 4)
graph.add_edge(3, 6)
graph.add_edge(4, 6)
graph.add_edge(4, 5)
graph.add_edge(5, 6)
print(eigenvector_centrality(graph))


graph = DirectedGraph()
graph.add_edge(1, 2)
graph.add_edge(2, 3)
graph.add_edge(2, 4)
graph.add_edge(4, 6)
graph.add_edge(4, 5)
graph.add_edge(5, 6)
graph.add_edge(6, 3)

print(eigenvector_centrality(graph))
print(katz_centrality(graph))
for v in katz_centrality(graph, alpha=0.5).values():
    print(v/0.59969438129825)
