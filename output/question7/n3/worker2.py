```python
# TODO: Implement 'find_all_paths'
def find_all_paths(graph, start, end):
    def dfs(current, visited, path, paths):
        visited.add(current)
        path.append(current)
        if current == end:
            paths.append(list(path))
        else:
            neighbors = graph.get_neighbors(current)
            for neighbor in neighbors:
                if neighbor not in visited:
                    dfs(neighbor, visited, path, paths)
        visited.remove(current)
        path.pop()
    
    paths = []
    visited = set()
    path = []
    dfs(start, visited, path, paths)
    return paths
```