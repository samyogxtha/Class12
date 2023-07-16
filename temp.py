import customtkinter
from customtkinter import *
import tkinter

import tkinter as tkinter
root = CTk()
def combobox_callback(choice):
    print("combobox dropdown clicked:", choice)

combobox = customtkinter.CTkComboBox(root,values=['All', 'Single','Double','Triple','Quad'],command=combobox_callback)
combobox.pack(padx=20, pady=10)
combobox.set("All")
root.mainloop()