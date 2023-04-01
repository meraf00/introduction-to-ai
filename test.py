from Graph import *

g = DirectedGraph()
g = UndirectedGraph()

g.add_node("a")
print(g)

g.add_node("a")
print(g)

g.add_node("c")
print(g)


g.add_edge("a", "c")
print(g)

g.add_edge("a", "c", 3)
print(g)

g.add_edge("b", "d")
print(g)

g.add_edge("b", "c", 1)
print(g)

g.add_edge("b", "d", 1)
print(g)

g.delete_edge("b", "d")
print(g)
print(g.neighbours("c"))

g.add_edge("b", "d", 1)
print(g)

g.delete_node("c")
print(g)


