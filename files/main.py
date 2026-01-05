import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load image
img = cv2.imread("images/traffic.jpg")

if img is None:
    print("❌ Image not found!")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Gaussian Blur
blur = cv2.GaussianBlur(gray, (5, 5), 1.4)

# Canny Edge Detection
edges = cv2.Canny(blur, 50, 150)

# Save output
cv2.imwrite("output/edges.jpg", edges)

# WHITE PIXEL COUNT
white_pixels = np.sum(edges == 255)
print("White Pixel Count:", white_pixels)

# Signal Time Logic
if white_pixels < 10000:
    signal_time = 30
    traffic = "LOW"
elif white_pixels < 25000:
    signal_time = 45
    traffic = "MEDIUM"
else:
    signal_time = 60
    traffic = "HIGH"

print("Traffic Density:", traffic)
print("Green Signal Time:", signal_time, "seconds")

# Display
plt.figure(figsize=(10,4))

plt.subplot(1,2,1)
plt.title("Original Image")
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis("off")

plt.subplot(1,2,2)
plt.title("Canny Edges")
plt.imshow(edges, cmap="gray")
plt.axis("off")

plt.show()
