import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


file_path = r'C:\Users\Вержбицкая Полина\Desktop\data1.txt' #мамин комп :(
with open(file_path, 'r') as f:
    lines = f.readlines()
frames = []
for i in range(0, len(lines), 2):
    x = list(map(float, lines[i].strip().split()))
    y = list(map(float, lines[i + 1].strip().split()))
    frames.append((x, y))
xs = [x for frame in frames for x in frame[0]]
ys = [y for frame in frames for y in frame[1]]
xmin, xmax = min(xs), max(xs)
ymin, ymax = min(ys), max(ys)

fig, ax = plt.subplots()
ax.set_xlim(xmin, xmax)
ax.set_ylim(ymin, ymax)
ax.grid(True, which='both', linestyle='--', linewidth=0.5)
line, = ax.plot([], [], lw=2)

def update(frame_number):
    x, y = frames[frame_number]
    line.set_data(x, y)
    ax.set_title(f'Frame {frame_number + 1}')
    return line,

animation = FuncAnimation(fig, update, frames=len(frames), blit=True)

gif_path = r'C:\Users\Вержбицкая Полина\Desktop\animated_process.gif'
animation.save(gif_path, writer='pillow', fps=5)

gif_path
