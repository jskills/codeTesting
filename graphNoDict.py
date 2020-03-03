
class GraphNode:
	def __init__(self, data):
		self.data = data
		self.vertexList = list()


	def addVertex(self, vertexVal):
		if vertexVal not in self.vertexList:
			newNode = GraphNode(vertexVal)
			self.vertexList.append(newNode)
			return newNode
		else:
			return None


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


	def findAllPaths(self, start, end, paths=[]):
		paths = paths + [start.data]
		if start.data == end.data:
			return [paths]
		all_paths = []
		if len(start.vertexList):
			for v in start.vertexList:
				if v.data not in paths:
					newpaths = self.findAllPaths(v, end, paths)
					for n in newpaths:
						all_paths.append(n)

		return all_paths

	
	def findShortestPath(self, start, end):
		paths = self.findAllPaths(start, end)
		checkLen = 0
		shortest = None
		for p in paths:
			if len(p) < checkLen or checkLen < 1:
				checkLen = len(p)
				shortest = p
		return shortest
			


                
            
        

    

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

print("All Paths")
print(str(a.findAllPaths(a, g)))
print("Shortest Path")
print(str(a.findShortestPath(a, g)))
