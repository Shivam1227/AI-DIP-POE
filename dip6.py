import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load image
img = cv2.imread('image.jpg', 0)

# ------------------- SPATIAL DOMAIN -------------------

# Mean Filter (Smoothing)
mean = cv2.blur(img, (5,5))

# Gaussian Filter (Smoothing + noise reduction)
gaussian = cv2.GaussianBlur(img, (5,5), 0)

# Median Filter (Noise removal)
median = cv2.medianBlur(img, 5)

# Sharpening (using kernel)
kernel_sharpen = np.array([[0, -1, 0],
                           [-1, 5, -1],
                           [0, -1, 0]])

sharpen = cv2.filter2D(img, -1, kernel_sharpen)

# ------------------- FREQUENCY DOMAIN -------------------

# DFT
dft = np.fft.fft2(img)
dft_shift = np.fft.fftshift(dft)

rows, cols = img.shape
crow, ccol = rows//2 , cols//2

# Low Pass Filter
mask_lpf = np.zeros((rows, cols), np.uint8)
mask_lpf[crow-30:crow+30, ccol-30:ccol+30] = 1
lpf = dft_shift * mask_lpf

# High Pass Filter
mask_hpf = 1 - mask_lpf
hpf = dft_shift * mask_hpf

# Inverse DFT
img_lpf = np.fft.ifft2(np.fft.ifftshift(lpf))
img_lpf = np.abs(img_lpf)

img_hpf = np.fft.ifft2(np.fft.ifftshift(hpf))
img_hpf = np.abs(img_hpf)

# ------------------- DISPLAY -------------------

plt.figure(figsize=(12,8))

titles = ['Original','Gaussian','Median','Sharpen','Low Pass','High Pass']
images = [img, gaussian, median, sharpen, img_lpf, img_hpf]

for i in range(6):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.axis('off')

plt.show()