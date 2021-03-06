# objective:
# find the number of connected components


from graph_representation.adjacentListRepresentation import Graph


graph = Graph()
graph.readConstructGraph()

print(graph.nbComponents)