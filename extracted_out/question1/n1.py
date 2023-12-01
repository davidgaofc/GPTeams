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
    # This function should take a Graph object and find all articulation points (cut vertices) in the graph.
    # An articulation point is a vertex which, when removed, increases the number of connected components in the graph.
    # This function should implement an algorithm like Tarjan's algorithm.
    # Expected Input: graph (Graph object)
    # Expected Output: articulation_points (list of vertices that are articulation points)
    pass