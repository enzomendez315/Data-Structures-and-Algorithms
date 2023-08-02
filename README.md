# Data Structures and Algorithms
This is a manual showing the implementation and usage of popular algorithms and data structures using Python.

## Data Structures
### Arrays
An array is a contiguously-allocated data structure. Arrays are structures of fixed-size data records such that each element can be efficiently located by its index or its address.

### Binary Trees

### Dictionaries
A dictionary allows access to data items by content. It uses a `key: value` pair to group and store items that can easily be found.

### Disjoint Sets

### Heaps
Heaps are a simple and elegant data structure for efficiently supporting the priority queue operations `insert()` and `extractMin()`. They work by maintaining a partial order on the set of elements which is weaker than the sorted order, but stronger than random order.

### Linked Lists

### Queues
A queue is a type of container that supports retrieval in first-in, first-out (FIFO) order. Its main operations are `enqueue()` and `dequeue()`, which inserts an item at the back of the queue or returns and removes it from the front of the queue, respectively.

### Stacks
A stack is a type of container that supports retrieval by last-in, first-out (LIFO) order. Its main operations are `push()` and `pop()`, which inserts an item at the top of the stack or returns and removes it from the top, respectively.

### Tries

## Graphs
### Breadth First Search
BFS is most commonly used to locate the shortest path between a starting vertex and any other vertex that is reachable.

```
BFS(G,s)
    for each vertex u in the set of all vertices - {s}
        state[u] = "undiscovered"
        parent[u] = nil (no parent is in the BFS tree)
    state[s] = "discovered"
    parent[s] = nil
    Q = {s}
    while Q != 0
        u = dequeue[Q]
        for each v in adjacent vertices of u    // Process vertex u
            if state[v] = "undiscovered"        // Process edge (u,v)
                state[v] = "discovered"
                parent[v] = u
                enqueue[Q,v]
        state[u] = "processed"
```

## Sorts
Sorting is the basic building block that many other algorithms are built around. Here are the most popular sorting algorithms:

### Bucket Sort

### Heap Sort

### Insertion Sort

### Merge Sort
Mergesort uses a recursive approach to partition the elements into two groups, sort each of the smaller problems recursively, and then interleaving the two sorted lists to totally order the elements.

The base case of the recursion occurs when the subarray to be sorted consists of a single element, so no arrangement is possible. For all other cases, the number of elements in a subproblem gets halved at each level.

Because the recursion goes lg(n) levels deep, and a linear amount of work is done per level, mergesort takes _O(nlogn)_ time in the worst case. The efficiency of mergesort depends upon how efficiently we combine the two sorted halves into a single sorted list.

```
Mergesort(A[1,n])
    Merge(MergeSort(A[1,[n/2]]), MergeSort(A[n/2]+1,n))
```

### Quick Sort

### Radix Sort