"""
Kruskal's algorithm reveals a minimum spanning tree of 
a weighted undirected graph.
"""

def kruskal(G):
    """
    Implements Kruskal's algorithm.
    
    G is a graph represented by a list of lists. 
    Each entry describes an edge [src, dst, weight].
    """
    result = []

    # i used for sorted edges
    # edges used for result[]
    i, edges = 0, 0

    # Sort edges in increasing order of weight
    G = sorted(G, key=lambda item: item[2])
    parent = {}
    rank = {}

    for node in range(G.vertices):
        parent.append(node[0])
        rank.append(0)

    while edges < G.vertices - 1:
        src, dst, weight = G[i]
        i += 1
        x = find(parent, src)
        y = find(parent, dst)

        if x != y:
            edges += 1
            result.append([src, dst, weight])
            union(parent, rank, x, y)
        # else discard the edge

def find(parent, i):
    if parent[i] != i:
        parent[i] = find(parent, parent[i])
    return parent[i]

def union(parent, rank, x, y):
    if rank[x] < rank[y]:
        parent[x] = y
    elif rank[x] > rank[y]:
        parent[y] = x
    else:
        parent[y] = x
        rank[x] += 1


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