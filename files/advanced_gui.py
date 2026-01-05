import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def process_image(path):
    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 1.4)
    edges = cv2.Canny(blur, 50, 150)

    # Edge Overlay
    overlay = img.copy()
    overlay[edges == 255] = [0, 0, 255]

    return img, gray, blur, edges, overlay

def show(img, label):
    if len(img.shape) == 2:
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(img).resize((200,130))
    img = ImageTk.PhotoImage(img)
    label.config(image=img)
    label.image = img

def upload():
    global imgs
    path = filedialog.askopenfilename(filetypes=[("Images","*.jpg *.png *.jpeg")])
    if path:
        imgs = process_image(path)
        show(imgs[0], lbl_original)
        show(imgs[1], lbl_gray)
        show(imgs[2], lbl_blur)
        show(imgs[3], lbl_edges)
        show(imgs[4], lbl_overlay)

# ---------- GUI ----------
root = tk.Tk()
root.title("Advanced Smart Traffic Vision")
root.geometry("1100x420")

tk.Button(root, text="Upload Traffic Image", command=upload, font=("Arial",12)).pack(pady=10)

frame = tk.Frame(root)
frame.pack()

labels = ["Original", "Grayscale", "Gaussian Blur", "Canny Edges", "Edge Overlay"]
widgets = []

for i, text in enumerate(labels):
    f = tk.Frame(frame)
    f.grid(row=0, column=i, padx=5)
    tk.Label(f, text=text).pack()
    lbl = tk.Label(f, width=200, height=130, bg="gray")
    lbl.pack()
    widgets.append(lbl)

lbl_original, lbl_gray, lbl_blur, lbl_edges, lbl_overlay = widgets

root.mainloop()
