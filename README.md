# Data Structures and Algorithms
This guide shows the implementation and usage of popular algorithms and data structures using Python.

# Data Structures
## Arrays
An array is a contiguously-allocated data structure. Arrays are structures of fixed-size data records such that each element can be efficiently located by its index or its address.

## Binary Trees

## Dictionaries
A dictionary allows access to data items by content. It uses a `key: value` pair to group and store items that can easily be found.

## Disjoint Sets

## Heaps
Heaps are a simple and elegant data structure for efficiently supporting the priority queue operations `insert()` and `extractMin()`. They work by maintaining a partial order on the set of elements which is weaker than the sorted order, but stronger than random order.

## Linked Lists

## Queues
A queue is a type of container that supports retrieval in first-in, first-out (FIFO) order. Its main operations are `enqueue()` and `dequeue()`, which inserts an item at the back of the queue or returns and removes it from the front of the queue, respectively.

## Stacks
A stack is a type of container that supports retrieval by last-in, first-out (LIFO) order. Its main operations are `push()` and `pop()`, which inserts an item at the top of the stack or returns and removes it from the top, respectively.

## Tries

# Graphs
## Breadth First Search
BFS can be used on both directed and undirected graphs, and is most commonly used to locate the shortest path between a starting vertex _s_ and any other vertex that is reachable. In essence, BFS is used to compute distances from a starting vertex _s_ to the other vertices.

BFS can also be used to verify that the graph is a _connected component_. That is, to see if there is a path between every pair of vertices. A great number of seemingly complicated problems reduce to finding connected components. For example, testing whether a Rubik's cube can be solved from any position is really asking whether the graph of legal configurations is connected.

Another use case for BFS could be implementing an algorithm that finds the path from a starting vertex _s_ to a vertex _u_. By storing each vertex's parent, we can reconstruct the path from _s_ to _u_ by working backward, following the chain of ancestors until we reach the root.

In summary, these are some of the possible use cases for BFS:
- Finding the distance from a starting vertex to any other vertex that is reachable.
- Finding the shortest path between two vertices.
- Determining if there is a path between two vertices.
- Finding connected components.

**BFS runs in _O(|V|+|E|)_.**
```python
"""
Preconditions: A directed/undirected graph with no weights.
Result: Shortest path. Minimum spanning tree. Path finding. Cycle detection.
"""
BFS(G,s)
    # Prepare all vertices
    for each vertex u in the set of all vertices
        dist[u] = infinity
        parent[u] = nil

    # Prepare starting vertex
    dist[s] = 0
    parent[s] = nil
    Q = {s}

    # Do work while queue isn't empty
    while Q != 0
        # Process next vertex
        u = dequeue[Q]
        # Process neighbors
        for each v in adjacent vertices of u
            if dist[v] = infinity
                dist[v] = dist[u] + 1
                parent[v] = u
                enqueue[Q,v]
```

## Depth First Search


```
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
```

# Sorts
Sorting is the basic building block that many other algorithms are built around. Here are the most popular sorting algorithms:

## Bucket Sort

## Heap Sort

## Insertion Sort

## Merge Sort
Mergesort uses a recursive approach to partition the elements into two groups, sort each of the smaller problems recursively, and then interleaving the two sorted lists to totally order the elements.

The base case of the recursion occurs when the subarray to be sorted consists of a single element, so no arrangement is possible. For all other cases, the number of elements in a subproblem gets halved at each level.

Because the recursion goes lg(n) levels deep, and a linear amount of work is done per level, mergesort takes _O(nlogn)_ time in the worst case. The efficiency of mergesort depends upon how efficiently we combine the two sorted halves into a single sorted list.

```python
Mergesort(A[1,n])
    Merge(MergeSort(A[1,[n/2]]), MergeSort(A[n/2]+1,n))
```

## Quick Sort

## Radix Sort