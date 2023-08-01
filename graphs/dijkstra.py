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
    dijkstra(G,s,t)
        known = {s}
        for all vertices u in the graph
            dist[u] = infinity
        for all edges (s,v)
            dist[v] = weight(s,v)
        last = s
        while last != t
            select the next vertex u (the unknown vertex minimizing dist[v])
            for all edges (u,x)
                dist[x] = min(dist[x], dist[u] + weight(u,x))
            last = u
            add u to the set of known
    """
    
    """ Algorithms Pseudocode
    dijkstra(G,len,s)
        for all vertices u in the graph
            dist[u] = infinity
            prev[u] = nil
        dist[s] = 0

        H = makequeue(V)    (using dist-values as keys)
        while H is not empty
            u = deletemin(H)
            for each v in adjacent vertices of u
                if dist[v] > dist[u] + len[u,v]
                    dist[v] = dist[u] + len[u,v]
                    prev[v] = u
                    decreasekey(H,v)
    """