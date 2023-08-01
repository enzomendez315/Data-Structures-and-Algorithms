"""
Kruskal's algorithm reveals a minimum spanning tree of 
a weighted undirected graph.
"""

class Graph:
    def __init__(self) -> None:
        self.vertices = {}

    def print_graph(self) -> None:
        """Prints a visual representation of the graph."""

        print(self.vertices)
        for vertex in self.vertices:
            print(vertex, " : ", " -> ".join([str(adj) for adj in self.vertices[vertex]]))

    def add_edge(self, start_vertex, end_vertex) -> None:
        """Adds an edge between two vertices."""

        if start_vertex in self.vertices:
            # Vertex is already present
            self.vertices[start_vertex].append(end_vertex)
        else:
            # Create a list with the vertex
            self.vertices[start_vertex] = [end_vertex]

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