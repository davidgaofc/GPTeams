```python
def find_all_paths(graph, start, end):
    # This function should take a Graph object and two node values, then return all possible paths between these nodes.
    # Expected Input: graph (Graph object), start (node value), end (node value)
    # Expected Output: paths (list of lists, each list is a path from start to end)

    def dfs(node, current_path, paths):
        current_path.append(node)
        if node == end:
            paths.append(current_path[:])
        else:
            for neighbor in graph.edges[node]:
                if neighbor not in current_path:
                    dfs(neighbor, current_path, paths)
        current_path.pop()

    paths = []
    dfs(start, [], paths)
    return paths
```
