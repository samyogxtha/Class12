# Import the required libraries
from customtkinter import *
from PIL import ImageTk, Image

# Create an instance of Tkinter Frame
win = CTk()

# Set the geometry of Tkinter Frame
win.geometry("700x450")

# Open the Image File
'''bg = ImageTk.PhotoImage(file="0assets/mgr.jpg")

# Create a Canvas
canvas = CTkCanvas(win, width=700, height=3500)
canvas.pack(fill=BOTH, expand=True)

# Add Image inside the Canvas
canvas.create_image(0, 0, image=bg, anchor='nw')

# Function to resize the window
def resize_image(e):
   global image, resized, image2
   # open image to resize it
   image = Image.open("0assets/mgr.jpg")
   # resize the image with width and height of root
   resized = image.resize((e.width, e.height), Image.ANTIALIAS)

   image2 = ImageTk.PhotoImage(resized)
   canvas.create_image(0, 0, image=image2, anchor='nw')

# Bind the function to configure the parent window
win.bind("<Configure>", resize_image)'''

CTkLabel(win,text='Bind the function to configure the parent window Bind the function to configure the parent window').place(x=0,y=0)

win.mainloop()