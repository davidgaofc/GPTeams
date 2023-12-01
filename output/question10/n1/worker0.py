```python
from sympy import symbols, Eq, solve

def find_polynomial_roots(polynomial):
    # Convert the polynomial coefficients into symbolic expression
    x = symbols('x')
    polynomial_expr = sum(coeff * (x**i) for i, coeff in enumerate(polynomial.coefficients))

    # Solve the equation for x to find the roots
    roots = solve(Eq(polynomial_expr, 0), x)
    # Convert the roots into ComplexNumber objects
    complex_roots = [ComplexNumber(float(root.real), float(root.imag)) for root in roots]

    return complex_roots
```

The `find_polynomial_roots` function uses the sympy library to solve the polynomial equation for `x` and find the roots. It converts the roots into `ComplexNumber` objects and returns a list of these objects representing the roots of the polynomial.