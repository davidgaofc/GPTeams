```python
import numpy as np

def find_polynomial_roots(polynomial):
    # Convert the polynomial coefficients to a numpy array
    coeffs = np.array(polynomial.coefficients[::-1])  # Reverse the order of the coefficients

    # Use numpy's polyroots function to find the roots
    roots = np.roots(coeffs)

    # Convert the roots to ComplexNumber objects
    root_objects = [ComplexNumber(root.real, root.imag) for root in roots]

    return root_objects
```

The `find_polynomial_roots` function uses the numpy library's `roots` function to find the roots of the polynomial. The input polynomial's coefficients are converted to a numpy array, and the `roots` function is applied to find the roots. The resulting roots are then converted to `ComplexNumber` objects and returned as a list.