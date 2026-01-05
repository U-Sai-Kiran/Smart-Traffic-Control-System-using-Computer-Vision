import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

REFERENCE_IMAGE = "images/reference.jpg"

def canny_white_pixels(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 1.4)
    edges = cv2.Canny(blur, 50, 150)
    return np.sum(edges == 255), edges

def upload_image():
    global sample_path
    sample_path = filedialog.askopenfilename(
        filetypes=[("Image Files","*.jpg *.png *.jpeg")]
    )
    if sample_path:
        messagebox.showinfo("Success", "Sample Image Loaded")

def detect_and_compare():
    if not sample_path:
        messagebox.showerror("Error", "Upload image first")
        return

    sample_white, sample_edges = canny_white_pixels(sample_path)
    ref_white, ref_edges = canny_white_pixels(REFERENCE_IMAGE)

    if sample_white > ref_white:
        traffic = "HIGH"
        time = 60
    elif sample_white > ref_white * 0.6:
        traffic = "MEDIUM"
        time = 45
    else:
        traffic = "LOW"
        time = 30

    cv2.imwrite("output/sample_edges.jpg", sample_edges)
    cv2.imwrite("output/reference_edges.jpg", ref_edges)

    messagebox.showinfo(
        "Traffic Result",
        f"Sample White Pixels: {sample_white}\n"
        f"Reference White Pixels: {ref_white}\n\n"
        f"Traffic Density: {traffic}\n"
        f"Green Signal Time: {time} seconds"
    )

# ---------------- GUI ----------------
root = tk.Tk()
root.title("Density Based Smart Traffic Control")
root.geometry("400x300")

sample_path = None

tk.Label(root, text="Smart Traffic Control System", font=("Arial",14,"bold")).pack(pady=10)

tk.Button(root, text="Upload Traffic Image", width=25, command=upload_image).pack(pady=10)
tk.Button(root, text="Detect & Compare", width=25, command=detect_and_compare).pack(pady=10)

tk.Label(root, text="Using Canny Edge Detection", font=("Arial",10)).pack(pady=20)

root.mainloop()
