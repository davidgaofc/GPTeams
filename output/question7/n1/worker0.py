```python
def find_all_paths(graph, start, end):
    visited = set()
    paths = []
    
    def dfs(current_node, path):
        visited.add(current_node)
        path.append(current_node)
        
        if current_node == end:
            paths.append(list(path))
        else:
            for neighbor in graph.edges[current_node]:
                if neighbor not in visited:
                    dfs(neighbor, path)
        
        visited.remove(current_node)
        path.pop()
    
    dfs(start, [])
    return paths
```