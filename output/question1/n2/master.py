def find_articulation_points(graph):
    # This function should take a Graph object and find all articulation points (cut vertices) in the graph.
    # An articulation point is a vertex which, when removed, increases the number of connected components in the graph.
    # This function should implement an algorithm like Tarjan's algorithm.
    # Expected Input: graph (Graph object)
    # Expected Output: articulation_points (list of vertices that are articulation points)
    
    # Initialize variables
    visited = set()
    parent = {}
    low = {}
    discovery = {}
    articulation_points = []
    time = 0

    # Helper function to find articulation points
    def find_articulation_points_helper(vertex):
        nonlocal time
        nonlocal articulation_points
        
        # Mark the current vertex as visited
        visited.add(vertex)
        
        # Initialize discovery time and low value for the current vertex
        discovery[vertex] = time
        low[vertex] = time
        
        # Increment the time
        time += 1
        
        # Count of children in the current vertex
        children = 0
        
        # Iterate over each neighbor of the current vertex
        for neighbor in graph.get_neighbors(vertex):
            # If the neighbor is not visited, increment the count of children in the current vertex
            if neighbor not in visited:
                children += 1
                parent[neighbor] = vertex
                find_articulation_points_helper(neighbor)
                
                # Check if the current vertex is an articulation point
                if parent[vertex] is None and children > 1:
                    articulation_points.append(vertex)
                if parent[vertex] is not None and low[neighbor] >= discovery[vertex]:
                    articulation_points.append(vertex)
                    
                # Update the low value of the current vertex
                low[vertex] = min(low[vertex], low[neighbor])
            
            # If the neighbor is visited and not the parent of the current vertex, update the low value of the current vertex
            elif neighbor != parent[vertex]:
                low[vertex] = min(low[vertex], discovery[neighbor])
    
    # Iterate over each vertex in the graph
    for vertex in graph.adjacency_list.keys():
        if vertex not in visited:
            find_articulation_points_helper(vertex)
    
    # Return the list of articulation points
    return articulation_points