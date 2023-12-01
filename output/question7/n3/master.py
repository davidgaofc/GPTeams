def find_all_paths(graph, start, end):
    paths = []
    visited = set()
    current_path = []
    
    def dfs(node):
        visited.add(node)
        current_path.append(node)
        
        if node == end:
            paths.append(current_path[:])
        else:
            for neighbor in graph.edges[node].keys():
                if neighbor not in visited:
                    dfs(neighbor)
        
        visited.remove(node)
        current_path.pop()
    
    dfs(start)
    
    paths2 = []
    stack = [(start, [start])]
    
    while stack:
        node, path = stack.pop()
        
        if node == end:
            paths2.append(path)
        
        for neighbor in graph.edges[node]:
            if neighbor not in path:
                stack.append((neighbor, path + [neighbor]))
    
    paths3 = []
    visited = set()
    path = []
    
    def dfs2(current, visited, path, paths):
        visited.add(current)
        path.append(current)
        
        if current == end:
            paths.append(list(path))
        else:
            neighbors = graph.get_neighbors(current)
            for neighbor in neighbors:
                if neighbor not in visited:
                    dfs2(neighbor, visited, path, paths)
        
        visited.remove(current)
        path.pop()
    
    dfs2(start, visited, path, paths3)
    
    return paths + paths2 + paths3