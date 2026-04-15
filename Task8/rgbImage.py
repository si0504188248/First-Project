import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

img = Image.open("image.jpg")
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



