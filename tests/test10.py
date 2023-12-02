import timeit
from radon.complexity import cc_visit
import inspect
import extracted_out.question10.n1 as n1
import extracted_out.question10.n2 as n2
import extracted_out.question10.n3 as n3
# Test cases
test_cases = [
    ([1, -3], ["3"]),

    # Quadratic Polynomial (Two Real Roots)
    ([1, -5, 6], ["2", "3"]),

    # Quadratic Polynomial (Complex Roots)
    ([1, 0, 1], ["-i", "i"]),

    # Cubic Polynomial (Three Real Roots)
    ([1, -6, 11, -6], ["1", "2", "3"]),

    # Cubic Polynomial (One Real and Two Complex Roots)
    ([1, -3, 3, -1], ["1", "1 + i", "1 - i"]),

    # Quartic Polynomial (Four Real Roots)
    ([1, -10, 35, -50, 24], ["1", "2", "3", "4"]),

    # Quartic Polynomial (Two Real and Two Complex Roots)
    ([1, 0, -2, 0, 1], ["-1", "1", "i", "-i"]),

    # Polynomial with Repeated Roots
    ([1, -4, 6, -4, 1], ["1", "1", "1", "1"]),

    # Polynomial with All Complex Roots
    ([1, 0, 0, 0, 1], ["i", "-i", "i", "-i"]),

    # Polynomial with All Real Roots
    ([1, 0, 0, 0, 0], ["0", "0", "0", "0"]),
]

# Functional testing
def test_functional(find_roots_func):
    correct_count = 0
    for coefficients, expected_roots in test_cases:
        try:
            polynomial = n1.create_polynomial(coefficients)
            roots = find_roots_func(polynomial)
            # Convert roots to a standard format for comparison
            roots = sorted([str(root) for root in roots])
            if roots == expected_roots:
                correct_count += 1
            else:
                print(f"Returned roots: {roots}, Expected roots: {expected_roots}")
                user_input = input("Is this result correct? (y/n): ")
                if user_input.lower() == 'y':
                    correct_count += 1
        except Exception as e:
            print(f"Error for coefficients {coefficients}: {e}")
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
def test_performance(find_roots_func):
    times = []
    for coefficients, _ in test_cases:
        try:
            polynomial = n1.create_polynomial(coefficients)
            time_taken = timeit.timeit(
                lambda: find_roots_func(polynomial), number=1000
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
        find_roots_func = module.find_polynomial_roots
        functional_results = test_functional(find_roots_func)
        complexity = calculate_complexity(find_roots_func)
        performance_results = test_performance(find_roots_func)
        write_results_to_file(f'../test_results/q10-{n}.txt', n, functional_results, complexity, performance_results)

main()