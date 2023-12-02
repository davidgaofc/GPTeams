import timeit
from radon.complexity import cc_visit
import inspect
import extracted_out.question7.n1 as n1
import extracted_out.question7.n2 as n2
import extracted_out.question7.n3 as n3
# Test cases for find_all_paths
test_cases = [
    # Case 1: Simple path between two directly connected nodes
    ([(1, 2, 1)], 1, 2, [[1, 2]]),

    # Case 2: Multiple paths between two nodes
    ([(1, 2, 1), (2, 3, 1), (1, 3, 2)], 1, 3, [[1, 2, 3], [1, 3]]),

    # Case 3: No path between two nodes
    ([(1, 2, 1)], 2, 3, []),

    # Case 4: Paths in a graph with cycles
    ([(1, 2, 1), (2, 3, 1), (3, 1, 1), (3, 4, 1)], 1, 4, [[1, 2, 3, 4]]),

    # Case 5: Paths in a large graph
    ([(1, 2, 1), (2, 3, 1), (3, 4, 1), (4, 5, 1), (1, 5, 5)], 1, 5, [[1, 2, 3, 4, 5], [1, 5]]),

    # Case 6: Path from a node to itself
    ([(1, 2, 1), (2, 3, 1)], 1, 1, [[1]]),

    # Case 7: Paths in a graph with multiple edges and nodes
    ([(1, 2, 1), (2, 3, 1), (3, 4, 1), (4, 5, 1), (2, 4, 2), (1, 3, 3)], 1, 5, [[1, 2, 3, 4, 5], [1, 2, 4, 5], [1, 3, 4, 5]]),

    # Case 8: Complex graph with many paths
    ([(1, 2, 1), (2, 4, 1), (1, 3, 1), (3, 4, 1), (2, 3, 1), (3, 5, 1), (4, 5, 1)], 1, 5, [[1, 2, 3, 5], [1, 2, 4, 5], [1, 3, 4, 5], [1, 3, 5]]),

    # Case 9: Graph with no connection to end node
    ([(1, 2, 1), (2, 3, 1), (3, 4, 1)], 1, 5, []),

    # Case 10: Graph with a single node
    ([(1, 1, 0)], 1, 1, [[1]])
]

# Create a graph from a list of edges
def create_graph_from_edges(edges):
    g = n1.Graph()
    nodes = set()
    for edge in edges:
        nodes.update(edge[:2])
    for node in nodes:
        g.add_node(node)
    for edge in edges:
        g.add_edge(*edge)
    return g

# Functional testing
def test_functional(find_all_paths_func):
    correct_count = 0
    for edges, start, end, expected_paths in test_cases:
        try:
            graph = create_graph_from_edges(edges)
            actual_paths = find_all_paths_func(graph, start, end)
            if sorted(actual_paths) == sorted(expected_paths):
                correct_count += 1
        except:
            pass
    return correct_count

# Cyclomatic complexity
def calculate_complexity(func):
    source_code = inspect.getsource(func)
    complexity_result = cc_visit(source_code)
    for item in complexity_result:
        if item.name == func.__name__:
            return item.complexity
    return None

# Performance testing
def test_performance(find_all_paths_func):
    times = []
    for edges, start, end, _ in test_cases:
        try:
            graph = create_graph_from_edges(edges)
            time_taken = timeit.timeit(
                lambda: find_all_paths_func(graph, start, end), number=1000
            )
            times.append(time_taken)
        except:
            pass
    return sum(times) / len(times) if times else None

# Writing results to a file
def write_results_to_file(filename, n, functional_results, complexity, performance_results):
    with open(filename, 'w') as file:
        file.write(f"Results for solution {n}:\n")
        file.write("Functional Test Results: " + str(functional_results) + '\n')
        file.write("Cyclomatic Complexity: " + str(complexity) + '\n')
        file.write("Performance Test Results: " + str(performance_results) + '\n')

def main():
    for n, module in enumerate([n1, n2, n3], 1):
        find_all_paths_func = module.find_all_paths
        functional_results = test_functional(find_all_paths_func)
        complexity = calculate_complexity(find_all_paths_func)
        performance_results = test_performance(find_all_paths_func)
        write_results_to_file(f'../test_results/q7-{n}.txt', n, functional_results, complexity, performance_results)

main()