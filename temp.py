from tkinter import Tk, Canvas
from customtkinter import *
from PIL import Image, ImageTk

image_files = ['images/image0.jpg', 'images/image1.jpg', 'images/image2.jpg', 'images/image3.jpg', 'images/image4.jpg', 'images/image5.jpg']
images = []

def load_images():
    for file in image_files:
        image = ImageTk.PhotoImage(Image.open(file).resize((1440, 720)))
        images.append(image)

def next_image(index):
    canvas.itemconfig(image_item, image=images[index])
    index += 1
    if index >= len(images):
        index = 0
    root.after(1000, next_image, index)

root = CTk()
canvas = CTkCanvas(root, width=1440, height=720)
canvas.pack()

load_images()

image_item = canvas.create_image(0, 0, anchor='nw', image=images[0])
next_image(0)  # Start with the second image (index 1)

root.mainloop()
