"""
The Bellman-Ford algorithm reveals the shortest path in a weighted 
graph with negative edges (but no negative cycles).
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

    """ Algorithms Pseudocode
    bellmanford(G,len,s)
        for all vertices u in the graph
            dist[u] = infinity
            prev[u] = nil

        dist[s] = 0
        repeat V-1 times:
            for all edges e
                update(e)
    """