from customtkinter import *
from PIL import Image

root = CTk()
root.title("Zero Hotel Booking")
root.minsize(height=720,width=1440)

frame = CTkFrame(root,height=720,width=1440,corner_radius=15)
frame.place(relx = 0.5,rely = 0.5, anchor=CENTER)

image_files = ['images/image0.jpg','images/image1.jpg', 'images/image2.jpg', 'images/image3.jpg','images/image4.jpg','images/image5.jpg']
images = []

def load_images():
    for file in image_files:
        image = CTkImage(Image.open(file),size=(1440,720))
        images.append(image)
    canvas.configure(image=images[0])

canvas = CTkLabel(frame, text = '', width=1440, height=720)
canvas.pack()

def next_image(index):
    canvas.configure(image=images[index])
    index += 1
    if index >= len(images):
        index = 0
    root.after(5000, next_image, index)

load_images()
next_image(0)





root.mainloop()