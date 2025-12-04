import sympy as sp
n, z, w = sp.symbols('n z w', real=True)
x = sp.cos(w*n)
X_z = sp.summation(x * z**(-n), (n, 0, sp.oo))
X_z_simplified = sp.simplify(X_z)
print("Z-transform of x[n] = cos(wn)u[n]:")
print("X(z) =", X_z_simplified)