import streamlit as st
import cv2
import numpy as np
import time

st.title("🚦 Smart Traffic Control System")

uploaded = st.file_uploader("Upload Traffic Image", type=["jpg","png","jpeg"])

if uploaded:
    file_bytes = np.asarray(bytearray(uploaded.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, 1)

    start = time.time()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 1.4)
    edges = cv2.Canny(blur, 50, 150)

    white_pixels = np.sum(edges == 255)

    st.image(img, caption="Original Image", channels="BGR")
    st.image(edges, caption="Canny Edges")

    if white_pixels < 10000:
        signal = 30
        level = "LOW"
    elif white_pixels < 25000:
        signal = 45
        level = "MEDIUM"
    else:
        signal = 60
        level = "HIGH"

    st.success(f"Traffic Density: {level}")
    st.info(f"Green Signal Time: {signal} seconds")
    st.write("Processing Time:", round(time.time()-start,3), "seconds")
