import cv2

img = cv2.imread("images/traffic.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5,5), 1.4)
edges = cv2.Canny(blur, 50, 150)

contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

vehicle_count = 0
for cnt in contours:
    x,y,w,h = cv2.boundingRect(cnt)
    if w > 30 and h > 30:
        vehicle_count += 1
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

print("Estimated Vehicles:", vehicle_count)

cv2.imshow("Vehicle Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
import time
start = time.time()

# processing code here

end = time.time()
print("Total Processing Time:", round(end-start,3),"seconds")
