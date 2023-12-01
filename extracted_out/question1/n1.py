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
    articulation_points = []

    # Create a variable to keep track of the discovery time of each vertex
    discovery_time = {}

    # Create a variable to keep track of the lowest discovery time reachable from each vertex
    lowest_reachable_time = {}

    # Create a variable to keep track of the parent of each vertex
    parent = {}

    # Create a variable to keep track of the number of children of each vertex
    children_count = {}

    # Create a variable to keep track of the current time
    time = 0

    # Create a helper function to perform depth-first search
    def dfs(vertex):
        nonlocal time

        # Increment the time and set the discovery time and lowest reachable time of the vertex
        time += 1
        discovery_time[vertex] = time
        lowest_reachable_time[vertex] = time

        # Initialize the number of children of the vertex
        children_count[vertex] = 0

        # Iterate over the neighbors of the vertex
        for neighbor in graph.get_neighbors(vertex):
            # If the neighbor is the parent of the vertex, continue to the next neighbor
            if neighbor == parent[vertex]:
                continue

            # If the neighbor has not been visited yet, set its parent and perform dfs
            if neighbor not in discovery_time:
                parent[neighbor] = vertex
                children_count[vertex] += 1
                dfs(neighbor)

                # Update the lowest reachable time of the vertex based on the lowest reachable time of its neighbor
                lowest_reachable_time[vertex] = min(lowest_reachable_time[vertex], lowest_reachable_time[neighbor])

                # Check if the vertex is an articulation point
                if parent[vertex] is not None and lowest_reachable_time[neighbor] >= discovery_time[vertex]:
                    articulation_points.append(vertex)

            # If the neighbor has been visited and is not the parent of the vertex, update the lowest reachable time of the vertex
            else:
                lowest_reachable_time[vertex] = min(lowest_reachable_time[vertex], discovery_time[neighbor])

        # Check if the vertex is the root of the DFS tree and has more than one child
        if parent[vertex] is None and children_count[vertex] > 1:
            articulation_points.append(vertex)

    # Iterate over all vertices in the graph
    for vertex in graph.adjacency_list:
        # If the vertex has not been visited, perform dfs
        if vertex not in discovery_time:
            parent[vertex] = None
            dfs(vertex)

    # Return the list of articulation points
    return articulation_points