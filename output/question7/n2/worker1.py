```python
def find_all_paths(graph, start, end):
    # This function should take a Graph object and two node values, then return all possible paths between these nodes.
    # Expected Input: graph (Graph object), start (node value), end (node value)
    # Expected Output: paths (list of lists, each list is a path from start to end)
    
    def dfs(current_node, current_path):
        # The depth-first search function takes a current node and current path as input
        # It explores all possible paths from the current node to the end node and appends the paths to the 'paths' list
        if current_node == end:
            paths.append(current_path)
            return
        
        for neighbor in graph.edges[current_node]:
            if neighbor not in current_path:
                dfs(neighbor, current_path + [neighbor])
    
    paths = []
    dfs(start, [start])
    return paths
```