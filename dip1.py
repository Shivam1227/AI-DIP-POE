import cv2
import numpy as np
import pywt
from matplotlib import pyplot as plt

# Load image (grayscale)
img = cv2.imread('image.jpg', 0)

# ------------------- DFT -------------------
dft = np.fft.fft2(img)
dft_shift = np.fft.fftshift(dft)
magnitude_spectrum = 20 * np.log(np.abs(dft_shift))

# ------------------- DCT -------------------
img_float = np.float32(img) / 255.0
dct = cv2.dct(img_float)

# ------------------- DWT -------------------
coeffs2 = pywt.dwt2(img, 'haar')
LL, (LH, HL, HH) = coeffs2

# ------------------- Display -------------------
plt.figure(figsize=(10,8))

plt.subplot(2,3,1), plt.imshow(img, cmap='gray')
plt.title('Original Image')

plt.subplot(2,3,2), plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('DFT Magnitude')

plt.subplot(2,3,3), plt.imshow(dct, cmap='gray')
plt.title('DCT')

plt.subplot(2,3,4), plt.imshow(LL, cmap='gray')
plt.title('LL')

plt.subplot(2,3,5), plt.imshow(LH, cmap='gray')
plt.title('LH')

plt.subplot(2,3,6), plt.imshow(HH, cmap='gray')
plt.title('HH')

plt.show()