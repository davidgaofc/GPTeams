import timeit
from radon.complexity import cc_visit
import inspect

import extracted_out.question8.n1 as n1
import extracted_out.question8.n2 as n2
import extracted_out.question8.n3 as n3

# Test cases
test_cases = [
    # Simple linear path: A -10- B -20- C
    (lambda: setup_map(["A", "B", "C"], [("A", "B", 10), ("B", "C", 20)], "A", "C"), ["A", "B", "C"]),

    # Triangle path: A -10- B -20- C -15- A
    (lambda: setup_map(["A", "B", "C"], [("A", "B", 10), ("B", "C", 20), ("C", "A", 15)], "A", "C"), ["A", "C"]),

    # No direct route: A -10- B, C -5- D
    (lambda: setup_map(["A", "B", "C", "D"], [("A", "B", 10), ("C", "D", 5)], "A", "D"), []),

    # Multiple paths with different lengths
    (lambda: setup_map(["A", "B", "C", "D"], [("A", "B", 10), ("B", "C", 15), ("A", "C", 30), ("C", "D", 20)], "A", "D"), ["A", "B", "C", "D"]),

    # Circular path with multiple entries and exits
    (lambda: setup_map(["A", "B", "C", "D"], [("A", "B", 10), ("B", "C", 15), ("C", "D", 20), ("D", "A", 25)], "A", "D"), ["A", "D"]),

    # Large map with multiple routes
    (lambda: setup_map(["A", "B", "C", "D", "E", "F"], [("A", "B", 5), ("B", "C", 10), ("C", "D", 15), ("D", "E", 20), ("E", "F", 25), ("A", "F", 100)], "A", "F"), ["A", "B", "C", "D", "E", "F"]),

    # Route with a dead end
    (lambda: setup_map(["A", "B", "C", "D"], [("A", "B", 10), ("B", "C", 20), ("C", "D", 30)], "A", "D"), ["A", "B", "C", "D"]),

    # Isolated cities with no routes
    (lambda: setup_map(["A", "B", "C", "D"], [], "A", "D"), []),

    # Map with loops and multiple connections
    (lambda: setup_map(["A", "B", "C", "D", "E"], [("A", "B", 10), ("B", "C", 20), ("C", "A", 30), ("C", "D", 40), ("D", "E", 50), ("E", "A", 60)], "A", "E"), ["A", "B", "C", "D", "E"]),

]

# Setup function for test data
def setup_map(cities, roads, start_city_name, end_city_name):
    # Create cities and roads, add them to a TransportationMap instance
    # Return the map, start city, and end city for a test case
    transport_map = n1.TransportationMap()
    city_objs = {city_name: n1.City(city_name) for city_name in cities}

    # Add cities to the map
    for city in city_objs.values():
        transport_map.add_city(city)

    # Add roads to the map
    for start, end, length in roads:
        road = n1.Road(city_objs[start], city_objs[end], length)
        transport_map.add_road(road)

    start_city = city_objs[start_city_name]
    end_city = city_objs[end_city_name]

    return transport_map, start_city, end_city

# Functional testing
def test_functional(route_func):
    correct_count = 0
    for setup_func, expected in test_cases:
        try:
            transport_map, start_city, end_city = setup_func()
            shortest_route = route_func(transport_map, start_city, end_city)
            for i in range(len(shortest_route)):
                shortest_route[i] = shortest_route[i].name
            if shortest_route == expected:
                correct_count += 1
        except Exception as e:
            pass
            # print(f"Error in test case: {e}")
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
def test_performance(route_func):
    times = []
    for setup_func, _ in test_cases:
        try:
            transport_map, start_city, end_city = setup_func()
            time_taken = timeit.timeit(
                lambda: route_func(transport_map, start_city, end_city), number=100
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
        find_shortest_route = module.find_shortest_route
        functional_results = test_functional(find_shortest_route)
        complexity = calculate_complexity(find_shortest_route)
        performance_results = test_performance(find_shortest_route)
        write_results_to_file(f'../test_results/q8-{n}.txt', n, functional_results, complexity, performance_results)
if __name__ == "__main__":
    main()