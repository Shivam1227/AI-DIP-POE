import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load binary image
img = cv2.imread('image.jpg', 0)

# Convert to binary
_, img_bin = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# Define structuring elements
B1 = np.array([[0,1,0],
               [1,1,1],
               [0,1,0]], dtype=np.uint8)

B2 = np.array([[1,0,1],
               [0,0,0],
               [1,0,1]], dtype=np.uint8)

# Convert 0/1 for processing
img_bin = img_bin // 255

# Erosion with B1
erode1 = cv2.erode(img_bin, B1)

# Complement image
img_comp = 1 - img_bin

# Erosion with B2
erode2 = cv2.erode(img_comp, B2)

# Hit-or-Miss result
hitmiss = cv2.bitwise_and(erode1, erode2)

# Display
plt.figure(figsize=(8,6))

plt.subplot(1,2,1), plt.imshow(img_bin, cmap='gray')
plt.title('Binary Image')

plt.subplot(1,2,2), plt.imshow(hitmiss, cmap='gray')
plt.title('Hit-or-Miss Result')

plt.show()