import numpy as np
import matplotlib.pyplot as plt

image = plt.imread("MU.jpg")
redChannel = np.zeros_like(image)
greenChannel = np.zeros_like(image)
blueChannel = np.zeros_like(image)
redChannel[:, :, 0] = image[:, :, 0]
greenChannel[:, :, 1] = image[:, :, 1]
blueChannel[:, :, 2] = image[:, :, 2]
plt.figure(figsize=(10, 8))
plt.subplot(2, 2, 1)
plt.imshow(image)
plt.title("Original Image")
plt.axis("off")
plt.subplot(2, 2, 2)
plt.imshow(redChannel)
plt.title("Red Channel")
plt.axis("off")
plt.subplot(2, 2, 3)
plt.imshow(greenChannel)
plt.title("Green Channel")
plt.axis("off")
plt.subplot(2, 2, 4)
plt.imshow(blueChannel)
plt.title("Blue Channel")
plt.axis("off")
plt.tight_layout()
plt.show()