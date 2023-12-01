```python
def find_articulation_points(graph):
    articulation_points = []

    # Initialize the time and low arrays
    time = 0
    low = {}
    visited = {}

    # Get the first vertex in the graph
    start_vertex = next(iter(graph.adjacency_list))
    
    def dfs(vertex, parent):
        nonlocal time
        nonlocal low

        # Count the number of children in the DFS tree
        children = 0

        # Mark the current vertex as visited
        visited[vertex] = True
        
        # Initialize discovery time and low value
        discovery_time[vertex] = time
        low[vertex] = time
        time += 1

        # Go through all adjacent vertices of the current vertex
        for adjacent_vertex in graph.adjacency_list[vertex]:
            # If the vertex has not been visited yet, visit it
            if adjacent_vertex not in visited:
                children += 1
                dfs(adjacent_vertex, vertex)
                
                # Update the low value of the current vertex
                low[vertex] = min(low[vertex], low[adjacent_vertex])
                
                # Check if the current vertex is an articulation point
                if parent is None and children > 1:
                    articulation_points.append(vertex)
                elif parent is not None and low[adjacent_vertex] >= discovery_time[vertex]:
                    articulation_points.append(vertex)
            
            # Update the low value of the current vertex
            elif adjacent_vertex != parent:
                low[vertex] = min(low[vertex], discovery_time[adjacent_vertex])
            
    # Start the DFS from the first vertex in the graph
    dfs(start_vertex, None)
    
    return articulation_points
```

This implementation uses a modified depth-first search (DFS) algorithm to find the articulation points in the graph. The time and low arrays are used to track the discovery time and low value of each vertex during the DFS traversal. The low value of a vertex is the earliest discovery time of any of its adjacent vertices, including its parent.

The DFS function is recursively called on each unvisited adjacent vertex of the current vertex. When a back edge is encountered (i.e., an adjacent vertex that has already been visited and is not the parent), the low value of the current vertex is updated to the minimum of its current low value and the discovery time of the adjacent vertex.

For a vertex to be an articulation point, it must satisfy one of the following conditions:
- It is the root of the DFS tree and has more than one child.
- It is not the root of the DFS tree and its low value is greater than or equal to its discovery time.

The algorithm starts the DFS traversal from the first vertex in the graph and returns a list of articulation points.