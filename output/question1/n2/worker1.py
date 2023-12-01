```python
def find_articulation_points(graph):
    # This function should take a Graph object and find all articulation points (cut vertices) in the graph.
    # An articulation point is a vertex which, when removed, increases the number of connected components in the graph.
    # This function should implement an algorithm like Tarjan's algorithm.
    # Expected Input: graph (Graph object)
    # Expected Output: articulation_points (list of vertices that are articulation points)
    
    # Initialize variables
    visited = {}
    parent = {}
    low = {}
    articulation_points = []

    # Helper function to perform depth-first search
    def dfs(vertex, time):
        visited[vertex] = True
        low[vertex] = time
        disc[vertex] = time
        time += 1
        children = 0

        # Iterate through each neighbor of the current vertex
        for neighbor in graph.get_neighbors(vertex):
            # If neighbor vertex is not visited, recursively call dfs on it
            if not visited.get(neighbor):
                parent[neighbor] = vertex
                children += 1
                dfs(neighbor, time)

                # Check if the subtree rooted at neighbor vertex has a connection to one of the ancestors of the current vertex
                low[vertex] = min(low[vertex], low[neighbor])

                # Check if the current vertex is an articulation point
                if parent[vertex] is None and children > 1:
                    articulation_points.append(vertex)
                if parent[vertex] is not None and low[neighbor] >= visited[vertex]:
                    articulation_points.append(vertex)
            
            # Update low value of vertex if the neighbor vertex is already visited and not the parent of vertex
            elif neighbor != parent[vertex]:
                low[vertex] = min(low[vertex], disc[neighbor])

    # Iterate through each vertex in the graph
    for vertex in graph.adjacency_list:
        if not visited.get(vertex):
            dfs(vertex, 0)

    return articulation_points
```