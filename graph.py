from collections import deque


class Graph():
    def __init__(self):
        self.graphDict = dict()

    def find_all_paths(self, graph, start, end, path=[]):
	# create a new list. Using path.append(start) would modify the value of path in the caller
        path = path + [start]
        if start == end:
            return [path]
        if not start in graph:
            return []
        all_paths = []
        for node in graph[start]:
            if node not in path:
                newpaths = self.find_all_paths(graph, node, end, path)
                for newpath in newpaths:
                    all_paths.append(newpath)
        return all_paths


    def find_shortest_rpath(self, graph, start, end, path=[]):
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
        edges = []
        for node in graph:
            for neighbor in graph[node]:
                edges.append((node, neighbor))
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



