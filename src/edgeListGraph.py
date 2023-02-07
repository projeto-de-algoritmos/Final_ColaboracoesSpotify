import collections
import heapq

class GraphEdgeList:
 
    def __init__(self):
        self.edgesListGraph = []
        # to store graph

    # function to add an edge to graph
    def addEdge(self, u, v, w):
        self.edgesListGraph.append([u, v, w])

    def djsktraShortestPath(self, source, sink):
        graph = collections.defaultdict(list)
        for l, r, c in self.edgesListGraph:
            graph[l].append((c,r))
        # create a priority queue and hash set to store visited nodes
        queue, visited = [(0, source, [])], set()
        heapq.heapify(queue)

        while queue:
            (cost, node, path) = heapq.heappop(queue)
            # visit the node if it was not visited before
            if node not in visited:
                visited.add(node)
                path = path + [node]
                # hit the sink
                if node == sink:
                    return (cost, path)
                # visit neighbours
                for c, neighbour in graph[node]:
                    if neighbour not in visited:
                        heapq.heappush(queue, (cost+c, neighbour, path))
        return float("inf")