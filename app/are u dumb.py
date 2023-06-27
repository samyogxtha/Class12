import tkinter, random
import customtkinter as ctk
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")

def close_window():
    root.destroy()
    
def yes_clicked():
    label = ctk.CTkLabel(master=root, text="I knew it. :3", font=('Berlin Sans FB',45), width=300, height=300)
    label.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    root.after(5000, close_window)

def no_clicked():
    x = random.uniform(0.38,0.9)
    y = random.uniform(0.38,0.9)
    no_button.place(relx=x, rely=y)

root = ctk.CTk()
root.geometry("300x240")
root.title("Are you Dumb?")

qn = ctk.CTkLabel(master=root, text="Are you dumb?", font=('Berlin Sans FB',30), width=300, height=150)
qn.place(relx=0.5, rely=0.25, anchor=tkinter.CENTER)

yes_button = ctk.CTkButton(root, text="Yes", width=15, border_width=0, corner_radius=8, command=yes_clicked)
yes_button.place(relx=0.25, rely=0.65)

no_button = ctk.CTkButton(root, text="No", width=15, border_width=0, corner_radius=8, command=no_clicked)
no_button.place(relx=0.65, rely=0.65)

root.mainloop()