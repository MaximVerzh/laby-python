import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from matplotlib.animation import FuncAnimation

data = np.loadtxt('data3lab3.txt')

data_length = len(data)
A = np.zeros((data_length, data_length))
np.fill_diagonal(A, 1)
A[np.arange(data_length), (np.arange(data_length) - 1) % data_length] = -1

fig = plt.figure()
ax = plt.axes(xlim=(0, data_length), ylim=(-2, 10))
line, = ax.plot([], [], lw=3)


def init():
    line.set_data([], [])
    return line,


data_values = [data.copy()]


def animate(i):
    if i > 0:
        new_vector = np.dot(A, data_values[-1])
        next_data = data_values[-1] - 0.5 * new_vector
        data_values.append(next_data)
    else:
        next_data = data_values[0]

    x = np.linspace(0, data_length, data_length)
    y = next_data
    line.set_data(x, y)
    return line,


animation = FuncAnimation(fig, animate, init_func=init,
                     frames=255, interval=20, blit=True)


animation.save('animation.gif', writer='Pillow')
