import timeit
from radon.complexity import cc_visit
import inspect
import extracted_out.question1.n1 as n1
import extracted_out.question1.n2 as n2
import extracted_out.question1.n3 as n3

def create_test_graph(edges):
    graph = n1.Graph()
    for vertex1, vertex2 in edges:
        if vertex1 not in graph.adjacency_list:
            graph.add_vertex(vertex1)
        if vertex2 not in graph.adjacency_list:
            graph.add_vertex(vertex2)
        graph.add_edge(vertex1, vertex2)
    return graph

# Test cases
test_cases = [
    ([], []),  # Empty graph
    ([], []),  # Single vertex
    ([('A', 'B')], []),  # Two connected vertices
    ([('A', 'B'), ('B', 'C'), ('C', 'D')], ['B', 'C']),  # Linear graph
    ([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A')], []),  # Circular graph
    ([('A', 'B'), ('A', 'C'), ('A', 'D')], ['A']),  # Star graph
    ([('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'E')], ['A']),  # Tree graph
    ([('A', 'B'), ('B', 'C'), ('C', 'A'), ('B', 'D'), ('D', 'E')], ['B', 'D']),  # Complex graph with multiple articulation points
    ([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A'), ('A', 'C'), ('B', 'D')], []),  # Fully connected graph
    ([('A', 'B'), ('B', 'C'), ('D', 'E')], ['B']),  # Graph with isolated vertex
]

# Functional testing
def test_functional(find_articulation_points_func):
    # results = []
    correct_count = 0
    for edges, expected in test_cases:
        try:
            graph = create_test_graph(edges)
            result = find_articulation_points_func(graph)
            if(result == expected):
                correct_count += 1
        except:
            pass
    return correct_count

# Cyclomatic complexity
def calculate_complexity(func):
    source_code = inspect.getsource(func)
    complexity_result = cc_visit(source_code)
    for item in complexity_result:
        # print(item.name, item.complexity)
        if item.name == func.__name__:
            return item.complexity
    return None

# Performance testing
def test_performance(find_articulation_points_func):
    times = []
    for edges, _ in test_cases:
        try:
            graph = create_test_graph(edges)
            time_taken = timeit.timeit(
                lambda: find_articulation_points_func(graph), number=1000
            )
            times.append(time_taken)
        except:
            pass
    if(len(times) == 0):
        return None
    return sum(times)/len(times)

# Writing results to a file
def write_results_to_file(filename, n, functional_results, complexity, performance_results):
    with open(filename, 'w') as file:
        file.write(f"Results for solution {n}:\n")
        file.write("Functional Test Results:")
        file.write(str(functional_results) + '\n')
        file.write("Cyclomatic Complexity: " + str(complexity) + '\n')
        file.write("Performance Test Results:")
        file.write(str(performance_results) + '\n')

def main():
    for n, func in enumerate([n1, n2, n3], 1):
        # print(n, func)
        func = func.find_articulation_points
        functional_results = test_functional(func)
        complexity = calculate_complexity(func)
        performance_results = test_performance(func)
        write_results_to_file(f'../test_results/q1-{n}.txt', n, functional_results, complexity, performance_results)

main()