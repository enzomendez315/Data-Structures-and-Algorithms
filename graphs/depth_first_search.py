"""
Preconditions: A directed/undirected graph with no weights.
Result: Path finding. Cycle detection.
"""

def dfs(G, current, goal):
    """Implements Depth First Search using recursion."""
    if current == goal:
        return [current]
    
    for next in G.vertices[current]:
        result = dfs(G, next)
        if result != None:
            return [current] + result
    
    return None
    
def dfs_stack(G, start, goal):
    """Implements Depth First Search using a stack."""
    stack = [start]
    visited = set()

    while stack:
        current = stack.pop()
        visited.add(current)

        if current == goal:
            return True

        for adj in G.vertices[current]:
            if not adj in visited:
                stack.append(adj)

    # Did not find the goal
    return False
    
""" General Implementation
Input: A graph with a list of edges and a starting vertex.
        If no starting vertex is provided, we will go through 
        each vertex in the graph.
Output: 

Overhead (what you need):
- Set to store "visited" vertices
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