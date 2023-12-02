import timeit
from radon.complexity import cc_visit
import inspect
import extracted_out.question2.n1 as n1
import extracted_out.question2.n2 as n2
import extracted_out.question2.n3 as n3

# Function to check if a binary search tree is balanced
def is_tree_balanced(root):
    if root is None:
        return True
    balance = n1.analyze_tree_balance(root)
    return abs(balance) <= 1 and is_tree_balanced(root.left) and is_tree_balanced(root.right)

# Test cases
test_cases = [
    ([], True),  # Empty tree
    ([3], True),  # Single node
    ([3, 1, 4], True),  # Already balanced tree
    ([5, 4, 3, 2, 1], True),  # Left skewed tree
    ([1, 2, 3, 4, 5], True),  # Right skewed tree
    ([4, 2, 6, 1, 5, 7], True),  # Small unbalanced tree
    ([8, 3, 10, 1, 6, 14, 4, 7, 13], True),  # Large unbalanced tree
    ([3, 1, 5, 2, 4, 6, 7], True),  # Tree with multiple levels
    ([5, 3, 7, 3, 5, 5], True),  # Tree with repeated values
    ([7, 2, 9, 1, 5, 8, 10, 3, 6], True),  # Randomly generated tree
]

# Functional testing
def test_functional(balance_tree_func):
    correct_count = 0
    for values, expected in test_cases:
        try:
            tree = n1.create_binary_search_tree(values)
            balanced_tree = balance_tree_func(tree)
            result = is_tree_balanced(balanced_tree)
            if result == expected:
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
def test_performance(balance_tree_func):
    times = []
    for values, _ in test_cases:
        try:
            tree = n1.create_binary_search_tree(values)
            time_taken = timeit.timeit(
                lambda: balance_tree_func(tree), number=1000
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
        balance_tree_func = module.balance_binary_search_tree
        functional_results = test_functional(balance_tree_func)
        complexity = calculate_complexity(balance_tree_func)
        performance_results = test_performance(balance_tree_func)
        write_results_to_file(f'../test_results/q2-{n}.txt', n, functional_results, complexity, performance_results)

main()