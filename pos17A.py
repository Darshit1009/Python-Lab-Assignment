import sympy as sp

n, z = sp.symbols('n z')
x = 3**n  # x[n] = 3^n * u[n], u[n] is implied by summation from n=0

X_z = sp.summation(x * z**(-n), (n, 0, sp.oo))
X_z_simplified = sp.simplify(X_z)

print("Z-transform of x[n] = 3^n u[n]:")
print("X(z) =", X_z_simplified)