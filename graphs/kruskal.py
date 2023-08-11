"""
Kruskal's algorithm reveals a minimum spanning tree of 
a weighted undirected graph.
"""

def kruskal(G):
    """Implements Kruskal's algorithm."""
    result = []

    # i used for sorted edges
    # e used for result[]
    i, e = 0, 0

    # Sort edges in increasing order of weight
    G = sorted(G, key=lambda item: item[2])
    parent = {}
    rank = {}

    for node in range(G.vertices):
        parent.append(node)
        rank.append(0)

    while e < G.vertices - 1:
        u, v, w = G[i]
        i += 1


    """ The Algorithm Design Manual Pseudocode
    kruskal(G)
        put the edges in a priority queue ordered by weight
        count = 0
        while count < n-1
            get next edge (u,v)
            if component(u) != component(v)
                add to tree
                merge component(u) and component(v)
    """

    """ Algorithms Pseudocode
    kruskal(G,weights)
        for all vertices u in the graph
            makeset(u)
        
        X = {}
        sort the edges E by weight
        for all edges (u,v) in increasing order of weight
            if find(u) != find(v)
                add edge (u,v) to X
                union(u,v)
    """