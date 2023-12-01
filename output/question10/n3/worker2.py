```python 
from sympy import symbols, Eq, solve

def create_complex_number(real, imaginary):
    # creating ComplexNumber object
    return ComplexNumber(real, imaginary)

class Polynomial:
    def __init__(self, coefficients):
        # coefficients are stored from the lowest degree to the highest
        self.coefficients = coefficients  

    def evaluate(self, x):
        # evaluating the polynomial for given x
        return sum(coef * (x**i) for i, coef in enumerate(self.coefficients))

    def derivative(self):
        # calculating derivative of the polynomial
        derived_coeffs = [i * coef for i, coef in enumerate(self.coefficients)][1:]
        return Polynomial(derived_coeffs)

    def __str__(self):
        # creating a string representation of the polynomial
        return " + ".join(f"{coef}x^{i}" for i, coef in enumerate(self.coefficients) if coef)

def create_polynomial(coefficients):
    # creating Polynomial object
    return Polynomial(coefficients)

def find_polynomial_roots(polynomial):
    # finding the roots of a polynomial using sympy
    x = symbols('x')
    equation = Eq(polynomial.evaluate(x), 0)
    solutions = solve(equation, x)

    # converting solutions to ComplexNumber objects
    roots = [create_complex_number(float(sol.evalf()), 0) for sol in solutions]
    return roots
```