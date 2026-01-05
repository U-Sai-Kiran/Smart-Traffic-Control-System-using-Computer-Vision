import cv2
import numpy as np
import time

img = cv2.imread("images/traffic.jpg")
start = time.time()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5,5), 1.4)
edges = cv2.Canny(blur, 50, 150)

h, w = edges.shape
lane_width = w // 3

lane1 = edges[:, 0:lane_width]
lane2 = edges[:, lane_width:2*lane_width]
lane3 = edges[:, 2*lane_width:w]

densities = {
    "Lane 1": np.sum(lane1 == 255),
    "Lane 2": np.sum(lane2 == 255),
    "Lane 3": np.sum(lane3 == 255)
}

for lane, value in densities.items():
    print(f"{lane} Density:", value)

print("Processing Time:", round(time.time() - start, 3), "seconds")
