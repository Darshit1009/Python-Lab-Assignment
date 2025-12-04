import numpy as np
import matplotlib.pyplot as plt

image = plt.imread("MU.jpg")

topPad = 50
bottomPad = 50
leftPad = 100
rightPad = 100

height, width, channels = image.shape
newHeight = height + topPad + bottomPad
newWidth = width + leftPad + rightPad

paddedImage = np.zeros((newHeight, newWidth, channels), dtype=image.dtype)
paddedImage[topPad:topPad+height, leftPad:leftPad+width, :] = image

plt.imshow(paddedImage)
plt.title("Image with Black Padding")
plt.axis("off")
plt.show()
