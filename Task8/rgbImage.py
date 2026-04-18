import os
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

path = input("enter the path of your file: ").strip()
if not os.path.isfile(path):
    print("File not found")
    exit()
try:
    img = Image.open(path)
    img.verify()
except Exception:
    print("The file is not a valid image")
    exit()
pixels = np.array(img)
r = pixels[:, :, 0].flatten()
g = pixels[:, :, 1].flatten()
b = pixels[:, :, 2].flatten()
plt.hist(r, bins=256, color='red', alpha=0.5, label='R')
plt.hist(g, bins=256, color='green', alpha=0.5, label='G')
plt.hist(b, bins=256, color='blue', alpha=0.5, label='B')
plt.legend()
plt.title("RGB Histogram")
plt.xlabel("Intensity")
plt.ylabel("Count")
plt.show()



