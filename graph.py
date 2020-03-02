from collections import deque


class Graph():
    def __init__(self):
        self.graphDict = dict()

    def find_all_paths(self, graph, start, end, path=[]):
	# create a new list.
        # path = path + [start] is necessary since
        # Using path.append(start) would modify the value of path in the caller
        path = path + [start]
        if start == end:
            # of start is the same as end return [path] and end recursion
            return [path]
        if not start in graph:
            # if start param does not even exist in the graph return empty list
            return []
        all_paths = []
        # since our graphDict is in the form of : nodename, list of all nodes it is connected to
        # iterate over each unique nodename and pass each of the nodes it's connected to back into this method
        for node in graph[start]:
            # the path array gets passed back into this method recursively
            # if the value of the connected node is not in our path array
            # recursively call this method passing in the connected node as the start node with the same end
            if node not in path:
                newpaths = self.find_all_paths(graph, node, end, path)
                # since we will get multiple paths from this call,
                # iterate and append them to the all_paths array which is returned at the end of this method
                for newpath in newpaths:
                    all_paths.append(newpath)
        return all_paths


    def find_shortest_rpath(self, graph, start, end, path=[]):
        # finding the shortest path is almost exactly the same as finding all paths
        # except instead of augmenting a long list of paths, we just store the one with the shortest length
        path = path + [start]
        if start == end:
            return path
        if not start in graph:
            return None
        shortest = None
        for node in graph[start]:
            if node not in path:
                newpath = self.find_shortest_rpath(graph, node, end, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
        return shortest


    def generateEdges(self, graph):
        edges = {}
        for node in graph:
            for neighbor in graph[node]:
                if node in edges:
                        edges[node].append(neighbor)
                else:
                        edges[node] = [neighbor]
        return edges	


    # using deque - faster, but probably not helpful for academic purposes
    def find_shortest_path(self, graph, start, end):
        dist = {start: [start]}
        q = deque(start)
        while len(q):
            at = q.popleft()
            for next in graph[at]:
                if next not in dist:
                    dist[next] = [dist[at], next]
                    q.append(next)
        return dist.get(end)


    def BFSearch(self, node):
        # breadth first search from any node in the graph
        # use different Dict structure (one entry per edge)
        newDict = {}
        newDict = self.generateEdges(self.graphDict)
        visited = {} 
        for i in newDict:
                visited[i] = False
        queue = []
        queue.append(node)
        visited[node] = True
        while len(queue):
                node = queue.pop(0)
                for n in newDict[node]:
                        if visited[n] == False:
                                visited[n] = True
                                queue.append(n)
                print(node,end=" ")
        print("\n")
	
        


######################################

g = Graph()
# note this is a directed graph
g.graphDict = {'A': ['B', 'C'],
          'B': ['D'],
          'C': ['D', 'F'],
          'D': ['C'],
          'E': ['F'],
          'F': ['G'],
          'G': ['D']}


print("All Edges")
print(g.generateEdges(g.graphDict))

print("Finding All Paths")
print(g.find_all_paths(g.graphDict, 'A', 'G'))

print("Shortest Path using recursion")
print(g.find_shortest_rpath(g.graphDict, 'A', 'G'))

print('BFSearch')
g.BFSearch('G')
