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

    def bfs(self, start_vertex) -> None:
        """Implements Breadth First Search."""

        visited = set()
        queue = Queue()

        while not queue.empty():
            vertex = queue.get()

            for adj in self.vertices[vertex]:
                if adj not in visited:
                    queue.put(adj)
                    visited.add(adj)

    """ The Algorithm Design Manual Pseudocode
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

    """ Algorithms Pseudocode
    bfs(G,s)
        for all vertices u in the graph
            dist[u] = infinity
        
        dist[s] = 0
        Q = [s] (queue containing just s)
        while Q is not empty
            u = eject(Q)
            for each v in adjacent vertices of u
                if dist(v) = infinity
                    inject(Q,v)
                    dist[v] = dist[u] + 1
    """