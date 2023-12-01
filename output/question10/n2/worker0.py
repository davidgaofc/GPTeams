```python
def find_polynomial_roots(polynomial):
    roots = []
    n = len(polynomial.coefficients) - 1

    # Iterate through all possible complex numbers to find the roots
    for i in range(n):
        x = ComplexNumber(0, 0)
        while True:
            # Use the Durand-Kerner method to approximate the roots
            f = polynomial.evaluate(x)
            if abs(f) < 0.0001:
                roots.append(x)
                break
            
            # Update x using the formula
            x = x - polynomial.evaluate(x) / polynomial.derivative().evaluate(x)
    
    return roots
```