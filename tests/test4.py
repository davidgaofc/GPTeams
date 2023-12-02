import timeit
from radon.complexity import cc_visit
import inspect

# Assuming n1, n2, and n3 are different implementations of the Tree structure with find_lowest_common_ancestor method
import extracted_out.question4.n1 as n1
import extracted_out.question4.n2 as n2
import extracted_out.question4.n3 as n3

# Test cases for find_lowest_common_ancestor
# Each case consists of a tuple: (list of (parent, child) pairs to create the tree, value1, value2, expected LCA)
test_cases = [
    # Simple Tree (LCA is root)
    ([(1, 2), (1, 3)], 2, 3, 1),

    # LCA not the root
    ([(1, 2), (1, 3), (2, 4), (2, 5)], 4, 5, 2),

    # One value does not exist
    ([(1, 2), (1, 3)], 4, 3, None),

    # Deeper tree, LCA is not root or direct children
    ([(1, 2), (1, 3), (2, 4), (2, 5), (5, 6), (5, 7)], 6, 7, 5),

    # LCA is one of the nodes
    ([(1, 2), (1, 3), (3, 4)], 3, 4, 3),

    # Both values are the same
    ([(1, 2), (2, 3)], 3, 3, 3),

    # Tree with multiple branches, LCA in deeper level
    ([(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7), (4, 8), (4, 9)], 8, 9, 4),

    # One value in deep branch, other closer to root
    ([(1, 2), (1, 3), (2, 4), (2, 5), (5, 6), (5, 7)], 4, 7, 2),

    # One value is a direct child of the other
    ([(1, 2), (2, 3), (2, 4)], 2, 3, 2),

    # Unbalanced tree, LCA on shorter side
    ([(1, 2), (1, 3), (3, 4), (4, 5), (4, 6)], 2, 5, 1)
]

import signal
class TimeoutException(Exception):
    pass

# Timeout handler function
def timeout_handler(signum, frame):
    raise TimeoutException

# Function to apply the timeout
def with_timeout(seconds, func, *args, **kwargs):
    # Register a signal handler for the alarm signal
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(seconds)  # Set the alarm

    try:
        result = func(*args, **kwargs)
        signal.alarm(0)  # Disable the alarm
        return result
    except TimeoutException:
        return None

# Functional testing
def test_functional(lca_func, TreeClass):
    correct_count = 0
    for edges, value1, value2, expected in test_cases:
        try:
            tree = TreeClass(edges[0][0])  # Create tree with the root value
            for parent, child in edges:
                tree.add_node(parent, child)  # Add nodes to the tree
            lca_value = with_timeout(1, lca_func, tree, value1, value2)
            if lca_value == expected:
                correct_count += 1
        except Exception as e:
            print(f"Error in test case {edges}: {e}")
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
def test_performance(lca_func, TreeClass):
    times = []
    for edges, value1, value2, _ in test_cases:
        try:
            tree = TreeClass(edges[0][0])
            for parent, child in edges:
                tree.add_node(parent, child)
            time_taken = timeit.timeit(
                lambda: with_timeout(1, lca_func, tree, value1, value2), number=10
            )
            times.append(time_taken)
        except Exception as e:
            print(f"Error in performance test for {edges}: {e}")
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
        print(f"Testing solution {n}...")
        lca_func = module.find_lowest_common_ancestor
        TreeClass = module.Tree
        print("functional")
        functional_results = test_functional(lca_func, TreeClass)
        print("complexity")
        complexity = calculate_complexity(lca_func)
        print("performance")
        performance_results = test_performance(lca_func, TreeClass)
        write_results_to_file(f'../test_results/q4-{n}.txt', n, functional_results, complexity, performance_results)

main()