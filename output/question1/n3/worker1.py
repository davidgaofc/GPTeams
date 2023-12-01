```python
def find_articulation_points(graph):
    # This function should take a Graph object and find all articulation points (cut vertices) in the graph.
    # An articulation point is a vertex which, when removed, increases the number of connected components in the graph.
    # This function should implement an algorithm like Tarjan's algorithm.
    # Expected Input: graph (Graph object)
    # Expected Output: articulation_points (list of vertices that are articulation points)
    articulation_points = []

    # Helper function to perform the depth-first search
    def dfs(node, parent, visited, disc, low, time, articulation_points):
        # Count of child nodes
        children = 0

        # Mark node as visited
        visited[node] = True

        # Initialize discovery time and low value
        disc[node] = time
        low[node] = time
        time += 1

        # Go through all adjacent vertices
        for neighbor in graph.adjacency_list[node]:
            if visited[neighbor] == False:
                # Set parent of neighboring vertex
                parent[neighbor] = node
                children += 1

                # Recursive call to the depth-first search
                dfs(neighbor, parent, visited, disc, low, time, articulation_points)

                # Update low value
                low[node] = min(low[node], low[neighbor])

                # Check if node is an articulation point
                if parent[node] == -1 and children > 1:
                    articulation_points.append(node)
                elif parent[node] != -1 and low[neighbor] >= disc[node]:
                    articulation_points.append(node)

            # Update low value of the node
            elif neighbor != parent[node]:
                low[node] = min(low[node], disc[neighbor])

    # Initialize data structures
    visited = {vertex: False for vertex in graph.adjacency_list}
    disc = {vertex: float('inf') for vertex in graph.adjacency_list}
    low = {vertex: float('inf') for vertex in graph.adjacency_list}
    parent = {vertex: -1 for vertex in graph.adjacency_list}
    time = 0

    # Call helper function for each unvisited vertex
    for vertex in graph.adjacency_list:
        if visited[vertex] == False:
            dfs(vertex, parent, visited, disc, low, time, articulation_points)

    return articulation_points
```