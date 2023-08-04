"""
Depth First Search reveals what parts of the graph are reachable from a given 
vertex. 
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

    def dfs(self) -> None:
        """Implements Depth First Search using recursion."""
        # Create a new dictionary with the vertices as keys 
        # and False as their values
        visited = {key: False for key in self.vertices}

        # Call the helper method
        for vertex in visited.keys():
            if not visited[vertex]:
                self.dfs_recursive(vertex, visited)

    def dfs_recursive(self, start_vertex, visited) -> None:
        """Helper method for Depth First Search."""
        # Mark vertex as visited
        visited[start_vertex] = True

        print(start_vertex, end=" ")

        # Recur for all adjacent vertices 
        for adj in self.vertices[start_vertex]:
            if not visited[adj]:
                self.dfs_recursive(adj, visited)

    def dfs_stack(self, start_vertex) -> set[str]:
        """Implements Depth First Search using a stack."""
        visited = set(start_vertex)
        stack = [start_vertex]

        while stack:
            vertex = stack.pop()
            visited.add(vertex)
        
            for adj in self.vertices[vertex]:
                if adj not in visited:
                    stack.append(adj)
        
        return visited
    
    """ General Implementation
    Input: A graph with a list of edges and a starting vertex.
            If no starting vertex is provided, we will go through 
            each vertex in the graph.
    Output: 

    Overhead (what you need):
    - Dictionary to store "visited" vertices
    - Variable that keeps track of time
    - Dictionary to store "parents" of vertices

    1. Initialize "visited". Mark all vertices as False
    2. Record previsit time and increase it by one (optional)
    3. For each neighbor of the current vertex u, check if it 
        has been visited. If it hasn't, mark its parent and 
        call the method again using the neighbor as input.
    4. Mark visited[u] as True
    5. Record postvisit time and increase it by one (optional)
    """

    """ The Algorithm Design Manual Pseudocode
    DFS(G,u)
        state[u] = "discovered"
        process vertex u    ?
        entry[u] = time
        time = time + 1
        for each v in adjacent vertices of u
            process edge (u,v)  ?
            if state[v] = "undiscovered", then
                parent[v] = u
                DFS(G,v)
        state[u] = "processed"
        exit[u] = time
        time = time + 1
    """

    """ Algorithms Pseudocode
    dfs(G)
        for all vertices u in the graph
            visited[u] = false
        for all vertices u in the graph
            if u is not visited
                explore(u)  // A new, disjoint, connected component is chosen

    explore(G,u)
        visited[u] = true
        previsit(u)
        for each v in adjacent vertices of u
            if v is not visited
                explore(v)
        postvisit(u)
    """