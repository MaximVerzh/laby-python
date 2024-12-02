import numpy as np
import matplotlib.pyplot as plt


from scipy.linalg import solve


with open('SymPy2.txt', 'r') as f:
    lines = f.readlines()


N = int(lines[0].strip())
A = np.array([list(map(float, lines[i + 1].split())) for i in range(N)])

b = np.array(list(map(float, lines[N + 1].split())))


x = solve(A, b)

plt.bar(range(len(x)), x, color='blue')
plt.xlabel('Индекс x')
plt.ylabel('Значение x')
plt.title('Решение ситсемы Ax = b')
plt.show()
