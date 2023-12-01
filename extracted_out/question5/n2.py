class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def apply_discount(self, discount):
        self.price *= (1 - discount)

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def find_book_by_title(self, title):
        return next((book for book in self.books if book.title == title), None)

def create_book(title, author, price):
    return Book(title, author, price)

def add_book_to_library(library, book):
    library.add_book(book)

def search_book_in_library(library, title):
    return library.find_book_by_title(title)

def update_book_price(book, new_price):
    book.price = new_price
    return book.price

def list_all_books(library):
    return [(book.title, book.author, book.price) for book in library.books]

# TODO: Implement the 'calculate_total_value' function
def calculate_total_value(library):
    # This function should take a Library object as input and return the total value of all books in the library.
    # Expected Input: library (Library object)
    # Expected Output: total_value (float, sum of prices of all books)
    total_value = 0
    for book in library.books:
        total_value += book.price
    return total_value