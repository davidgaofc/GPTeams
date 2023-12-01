class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)  # Assuming an undirected graph

    def get_neighbors(self, vertex):
        return self.adjacency_list.get(vertex, [])

def create_graph():
    return Graph()

def add_vertex_to_graph(graph, vertex):
    graph.add_vertex(vertex)

def add_edge_to_graph(graph, vertex1, vertex2):
    graph.add_edge(vertex1, vertex2)

# TODO: Implement 'find_articulation_points'
def find_articulation_points(graph):
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