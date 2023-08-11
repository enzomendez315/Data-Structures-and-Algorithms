"""
Preconditions: A directed/undirected graph with no weights.
Result: Shortest path. Minimum spanning tree. Path finding. Cycle detection.
"""

from queue import Queue
    
def bfs(G, start, goal):
    """
    Implements Breadth First Search to see if 
    there is a path between a starting vertex 
    and another vertex.
    """
    queue = Queue()
    visited = set()
    queue.put(start)

    while not queue.empty():
        current = queue.get()
        visited.add(current)

        if current == goal:
            return True

        for adj in G.vertices[current]:
            if adj not in visited:
                queue.put(adj)

    # Did not find the goal
    return False

def bfs_dist(G, start):
    """
    Implements Breadth First Search to find the 
    distance to all reachable vertices given a 
    starting vertex.
    """
    # The distances to all vertices reachable from start
    dist = {key: -1 for key in G.vertices}

    # To process the vertices in order
    queue = Queue()
    queue.put(start)

    # Set distance to itself
    dist[start] = 0

    while not queue.empty():
        current = queue.get()

        # Visit neighbors
        for adj in G.vertices[current]:
            if dist[adj] == -1:
                queue.put(adj)
                dist[adj] = dist[current] + 1

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