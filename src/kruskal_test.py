import itertools as it
import networkx as nx
 
 
# Driver's code
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

n_nodes = 0

G = nx.Graph()

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
                    G.add_node(nodeCombination[0])

                if translateNodes.get(nodeCombination[1], None) == None:
                    translateNodes[nodeCombination[1]] = n_nodes
                    n_nodes += 1
                    G.add_node(nodeCombination[1])
                
                perm_set.add(nodeCombination)
                
                pop1 = int(artists_dict.get(nodeCombination[0], 1))
                pop2 = int(artists_dict.get(nodeCombination[1], 1))

                pop1 = 100 - pop1 + 1
                pop2 = 100 - pop2 + 1
                
                G.add_edge(nodeCombination[0], nodeCombination[1], weight=pop1+pop2)


dist = nx.bellman_ford_path_length(G, "Sam Smith", "Ivete Sangalo")
listLen = nx.single_source_bellman_ford_path_length(G, "Sam Smith")

print(len(listLen))