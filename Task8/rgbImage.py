import os
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

HIST_BINS = 256
HIST_ALPHA = 0.5
HIST_COLORS = ('red', 'green', 'blue')
HIST_LABELS = ('R', 'G', 'B')

def load_img(image_path):
    try:
        with (Image.open(image_path)) as img:
            return np.array(img.convert('RGB'))
    except Exception:
        return None

def rgb_hist(colors,labels,pixels):
    for i, (color, label) in enumerate(zip(colors, labels)):
        var = pixels[:, :,i].flatten()
        plt.hist(var, bins=HIST_BINS, color=color, alpha=HIST_ALPHA, label=label)

def vision():
    plt.legend()
    plt.title("RGB Histogram")
    plt.xlabel("Intensity")
    plt.ylabel("Count")
    plt.show()

if __name__ == '__main__':
    while True:
        path = input("Enter your image path")
        pixels = load_img(path)
        if pixels is not None:
            break
        print("invalid path, please try again.\n")
    plt.figure()
    rgb_hist(HIST_COLORS, HIST_LABELS, pixels)
    vision()



