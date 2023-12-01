```python
def find_all_paths(graph, start, end):
    # This function should take a Graph object and two node values, then return all possible paths between these nodes.
    # Expected Input: graph (Graph object), start (node value), end (node value)
    # Expected Output: paths (list of lists, each list is a path from start to end)
    paths = []
    visited = set()
    current_path = []
    
    # Helper function to recursively find all paths
    def dfs(node):
        visited.add(node)
        current_path.append(node)
        
        if node == end:
            paths.append(current_path[:])
        else:
            for neighbor in graph.edges[node].keys():
                if neighbor not in visited:
                    dfs(neighbor)
        
        # Backtrack
        visited.remove(node)
        current_path.pop()
    
    dfs(start)
    return paths
```