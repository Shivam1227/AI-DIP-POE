import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load original image (color)
img_color = cv2.imread('image.jpg')

# Convert to grayscale
img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

# Convert to binary
_, img_bin = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)

# Structuring element
kernel = np.ones((5,5), np.uint8)

# Morphological operations
erosion = cv2.erode(img_bin, kernel, iterations=1)
dilation = cv2.dilate(img_bin, kernel, iterations=1)
opening = cv2.morphologyEx(img_bin, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(img_bin, cv2.MORPH_CLOSE, kernel)

# Display
plt.figure(figsize=(10,8))

titles = ['Original', 'Grayscale', 'Erosion', 'Dilation', 'Opening', 'Closing']
images = [img_color, img_gray, erosion, dilation, opening, closing]

for i in range(6):
    plt.subplot(2,3,i+1)
    if i == 0:
        plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))
    else:
        plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.axis('off')

plt.show()