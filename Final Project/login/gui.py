
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Samyog\OneDrive\Documents\Class12\Final Project\login\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1280x720")
window.configure(bg = "#093545")


canvas = Canvas(
    window,
    bg = "#093545",
    height = 720,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    640.0,
    664.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    640.0,
    664.0,
    image=image_image_2
)

canvas.create_text(
    507.0,
    474.0,
    anchor="nw",
    text="Don’t have an account?",
    fill="#FFFFFF",
    font=("Montserrat Medium", 14 * -1)
)

canvas.create_text(
    681.0,
    474.0,
    anchor="nw",
    text="Signup Here",
    fill="#20DF7F",
    font=("Montserrat Medium", 14 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=490.0,
    y=518.0,
    width=300.0,
    height=45.0
)

canvas.create_text(
    618.0,
    531.0,
    anchor="nw",
    text="Login",
    fill="#FFFFFF",
    font=("LexendDeca Regular", 16 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    640.0,
    431.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#224957",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=500.0,
    y=409.0,
    width=280.0,
    height=43.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    640.0,
    354.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#224957",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=500.0,
    y=332.0,
    width=280.0,
    height=43.0
)

canvas.create_text(
    537.0,
    204.0,
    anchor="nw",
    text="Don’t have an account? Signup HereDon’t have an account? Signup Here",
    fill="#FFFFFF",
    font=("LexendDeca Regular", 64 * -1)
)

canvas.create_text(
    555.0,
    126.0,
    anchor="nw",
    text="00:00",
    fill="#FFFFFF",
    font=("LexendDeca Regular", 64 * -1)
)
window.resizable(False, False)
window.mainloop()
