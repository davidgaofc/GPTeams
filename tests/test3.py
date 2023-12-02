import timeit
from radon.complexity import cc_visit
import inspect
import extracted_out.question3.n1 as n1  # Assuming n1 contains a version of calculate_convex_hull
import extracted_out.question3.n2 as n2  # Assuming n2 contains another version
import extracted_out.question3.n3 as n3  # Assuming n3 contains yet another version

import math
# Assuming the calculate_convex_hull function is defined properly in n1, n2, n3

# Test cases
test_cases = [
    # Simple square
    ([(0, 0), (1, 1), (0, 1), (1, 0)], [(0, 0), (1, 0), (1, 1), (0, 1)]),

    # Five points, one inside
    ([(0, 0), (2, 0), (1, 1), (2, 2), (0, 2)], [(0, 0), (2, 0), (2, 2), (0, 2)]),

    # Collinear points
    ([(0, 0), (1, 1), (2, 2), (3, 3)], [(0, 0), (3, 3)]),

    # Single point
    ([(1, 1)], [(1, 1)]),

    # Two points
    ([(0, 0), (1, 1)], [(0, 0), (1, 1)]),

    # Points forming a 'U' shape
    ([(0, 0), (0, 2), (1, 1), (2, 2), (2, 0)], [(0, 0), (2, 0), (2, 2), (0, 2)]),

    # Points in a line with one outlier
    ([(0, 0), (1, 1), (2, 2), (3, 3), (2, 4)], [(0, 0), (3, 3), (2, 4)]),

    # Complex shape
    ([(0, 0), (1, 2), (2, 1), (3, 3), (4, 0), (2, 4)], [(0, 0), (4, 0), (3, 3), (2, 4), (1, 2)]),

    # Random distribution
    ([(1, 3), (2, 8), (5, 4), (7, 2), (6, 9), (8, 7), (9, 5)], [(1, 3), (7, 2), (9, 5), (8, 7), (6, 9), (2, 8)]),

    # Large number of points forming a circle
    ([(math.cos(theta), math.sin(theta)) for theta in [i * 2 * math.pi / 20 for i in range(20)]],
     [(math.cos(theta), math.sin(theta)) for theta in [i * 2 * math.pi / 20 for i in range(20)]])
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
def test_functional(convex_hull_func):
    correct_count = 0
    for points, expected_hull in test_cases:
        try:
            calculated_hull = with_timeout(1, convex_hull_func, points)
            if sorted(calculated_hull) == sorted(expected_hull):
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
def test_performance(convex_hull_func):
    times = []
    for points, _ in test_cases:
        try:
            time_taken = timeit.timeit(
                lambda: with_timeout(1, convex_hull_func, points), number=1000
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
        print(f"Testing solution {n}")
        convex_hull_func = module.calculate_convex_hull
        functional_results = test_functional(convex_hull_func)
        print("functional")
        complexity = calculate_complexity(convex_hull_func)
        print("complexity")
        performance_results = test_performance(convex_hull_func)
        print("performance")
        write_results_to_file(f'../test_results/q3-{n}.txt', n, functional_results, complexity, performance_results)

main()