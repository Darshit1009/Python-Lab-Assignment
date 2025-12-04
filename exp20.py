import sympy as sp

z = sp.symbols('z')
Hz = 0.5 * (z - 0.7) * (z - 0.9) / ((z - 0.6) * (z - 0.4))
den = sp.denom(Hz)
poles = sp.solve(den, z)
stable = all(abs(complex(p)) < 1 for p in poles)
roc_radius = max(abs(complex(p)) for p in poles)

print("H(z) =", Hz)
print("Poles:", poles)
print("Region of Convergence: |z| >", roc_radius)
print("System Stability:", "Stable" if stable else "Unstable")