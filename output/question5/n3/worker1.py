```python
def calculate_total_value(library):
    total_value = 0
    for book in library.books:
        total_value += book.price
    return total_value
```
or using a list comprehension:
```python
def calculate_total_value(library):
    return sum([book.price for book in library.books])
```