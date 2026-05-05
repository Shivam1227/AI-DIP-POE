import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('image.jpg', 0)

fig, axes = plt.subplots(2, 4, figsize=(20, 10))
fig.suptitle("Morphological Algorithms", fontsize=16)

# ─────────────────────────────────────────
# 1. BOUNDARY EXTRACTION
# ─────────────────────────────────────────
_, binary1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
kernel = np.ones((3,3), np.uint8)
eroded = cv2.erode(binary1, kernel)
boundary = cv2.subtract(binary1, eroded)

axes[0,0].imshow(boundary, cmap='gray')
axes[0,0].set_title("Boundary Extraction")
axes[0,0].axis('off')

# ─────────────────────────────────────────
# 2. REGION FILLING
# ─────────────────────────────────────────
_, binary2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
h, w = binary2.shape
mask = np.zeros((h+2, w+2), np.uint8)
filled = binary2.copy()
cv2.floodFill(filled, mask, (0,0), 255)
filled_inv = cv2.bitwise_not(filled)
result = binary2 | filled_inv

axes[0,1].imshow(result, cmap='gray')
axes[0,1].set_title("Region Filling")
axes[0,1].axis('off')

# ─────────────────────────────────────────
# 3. CONNECTED COMPONENTS
# ─────────────────────────────────────────
_, binary3 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
num_labels, labels = cv2.connectedComponents(binary3)
print("Number of components:", num_labels)
label_img = np.uint8(255 * labels / np.max(labels))

axes[0,2].imshow(label_img, cmap='gray')
axes[0,2].set_title("Connected Components")
axes[0,2].axis('off')

# ─────────────────────────────────────────
# 4. CONVEX HULL
# ─────────────────────────────────────────
_, binary4 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(binary4, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
hull_img = np.zeros_like(binary4)
for cnt in contours:
    hull = cv2.convexHull(cnt)
    cv2.drawContours(hull_img, [hull], -1, 255, -1)

axes[0,3].imshow(hull_img, cmap='gray')
axes[0,3].set_title("Convex Hull")
axes[0,3].axis('off')

# ─────────────────────────────────────────
# 5. THINNING
# ─────────────────────────────────────────
_, binary5 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
skeleton = np.zeros(binary5.shape, np.uint8)
element = cv2.getStructuringElement(cv2.MORPH_CROSS, (3,3))
done = False
while not done:
    eroded = cv2.erode(binary5, element)
    temp = cv2.dilate(eroded, element)
    temp = cv2.subtract(binary5, temp)
    skeleton = cv2.bitwise_or(skeleton, temp)
    binary5 = eroded.copy()
    if cv2.countNonZero(binary5) == 0:
        done = True

axes[1,0].imshow(skeleton, cmap='gray')
axes[1,0].set_title("Thinning")
axes[1,0].axis('off')

# ─────────────────────────────────────────
# 6. THICKENING
# ─────────────────────────────────────────
_, binary6 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
kernel2 = np.ones((3,3), np.uint8)
thick = cv2.dilate(binary6, kernel2, iterations=2)

axes[1,1].imshow(thick, cmap='gray')
axes[1,1].set_title("Thickening")
axes[1,1].axis('off')

# ─────────────────────────────────────────
# 7. SKELETONS
# ─────────────────────────────────────────
_, binary7 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
skeleton2 = np.zeros(binary7.shape, np.uint8)
element2 = cv2.getStructuringElement(cv2.MORPH_CROSS, (3,3))
while True:
    eroded = cv2.erode(binary7, element2)
    temp = cv2.dilate(eroded, element2)
    temp = cv2.subtract(binary7, temp)
    skeleton2 = cv2.bitwise_or(skeleton2, temp)
    binary7 = eroded.copy()
    if cv2.countNonZero(binary7) == 0:
        break

axes[1,2].imshow(skeleton2, cmap='gray')
axes[1,2].set_title("Skeleton")
axes[1,2].axis('off')

# ─────────────────────────────────────────
# 8. PRUNING
# ─────────────────────────────────────────
_, binary8 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
kernel3 = np.ones((3,3), np.uint8)
pruned = cv2.morphologyEx(binary8, cv2.MORPH_OPEN, kernel3)

axes[1,3].imshow(pruned, cmap='gray')
axes[1,3].set_title("Pruning")
axes[1,3].axis('off')

plt.tight_layout()
plt.show()