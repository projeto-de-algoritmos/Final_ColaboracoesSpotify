import collections
import heapq
import itertools as it

def shortestPath(edges, source, sink):
    # create a weighted DAG - {node:[(cost,neighbour), ...]}
    graph = collections.defaultdict(list)
    for l, r, c in edges:
        graph[l].append((c,r))
    # create a priority queue and hash set to store visited nodes
    queue, visited = [(0, source, [])], set()
    heapq.heapify(queue)
    # traverse graph with BFS
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


perm_set = set()

edges = []

artists_dict = {}

with open("artists.txt", encoding="utf8") as f:
    lines = f.readlines()

    for i in range(len(lines)):
        try:
            artist, popularity = (lines[i].replace('"', '').replace('\n', '').split('|'))
            artists_dict[artist] = popularity
        except:
            import ipdb; ipdb.set_trace()

f.close()

with open("grafos.txt", encoding="utf8") as f:
    lines = f.readlines()

    for i in range(len(lines)):
        edge, nodes = lines[i].replace("'", '').replace('"', '').split('|')
        nodesList = nodes.replace('\n', '').split(',')
        perm = it.permutations(nodesList, 2)
        

        for nodeCombination in list(perm):
            # Creates a edge only if not exists. To avoid multiple edges between 2 nodes
            if nodeCombination not in perm_set:
                perm_set.add(nodeCombination)
                pop1 = int(artists_dict.get(nodeCombination[0], 1))
                pop2 = int(artists_dict.get(nodeCombination[1], 1))

                pop1 = 100 - pop1 + 1
                pop2 = 100 - pop2 + 1

                edges.append((nodeCombination[0], nodeCombination[1], pop1+pop2))

f.close()

print ("A -> E:")
print (shortestPath(edges, "Ivete Sangalo", "Sam Smith"))