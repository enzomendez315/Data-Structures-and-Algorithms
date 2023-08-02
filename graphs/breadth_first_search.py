"""
Breadth First Search reveals the distance between a starting vertex 
and all the vertices that are reachable from that vertex.
"""

from queue import Queue

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

    def bfs(self, start_vertex) -> list:
        """Implements Breadth First Search."""

        # A set for the visited vertices
        visited = {start_vertex}

        # A list with the order given by bfs
        result = [start_vertex]

        # To process the vertices in order
        queue = Queue()
        queue.put(start_vertex)

        while not queue.empty():
            vertex = queue.get()
            # Visit neighbors
            for adj in self.vertices[vertex]:
                if adj not in visited:
                    visited.add(adj)
                    result.append(adj)
                    queue.put(adj)
        
        return result
    
    def bfs_distance(self, start_vertex) -> dict:
        """
        Implements Breadth First Search to find the 
        distance to all reachable vertices given a 
        starting vertex.
        """

        # The distances to all vertices reachable from start_vertex
        dist = {key: -1 for key in self.vertices}

        # To process the vertices in order
        queue = Queue()

        # Set distance to itself
        dist[start_vertex] = 0

        queue.put(start_vertex)
        while not queue.empty():
            vertex = queue.get()
            # Visit neighbors
            for adj in self.vertices[vertex]:
                if dist[adj] == -1:
                    queue.put(adj)
                    dist[adj] = dist[vertex] + 1

        return dist
    
    """ General Implementation
    Input: A graph with a list of edges and a starting vertex
            If no starting vertex is provided, we will go through 
            each vertex in the graph.
    Output: 

    Overhead (what you need):
    - Set, to store "visited" vertices or dictionary to record 
        distances to other vertices
    - Queue to process vertices in order
    - Dictionary to store "parents" of vertices

    1. Initialize "visited" or "distances", depending on implementation
    2. Enqueue starting vertex
    3. While the queue is not empty, dequeue the next vertex and look at 
        its neighbors. If it hasn't been visited or if the distance to 
        the neighbor is set to infinity, enqueue it and marke it as visited 
        (or record the right distance).
    4. Return the dictionary with the distances or the list with the right order
    """

    """ The Algorithm Design Manual Pseudocode
    BFS(G,s)
        for each vertex u in the set of all vertices
            state[u] = "undiscovered"
            parent[u] = nil (no parent is in the BFS tree)
        state[s] = "discovered"
        parent[s] = nil
        Q = {s}
        while Q != 0
            u = dequeue[Q]
            for each v in adjacent vertices of u    # Process vertex u
                if state[v] = "undiscovered"        # Process edge (u,v)
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