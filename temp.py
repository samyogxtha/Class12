from tkinter import *

from PIL import Image, ImageTk

root = Tk()
root.title("Title")
root.geometry("600x600")
root.configure(background="black")



def resize_image(event):

    new_width = event.width
    new_height = event.height
    print(new_height,new_width)

    image = img_copy.resize((new_width, new_height))

    background_image = ImageTk.PhotoImage(image)
    background.configure(image =  background_image)
    
image = Image.open("assets/loginbg.png")
img_copy= image.copy()


background_image = ImageTk.PhotoImage(image)

background = Label(root, image=background_image)
background.pack(fill=BOTH, expand=YES)
background.bind('<Configure>', resize_image)



root.mainloop()