import heapq
import random

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        if from_node not in self.edges:
            self.edges[from_node] = {}
        self.edges[from_node][to_node] = distance

    def find_shortest_path(self, start, end):
        distances = {node: float('infinity') for node in self.nodes}
        distances[start] = 0
        priority_queue = [(0, start)]

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            if current_distance > distances[current_node]:
                continue

            for neighbor, weight in self.edges[current_node].items():
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances[end]

class DataAnalyzer:
    def __init__(self, data):
        self.data = data

    def mean(self):
        return sum(self.data) / len(self.data)

    def median(self):
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        mid = n // 2
        if n % 2 == 1:
            return sorted_data[mid]
        else:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2

    def mode(self):
        frequency = {}
        for item in self.data:
            frequency[item] = frequency.get(item, 0) + 1
        max_frequency = max(frequency.values())
        modes = [key for key, value in frequency.items() if value == max_frequency]
        return modes

def create_graph():
    g = Graph()
    for i in range(1, 6):
        g.add_node(i)
    edges = [(1, 2, 2), (1, 3, 5), (2, 3, 1), (2, 4, 7), (3, 4, 3), (3, 5, 1), (4, 5, 2)]
    for from_node, to_node, distance in edges:
        g.add_edge(from_node, to_node, distance)
    return g

def shortest_path(graph, start, end):
    return graph.find_shortest_path(start, end)

def analyze_data(data):
    analyzer = DataAnalyzer(data)
    return {
        'mean': analyzer.mean(),
        'median': analyzer.median(),
        'mode': analyzer.mode()
    }

# TODO: Implement 'find_all_paths'
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