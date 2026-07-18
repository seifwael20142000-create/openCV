import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("tree.jpg")

H = img.shape[0]
W = img.shape[1]

print(img.shape)
print(img.dtype)
print(img.size)

print(img[H//2, W//2])

print(img[H//2, W//2, 0])
print(img[H//2, W//2, 1])
print(img[H//2, W//2, 2])

y, x = np.ogrid[:H, :W]
r = min(H, W) // 10
mask = (x - W//2)**2 + (y - H//2)**2 <= r**2

img[mask] = [255, 255, 255]

b = img[:, :, 0]
g = img[:, :, 1]
r = img[:, :, 2]

plt.subplot(1,3,1)
plt.imshow(b, cmap="gray")

plt.subplot(1,3,2)
plt.imshow(g, cmap="gray")

plt.subplot(1,3,3)
plt.imshow(r, cmap="gray")

plt.savefig("channels1.png")
plt.show()

f = img.astype(np.float32) / 255

print(f[H//2, W//2])

img2 = (f * 255).astype(np.uint8)

print(img2[H//2, W//2])

cv2.imwrite("output1.jpg", img)
