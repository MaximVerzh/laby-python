import numpy as np
from PIL import Image
import math
import matplotlib.pyplot as plt
from matplotlib.animation import PillowWriter
import os
from matplotlib.animation import FuncAnimation

def enhance_contrast(file_path, new_file_path):

    image = Image.open(file_path).convert('L')
    data = np.array(image)

    dif = math.ceil(255 / (np.amax(data) - np.amin(data)))
    min_pix = np.amin(data)
    data = 255 - (data - min_pix) * dif

    res_img = Image.fromarray(data)
    res_img.save(new_file_path)

enhance_contrast('lunar01_raw.jpg', 'lunar011_raw.jpg')
enhance_contrast('lunar02_raw.jpg', 'lunar022_raw.jpg')
enhance_contrast('lunar03_raw.jpg', 'lunar033_raw.jpg')