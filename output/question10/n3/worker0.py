```python
import numpy as np

def find_polynomial_roots(polynomial):
    # Get the coefficients of the polynomial
    coefficients = polynomial.coefficients

    # Find the roots using numpy's roots function
    roots = np.roots(coefficients)

    # Convert the roots to ComplexNumber objects
    complex_roots = [ComplexNumber(root.real, root.imag) for root in roots]

    return complex_roots
```
Note: This solution assumes that the Polynomial class has a `coefficients` attribute that contains a list of the polynomial's coefficients in ascending order.