import tkinter as tk
import customtkinter as ctk
from time import sleep

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")

root = ctk.CTk()
root.geometry("300x260")
root.title("Number Gusser")

def guess():
    global loading_window
    loading_window = ctk.CTkToplevel()
    loading_window.title("Guessing")

    loading_window.geometry("200x100")
    loading_window.resizable(False, False)
    loading_window.attributes("-topmost", True)

    label = ctk.CTkLabel(loading_window, text="Guessing...", font=('Dubai',14))
    label.pack(padx=20, pady=20)

    progress = ctk.CTkProgressBar(loading_window, mode="indeterminate")
    progress.pack(padx=20, pady=10)
    progress.start() 

    loading_window.after(200)
    label.configure(text= "Reading Your Mind...", font=('Dubai',14))
    loading_window.after(400)
    label.configure(text= "Getting there...", font=('Dubai',14))
    loading_window.after(300)

    progress.stop()

    ans()

    loading_window.mainloop()

def ans():
    ans_window = ctk.CTkToplevel()
    ans_window.title("Guess")
    ans_window.geometry("200x100")
    ans_window.attributes("-topmost", True)

    answ = ctk.CTkLabel(ans_window,height=300,width=200, text='Reading your Mind...', font=('Dubai',18))
    answ.pack()

    ans_window.after(5000)
    answ.destroy()
    #loading_window.destroy()
    
    label = ctk.CTkLabel(ans_window, text="The Number is:", font=('Dubai',14))
    label.pack(padx=20,pady=5)
    
    num = entry.get()
    answ = ctk.CTkLabel(ans_window,height=100,width=100, text=str(num), font=('Dubai',18))
    answ.pack(padx=20)
    
    ans_window.mainloop()

main = ctk.CTkFrame(root, width=300, height=200, corner_radius=10)
main.place(relx=0.5, rely=0.6, anchor=ctk.CENTER)
title = ctk.CTkLabel(root, corner_radius=10, text='Number Guesser' , font=('Dubai',25))
title.place(relx=0.5, rely=0.1, anchor=ctk.CENTER)

qn = ctk.CTkLabel(main, text="Think of a Number:", font=('Dubai',18))
qn.place(relx=0.5, rely=0.3, anchor=ctk.CENTER)

entry = ctk.CTkEntry(main, placeholder_text="Enter Number:", width=200, border_width=2, corner_radius=10)
entry.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

button_guess = ctk.CTkButton(main, text="Guess", width=15, border_width=0, corner_radius=8, command=ans)
button_guess.place(relx=0.5, rely=0.7, anchor=ctk.CENTER)









root.mainloop()
