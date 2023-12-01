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

# TODO: Implement 'find_polynomial_roots'
def find_polynomial_roots(polynomial):
    # This function should take a Polynomial object and find all its roots (real and complex).
    # Implement an algorithm for finding roots of a polynomial, like the Durand-Kerner method or other numerical methods.
    # Expected Input: polynomial (Polynomial object)
    # Expected Output: roots (list of ComplexNumber objects, representing the roots of the polynomial)
    pass