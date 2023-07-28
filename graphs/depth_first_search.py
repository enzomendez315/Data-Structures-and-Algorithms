class Graph:
    def __init__(self) -> None:
        self.vertex = {}

    def print_graph(self) -> None:
        print(self.vertex)
        for i in self.vertex:
            print(i, " -> ", " -> ".join([str(j) for j in self.vertex]))

    def add_edge(self, start_vertex, end_vertex) -> None:
        """Adds an edge between two vertices."""

        if start_vertex in self.vertex:
            # Vertex is already present
            self.vertex[start_vertex].append(end_vertex)
        else:
            # Create a list with the vertex
            self.vertex[start_vertex] = [end_vertex]

    def dfs(self) -> None:
        # Create a new list with all elements as False
        visited = [False] * len(self.vertex)

        # Call the helper function
        for i in range(len(self.vertex)):
            if not visited[i]:
                self.dfs_recursive(i, visited)

    def dfs_recursive(self, start_vertex, visited) -> None:
        # Mark vertex as visited
        visited[start_vertex] = True

        print(start_vertex, end=" ")

        # Recur for all adjacent vertices 
        for i in self.vertex:
            if not visited[i]:
                self.dfs_recursive(i, visited)