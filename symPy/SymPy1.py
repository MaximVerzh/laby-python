import sympy as sp


λ, μ, ρ = sp.symbols('λ μ ρ')
matrix = sp.Matrix([
    [0, 0, 0, -1/ρ, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, -1/ρ, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, -1/ρ, 0, 0, 0],
    [-(λ + 2*μ), 0, 0, 0, 0, 0, 0, 0, 0],
    [0, -μ, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, -μ, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, -λ, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, -λ, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, -λ, 0, 0, 0]
])


eigenvalues = matrix.eigenvals()


print("Собственные значения матрицы:")
for eigenvalue, multiplicity in eigenvalues.items():
    print(f"Собственное значение: {eigenvalue}, Кратность: {multiplicity}")
