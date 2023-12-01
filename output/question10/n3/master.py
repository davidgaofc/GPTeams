import numpy as np

class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def add(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def multiply(self, other):
        real = self.real * other.real - self.imaginary * other.imaginary
        imaginary = self.real * other.imaginary + self.imaginary * other.real
        return ComplexNumber(real, imaginary)

    def modulus(self):
        return (self.real**2 + self.imaginary**2)**0.5

    def conjugate(self):
        return ComplexNumber(self.real, -self.imaginary)

    def __str__(self):
        return f"{self.real} + {self.imaginary}i"

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

def find_polynomial_roots(polynomial):
    # Convert the coefficients of the polynomial into a numpy array
    p = np.array(polynomial.coefficients)

    # Use numpy's roots function to find the roots
    roots = np.roots(p)

    # Convert the roots into ComplexNumber objects
    root_objects = [ComplexNumber(root.real, root.imag) for root in roots]

    return root_objects