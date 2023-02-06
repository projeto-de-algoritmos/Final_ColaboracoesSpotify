# Python program for Kruskal's algorithm to find
# Minimum Spanning Tree of a given connected,
# undirected and weighted graph
 
# Class to represent a graph
 
import collections
import heapq
import itertools as it

 
class Graph:
 
    def __init__(self):
        self.graph = []
        # to store graph
    
    def addSize(self, vertices):
        self.V = vertices  # No. of vertices)

    # function to add an edge to graph
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])
 
    # A utility function to find set of an element i
    # (truly uses path compression technique)
    def find(self, parent, i):
        try:
            if parent[i] != i:
            # Reassignment of node's parent to root node as
            # path compression requires
                parent[i] = self.find(parent, parent[i])
            return parent[i]
        except:
            import ipdb; ipdb.set_trace()
 
    # A function that does union of two sets of x and y
    # (uses union by rank)
    def union(self, parent, rank, x, y):
 
        # Attach smaller rank tree under root of
        # high rank tree (Union by Rank)
        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[x] > rank[y]:
            parent[y] = x
 
        # If ranks are same, then make one as root
        # and increment its rank by one
        else:
            parent[y] = x
            rank[x] += 1
 
    # The main function to construct MST using Kruskal's
        # algorithm
    def KruskalMST(self):
        result = []  # This will store the resultant MST
 
        # An index variable, used for sorted edges
        i = 0
 
        # An index variable, used for result[]
        e = 0

        edgesNum = 0
 
        # Step 1:  Sort all the edges in
        # non-decreasing order of their
        # weight.  If we are not allowed to change the
        # given graph, we can create a copy of graph
        self.graph = sorted(self.graph, key=lambda item: item[2])
 
        parent = []
        rank = []
 
        # Create V subsets with single elements
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
 
        # Number of edges to be taken is less than to V-1
        while e < self.V - 1:
 
            # Step 2: Pick the smallest edge and increment
            # the index for next iteration
            try:
                u, v, w = self.graph[i]
            except:
                import ipdb; ipdb.set_trace()
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
 
            # If including this edge doesn't
            # cause cycle, then include it in result
            # and increment the index of result
            # for next edge
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
            # Else discard the edge
 
        minimumCost = 0
        print("Edges in the constructed MST")
        for u, v, weight in result:
            minimumCost += weight
            edgesNum += 1
            #print(edgesNum)
        print("Minimum Spanning Tree", minimumCost)
        print("Number of edges", edgesNum)
 
 
perm_set = set()

nodes_set = set()

translateNodes = dict()

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

g = Graph()
n_nodes = 0

with open("grafos.txt", encoding="utf8") as f:
    lines = f.readlines()

    for i in range(len(lines)):
        edge, nodes = lines[i].replace("'", '').replace('"', '').split('|')
        nodesList = nodes.replace('\n', '').split(',')
        comb = it.combinations(nodesList, 2)
        

        for nodeCombination in list(comb):
            # Creates a edge only if not exists. To avoid multiple edges between 2 nodes
            if nodeCombination not in perm_set:

                if translateNodes.get(nodeCombination[0], None) == None:
                    translateNodes[nodeCombination[0]] = n_nodes
                    n_nodes += 1

                if translateNodes.get(nodeCombination[1], None) == None:
                    translateNodes[nodeCombination[1]] = n_nodes
                    n_nodes += 1
                
                perm_set.add(nodeCombination)
                
                pop1 = int(artists_dict.get(nodeCombination[0], 1))
                pop2 = int(artists_dict.get(nodeCombination[1], 1))

                # pop1 = 100 - pop1 + 1
                # pop2 = 100 - pop2 + 1

                g.addEdge(translateNodes[nodeCombination[0]], translateNodes[nodeCombination[1]], pop1+pop2)




f.close() 
g.addSize(len(translateNodes)+1)

print(len(translateNodes)+1)
# Function call
g.KruskalMST()