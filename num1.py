import matplotlib.pyplot as plt

file_path = r'C:\Users\Вержбицкая Полина\Downloads\002.dat'
with open(file_path, 'r') as file:
    n = int(file.readline().strip())
    points = [list(map(float, file.readline().split())) for i in range(n)]

x = [point[0] for point in points]
y = [point[1] for point in points]

plt.figure(figsize=(15, 10))
plt.scatter(x, y, color='blue', s=20, label="Точки")
plt.gca().set_aspect('equal', adjustable='box')
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Визуализация")
plt.legend()
plt.show()

