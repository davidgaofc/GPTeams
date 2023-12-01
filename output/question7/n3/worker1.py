```python
def find_all_paths(graph, start, end):
    paths = []
    stack = [(start, [start])]
    
    while stack:
        node, path = stack.pop()
        
        if node == end:
            paths.append(path)
        
        for neighbor in graph.edges[node]:
            if neighbor not in path:
                stack.append((neighbor, path + [neighbor]))
    
    return paths
```