import timeit
from radon.complexity import cc_visit
import inspect
import extracted_out.question5.n1 as n1
import extracted_out.question5.n2 as n2
import extracted_out.question5.n3 as n3
# Assuming the Book and Library classes are defined as provided earlier

def calculate_total_value(library):
    total_value = sum(book.price for book in library.books)
    return total_value

# Test cases for calculate_total_value
test_cases = [
    ([], 0),  # Test Case 1: Empty library
    ([n1.Book("Book1", "Author1", 10)], 10),  # Test Case 2: Single book
    ([n1.Book("Book1", "Author1", 10), n1.Book("Book2", "Author2", 20)], 30),  # Test Case 3: Two books
    ([n1.Book("Book1", "Author1", 15)], 15),  # Test Case 4: Single book with different price
    ([n1.Book("Book1", "Author1", 25), n1.Book("Book2", "Author2", 35)], 60),  # Test Case 5: Two books with different prices
    ([n1.Book("Book1", "Author1", 0), n1.Book("Book2", "Author2", 0)], 0),  # Test Case 6: Two books with zero price
    ([n1.Book("Book1", "Author1", -10), n1.Book("Book2", "Author2", 20)], 10),  # Test Case 7: Negative price book
    ([n1.Book("Book1", "Author1", 100) for _ in range(10)], 1000),  # Test Case 8: Multiple copies of a book
    ([n1.Book(f"Book{i}", f"Author{i}", i) for i in range(10)], sum(range(10))),  # Test Case 9: Sequentially priced books
    ([n1.Book("Book1", "Author1", 100), n1.Book("Book2", "Author2", 200), n1.Book("Book3", "Author3", 300)], 600) # Test Case 10: Three books with high prices
]

# Functional testing
def test_functional(calculate_func):
    correct_count = 0
    for book_info, expected in test_cases:
        library = n1.Library()
        for book in book_info:
            library.add_book(book)
        result = calculate_func(library)
        if result == expected:
            correct_count += 1
    return correct_count

# Cyclomatic complexity calculation
def calculate_complexity(func):
    source_code = inspect.getsource(func)
    complexity_result = cc_visit(source_code)
    for item in complexity_result:
        if item.name == func.__name__:
            return item.complexity
    return None

# Performance testing
def test_performance(calculate_func):
    times = []
    for book_info, _ in test_cases:
        library = n1.Library()
        for book in book_info:
            library.add_book(book)
        time_taken = timeit.timeit(lambda: calculate_func(library), number=1000)
        times.append(time_taken)
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
        calc_func = module.calculate_total_value
        functional_results = test_functional(calc_func)
        complexity = calculate_complexity(calc_func)
        performance_results = test_performance(calc_func)
        write_results_to_file(f'../test_results/q5-{n}.txt', n, functional_results, complexity, performance_results)


main()