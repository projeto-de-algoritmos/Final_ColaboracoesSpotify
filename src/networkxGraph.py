import networkx as nx

def shortest_path(G, artist1, artist2):
    path = nx.bellman_ford_path(G, artist1, artist2)
    return path


def shortest_dist(G, artist1, artist2):
    dist = nx.bellman_ford_path_length(G, artist1, artist2)
    return dist


def acessible_nodes(G, artist):
    listLen = nx.single_source_bellman_ford_path_length(G, artist)
    return len(listLen)
