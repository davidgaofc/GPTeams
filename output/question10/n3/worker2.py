```python
import numpy as np

def create_complex_number(real, imaginary):
    return ComplexNumber(real, imaginary)

class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients  # coefficients are stored from the lowest degree to the highest

    def evaluate(self, x):
        return sum(coef * (x**i) for i, coef in enumerate(self.coefficients))

    def derivative(self):
        derived_coeffs = [i * coef for i, coef in enumerate(self.coefficients)][1:]
        return Polynomial(derived_coeffs)

    def __str__(self):
        return " + ".join(f"{coef}x^{i}" for i, coef in enumerate(self.coefficients) if coef)

def create_polynomial(coefficients):
    return Polynomial(coefficients)

def find_polynomial_roots(polynomial):
    # Convert the coefficients of the polynomial into a numpy array
    p = np.array(polynomial.coefficients)

    # Use numpy's roots function to find the roots
    roots = np.roots(p)

    # Convert the roots into ComplexNumber objects
    root_objects = [create_complex_number(root.real, root.imag) for root in roots]

    return root_objects
```

This implementation uses the `numpy` library's `roots` function to find the roots of the polynomial. The roots are then converted into `ComplexNumber` objects using the `create_complex_number` function. The roots are returned as a list of `ComplexNumber` objects.