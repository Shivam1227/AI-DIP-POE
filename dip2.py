import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load image
img = cv2.imread('image.jpg', 0)

# ------------------- Sobel -------------------
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
sobel = cv2.magnitude(sobelx, sobely)

# ------------------- Prewitt -------------------
kernelx = np.array([[1,0,-1],[1,0,-1],[1,0,-1]])
kernely = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])

prewittx = cv2.filter2D(img, -1, kernelx)
prewitty = cv2.filter2D(img, -1, kernely)
prewitt = prewittx + prewitty

# ------------------- Canny -------------------
canny = cv2.Canny(img, 100, 200)

# ------------------- Display -------------------
plt.figure(figsize=(10,8))

plt.subplot(2,2,1), plt.imshow(img, cmap='gray')
plt.title('Original Image')

plt.subplot(2,2,2), plt.imshow(sobel, cmap='gray')
plt.title('Sobel')

plt.subplot(2,2,3), plt.imshow(prewitt, cmap='gray')
plt.title('Prewitt')

plt.subplot(2,2,4), plt.imshow(canny, cmap='gray')
plt.title('Canny')

plt.show()