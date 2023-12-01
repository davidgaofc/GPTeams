def find_articulation_points(graph):
    # Initialize variables
    articulation_points = []
    discovery_time = {}
    low_link = {}
    time = 0
    visited = set()

    # DFS traversal
    def dfs(vertex, parent):
        nonlocal time
        # Store the discovery time of the vertex
        discovery_time[vertex] = time
        # Initialize low link as the discovery time
        low_link[vertex] = time
        time += 1

        # Track the number of children of the current vertex
        children = 0

        # Mark the vertex as visited
        visited.add(vertex)

        # Iterate over all neighboring vertices
        for neighbor in graph.get_neighbors(vertex):
            # Check if the neighbor is not visited
            if neighbor not in visited:
                # Increment the number of children
                children += 1
                # Recursively explore the neighbor
                dfs(neighbor, vertex)

                # Update the low link of the vertex based on the low link of the neighbor
                low_link[vertex] = min(low_link[vertex], low_link[neighbor])

                # Check for articulation points
                if parent is None and children > 1:
                    articulation_points.append(vertex)
                elif parent is not None and low_link[neighbor] >= discovery_time[vertex]:
                    articulation_points.append(vertex)

            # If the neighbor is already visited and not the parent, update the low link of the vertex
            elif neighbor != parent:
                low_link[vertex] = min(low_link[vertex], discovery_time[neighbor])

    # Perform DFS traversal on all vertices
    for vertex in graph.get_vertices():
        if vertex not in visited:
            dfs(vertex, None)

    # Return the list of articulation points
    return articulation_points