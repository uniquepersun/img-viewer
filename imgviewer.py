import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def open_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        img = Image.open(file_path)
        img = img.resize((400, 300)) 
        img = ImageTk.PhotoImage(img)
        image_label.config(image=img)
        image_label.image = img

def rotate_image(degrees):
    global image, img
    image = Image.rotate(degrees)
    img = ImageTk.PhotoImage(image)
    image_label.config(image=img)
    image_label.image = img

root = tk.Tk()
root.title("Image Viewer")

image_label = tk.Label(root)
image_label.pack()

open_button = tk.Button(root, text="Open Image", command=open_image)
open_button.pack()

rotate_left_button = tk.Button(root, text="Rotate Left", command=lambda: rotate_image(-90))
rotate_left_button.pack()

rotate_right_button = tk.Button(root, text="Rotate Right", command=lambda: rotate_image(90))
rotate_right_button.pack()

root.mainloop()
