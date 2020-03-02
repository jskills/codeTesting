
class GraphNode:
    def __init__(self, data):
        self.data = data
        self.vertexList = list()

    def addVertex(self, vertexVal):
        if vertexVal not in self.vertexList:
            newNode = GraphNode(vertexVal)
            self.vertexList.append(newNode)
        return newNode

    def connectVertex(self, node, vertexNode):
        node.vertexList.append(vertexNode)
        

    def printGraph(self, node, visited=list()):
        # starting with one node, print all connections in a directed graph
        if node.data:
            if len(node.vertexList):
                for v in node.vertexList:
                    print(node.data + "->" + v.data)
                    if v.data not in visited:
                        visited.append(v.data)
                        self.printGraph(v, visited)
                else:   
                    return
        else:
            return

    

###############################################

a = GraphNode('A')
b = a.addVertex('B')
c = a.addVertex('C')
b.connectVertex(b,c)
d = b.addVertex('D')
e = GraphNode('E')
f = c.addVertex('F')
g = f.addVertex('G')
c.connectVertex(c,d)
d.connectVertex(d,c)
g.connectVertex(g,d)
e.connectVertex(e,f)


b.printGraph(a)

