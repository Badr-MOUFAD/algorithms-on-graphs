
# The indexing of vertices start from 1
# This convention abide by the representation
# given by the course algorithms on graphs

# the adopted graph representation is: Adjacent List


class Graph:
    def __init__(self):
        self.nbVertices = 0
        self.nbEdges = 0

        self.vertices = dict()
        self.nbComponents = 0
        self.clock = 0
        return

    def __getitem__(self, item):
        if 1 <= int(item) <= self.nbVertices:
            return self.vertices[item]

        raise Exception("This node does not exist")

    def __setitem__(self, key, value):
        self.vertices[key] = value

    def readConstructGraph(self):
        self.nbVertices, self.nbEdges = [int(s) for s in input().split(" ")]

        # construct vertices
        # index start from 1
        for index in range(1, self.nbVertices + 1):
            self[index] = Vertex(index=index, neighbours={})

        for i in range(self.nbEdges):
            indexVertexStart, indexVertexEnd = [int(s) for s in input().split(" ")]

            self[indexVertexStart].neighbours[indexVertexEnd] = self[indexVertexEnd]
            self[indexVertexEnd].neighbours[indexVertexStart] = self[indexVertexStart]

        #
        self.applyDFS()
        return

    # applying Deep first search
    def applyDFS(self):
        self.nbComponents = 0
        self.clock = 0

        for v in self.vertices.values():
            if not v.wasVisited:
                self.explore(vertex=v, componentIndex=self.nbComponents)
                self.nbComponents += 1
        return

    # find all connected vertices to a given vertex
    def explore(self, vertex, componentIndex=None):
        if vertex.wasVisited:
            return

        vertex.wasVisited = True
        vertex.componentIndex = componentIndex

        # save the order in which the vertex was explored
        vertex.preVisited = self.clock
        self.clock += 1

        for v in vertex.neighbours.values():
            self.explore(vertex=v, componentIndex=componentIndex)

        # save the order in which it was quited
        vertex.postVisited = self.clock
        self.clock += 1
        return


class Vertex:
    # neighbours must be in a form of a dict
    # { index_of_vertex: vertex, ... }
    def __init__(self, index, neighbours={}):
        self.index = index

        self.wasVisited = False

        self.componentIndex = None

        self.postVisited = None
        self.preVisited = None

        self.neighbours = neighbours
        return


# example
# input
# 4 4
# 1 2
# 3 2
# 4 3
# 1 4

# g1 = Graph()
# g1.readGraph()

# for i, v in g1.vertices.items():
#     print("index vertex :{0} {1}".format(i, v.index))
#     print("\t neighbours")
#     for j, w in v.neighbours.items():
#         print("\t index vertex :{0} {1}".format(j, w.index))

# g1.applyDFS()
# print(g1.nbComponents)