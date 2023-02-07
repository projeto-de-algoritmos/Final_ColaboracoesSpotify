from menu import menu
import graph
import edgeListGraph
import networkx as nx

import itertools as it

def get_artists(g):
    with open("artists.txt", encoding="utf8") as f:
        lines = f.readlines()

        for i in range(len(lines)):
            artist, popularity = (lines[i].replace('"', '').replace('\n', '').split('|'))
            g.artists_dict[artist] = popularity

    f.close()


def build_graph(g, networkXG, edgeListG):
    n_nodes = 0
    with open("grafos.txt", encoding="utf8") as f:
        lines = f.readlines()

        for i in range(len(lines)):
            edge, nodes = lines[i].replace("'", '').replace('"', '').split('|')
            nodesList = nodes.replace('\n', '').split(',')
            perm = it.permutations(nodesList, 2)
            

            for nodeCombination in list(perm):
                # Creates a edge only if not exists. To avoid multiple edges between 2 nodes
                if nodeCombination not in g.perm_set:
                    if g.translateNodes.get(nodeCombination[0], None) == None:
                        g.translateNodes[nodeCombination[0]] = n_nodes
                        n_nodes += 1

                    if g.translateNodes.get(nodeCombination[1], None) == None:
                        g.translateNodes[nodeCombination[1]] = n_nodes
                        n_nodes += 1
                    
                    g.perm_set.add(nodeCombination)
                    
                    pop1 = int(g.artists_dict.get(nodeCombination[0], 1))
                    pop2 = int(g.artists_dict.get(nodeCombination[1], 1))

                    pop1 = 100 - pop1 + 1
                    pop2 = 100 - pop2 + 1

                    g.addEdge(nodeCombination[0], nodeCombination[1], edge)
                    networkXG.add_edge(nodeCombination[0], nodeCombination[1], weight=pop1+pop2)
                    edgeListG.addEdge(nodeCombination[0], nodeCombination[1], pop1+pop2)

    f.close()

g = graph.Graph()
networkXG = nx.DiGraph()
edgeListG = edgeListGraph.GraphEdgeList()

get_artists(g)
build_graph(g, networkXG, edgeListG)

menu(g, networkXG, edgeListG)