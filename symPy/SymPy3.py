import sympy as sp
from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt

x = sp.symbols('x')
y = sp.Function('y')

dif = sp.Eq(y(x).diff(x), -2 * y(x))

sympy_solution = sp.dsolve(dif, y(x), ics={y(0): sp.sqrt(2)})


sympy_func = sp.lambdify(x, sympy_solution.rhs, 'numpy')


def dif_func(t, y):
    return -2 * y

sci_solution = solve_ivp(dif_func, [0, 10], [np.sqrt(2)], t_eval=np.linspace(0, 10, 500))


x_vals = sci_solution.t
sci_vals = sci_solution.y[0]
sympy_vals = sympy_func(x_vals)


plt.figure(figsize=(10, 6))


plt.subplot(2, 1, 1)
plt.plot(x_vals, sympy_vals, label="SymPy ", color="black")
plt.plot(x_vals, sci_vals, label="SciPy ", linestyle="dashed", color="orange")
plt.xlabel("x")
plt.ylabel("y(x)")
plt.title("Решение дифура")
plt.legend()
plt.grid()
plt.subplot(2, 1, 2)
plt.plot(x_vals, np.abs(sympy_vals - sci_vals), label="Разность (SymPy - SciPy)", color="red")
plt.xlabel("x")
plt.ylabel("Разность")
plt.title("Разность решений")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()
print("Решение SymPy:")
sp.pprint(sympy_solution)
