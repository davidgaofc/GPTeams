import timeit
from radon.complexity import cc_visit
import inspect

import extracted_out.question9.n1 as n1
import extracted_out.question9.n2 as n2
import extracted_out.question9.n3 as n3


# Define the test cases for optimize_vehicle_loading
test_cases = [
    # Empty Warehouse
    ([], 100, []),

    # Warehouse with Light Products
    ([('apple', 1, 50), ('banana', 1, 50)], 100, [('apple', 50), ('banana', 50)]),

    # Warehouse with Heavy Products
    ([('fridge', 100, 2), ('washing_machine', 120, 1)], 80, []),

    # Exact Weight Match
    ([('box', 10, 10)], 100, [('box', 10)]),

    # Mixed Product Weights
    ([('small_box', 5, 10), ('large_box', 20, 3)], 100, [('small_box', 10), ('large_box', 3)]),

    # Insufficient Vehicle Capacity
    ([('couch', 150, 1)], 100, []),

    # Large Warehouse and Vehicle
    ([('item1', 10, 20), ('item2', 15, 30)], 1000, [('item1', 20), ('item2', 30)]),

    # Repeated Product Types
    ([('chair', 5, 10), ('chair', 5, 10)], 100, [('chair', 20)]),

    # Random Product Weights and Quantities
    ([('itemA', 7, 5), ('itemB', 12, 8)], 150, [('itemA', 5), ('itemB', 8)]),

    # Balanced Loading (if applicable)
    # Assuming balanced loading means evenly distributing the weight
    ([('left_side', 30, 1), ('right_side', 30, 1)], 100, [('left_side', 1), ('right_side', 1)]),
]

def is_loading_correct(loaded_products, expected_load, vehicle_capacity):
    total_weight = 0
    if(loaded_products is None):
        return True
    for product, weight, quantity in loaded_products:
        if (product.name, quantity) not in expected_load:
            return False
        total_weight += product.weight * quantity

    return total_weight <= vehicle_capacity

def test_functional(loading_func):
    correct_count = 0
    for warehouse_setup, vehicle_capacity, expected_load in test_cases:
        try:
            warehouse = n1.Warehouse()
            for product, weight, quantity in warehouse_setup:
                warehouse.add_product(n1.Product(product, weight), quantity)

            vehicle = n1.DeliveryVehicle(vehicle_capacity)
            loaded_products = loading_func(warehouse, vehicle)
            # print(loaded_products, expected_load, vehicle_capacity)
            if is_loading_correct(loaded_products, expected_load, vehicle_capacity):
                correct_count += 1
        except:
            # print("Error")
            pass
    return correct_count

def calculate_complexity(func):
    source_code = inspect.getsource(func)
    complexity_result = cc_visit(source_code)
    for item in complexity_result:
        if item.name == func.__name__:
            return item.complexity
    return None

def test_performance(loading_func):
    times = []
    for warehouse_setup, vehicle_capacity, _ in test_cases:
        try:
            warehouse = n1.Warehouse()
            for product, quantity in warehouse_setup:
                warehouse.add_product(n1.Product(product[0], product[1]), quantity)

            vehicle = n1.DeliveryVehicle(vehicle_capacity)
            time_taken = timeit.timeit(
                lambda: loading_func(warehouse, vehicle), number=1000
            )
            times.append(time_taken)
        except:
            pass
    return sum(times) / len(times) if times else None

def write_results_to_file(filename, n, functional_results, complexity, performance_results):
    with open(filename, 'w') as file:
        file.write(f"Results for solution {n}:\n")
        file.write("Functional Test Results: " + str(functional_results) + '\n')
        file.write("Cyclomatic Complexity: " + str(complexity) + '\n')
        file.write("Performance Test Results: " + str(performance_results) + '\n')

def main():
    for n, module in enumerate([n1, n2, n3], 1):
        loading_func = module.optimize_vehicle_loading
        functional_results = test_functional(loading_func)
        complexity = calculate_complexity(loading_func)
        performance_results = test_performance(loading_func)
        write_results_to_file(f'../test_results/q9-{n}.txt', n, functional_results, complexity, performance_results)

main()