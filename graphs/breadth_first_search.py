from queue import Queue

class Graph:
    def __init__(self) -> None:
        self.vertices = {}

    def print_graph(self) -> None:
        """Prints a visual representation of the graph."""

        print(self.vertices)
        for i in self.vertices:
            print(i, " : ", " -> ".join([str(j) for j in self.vertices[i]]))

    def add_edge(self, start_vertex, end_vertex) -> None:
        """Adds an edge between two vertices."""

        if start_vertex in self.vertices:
            # Vertex is already present
            self.vertices[start_vertex].append(end_vertex)
        else:
            # Create a list with the vertex
            self.vertices[start_vertex] = [end_vertex]

    """ The Algorithm Design Manual
    BFS(G,s)
        for each vertex u in the set of all vertices - {s}
            state[u] = "undiscovered"
            parent[u] = nil (no parent is in the BFS tree)
        state[s] = "discovered"
        parent[s] = nil
        Q = {s}
        while Q != 0
            u = dequeue[Q]
            process vertex u    ?
            for each v in adjacent vertices of u
                process edge (u,v)  ?
                if state[v] = "undiscovered"
                    state[v] = "discovered"
                    parent[v] = u
                    enqueue[Q,v]
            state[u] = "processed"
    """

    """
    BFS(u)
        Mark u as visited.
        Enqueue u.
    """