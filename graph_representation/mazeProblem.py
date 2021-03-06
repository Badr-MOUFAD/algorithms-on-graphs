# objective :
# find whether two vertices are connected


from graph_representation.adjacentListRepresentation import Graph


maze = Graph()
maze.readConstructGraph()

# input the given vertices
v1, v2 = [int(s) for s in input().split(" ")]

# output
if maze[v1].componentIndex == maze[v2].componentIndex:
    print(1)
else:
    print(0)
