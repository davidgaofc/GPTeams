```python
import numpy as np
import scipy.optimize as opt

def find_polynomial_roots(polynomial):
    def f(x):
        return polynomial.evaluate(x)
    
    roots = opt.fsolve(f, np.roots(polynomial.coefficients))
    return [ComplexNumber(root, 0) for root in roots]
```