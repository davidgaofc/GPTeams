```python
def calculate_total_value(library):
    total_value = sum(book.price for book in library.books)
    return total_value
```