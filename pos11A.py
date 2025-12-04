import numpy as np
import matplotlib.pyplot as plt

image = plt.imread("MU.jpg")

dimensions = image.size
shape = image.shape
minBlue = np.min(image[:, :, 2])

print("Dimensions:", dimensions)
print("Shape:", shape)
print("Min Pixel Value at Channel B:", minBlue)

plt.imshow(image)
plt.title("Sample Image")
plt.axis("off")
plt.show()