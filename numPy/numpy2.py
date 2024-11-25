import numpy as np
import matplotlib.pyplot as plt

file_paths = [
    "signal01.dat",
    "signal02.dat",
    "signal03.dat",
]
def smooth_signal(signal, window=10):
    cumsum = np.cumsum(signal, dtype=float) # Cumulative sum :))
    cumsum[window:] = cumsum[window:] - cumsum[:-window]
    return cumsum / np.minimum(np.arange(1, len(signal) + 1), window)


fig, axs = plt.subplots(len(file_paths), 1, figsize=(10, 15))
for i, file_path in enumerate(file_paths):
    data = np.loadtxt(file_path)
    smoothed = smooth_signal(data)
    axs[i].plot(data, label="До обработки", alpha=0.5)
    axs[i].plot(smoothed, label="После обработки", color='red', linewidth=1.5)
    axs[i].set_title(f"Сигнал {i + 1}")
    axs[i].legend()
    axs[i].grid(True)

plt.tight_layout()
plt.show()
