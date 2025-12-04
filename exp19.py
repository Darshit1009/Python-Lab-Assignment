import sympy as sp
n, z = sp.symbols('n z')
u = sp.Heaviside(n)
X = sp.summation(u * z**(-n), (n, 0, sp.oo))
print("Z-transform of unit step:", X)
print("Region of Convergence: |z| > 1")
print("System Stability: Unstable (ROC does not include unit circle)")