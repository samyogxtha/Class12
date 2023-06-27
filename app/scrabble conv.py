import tkinter, random
import customtkinter as ctk
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")

def close_window():
    root.destroy()
    
def _no_of_player_():
    no_players = entry.get()
    
    
root = ctk.CTk()
root.geometry("610x550")
root.title("Scrabble Game")



v = 'aeiouAEIOU'
name_list = ['Players']
no_players = 0
#main square box
main = ctk.CTkFrame(root, width=600, height=540, corner_radius=10)
main.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
title = ctk.CTkLabel(main, corner_radius=10, text='Scrabble Game' , font=('Berlin Sans FB',45), width=580, height=100)
title.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

#the play area
first = ctk.CTkFrame(main,corner_radius=10, width=600, height=440)
first.place_configure(relx=0.5, rely=0.6, anchor=tkinter.CENTER)


qn = ctk.CTkLabel(first, text="Enter the number of Players:", font=('Berlin Sans FB',15))
qn.place(relx=0.5, y=15, anchor=tkinter.CENTER)
entry = ctk.CTkEntry(first, placeholder_text="Enter the number of Players:", width=200, border_width=2, corner_radius=10)
entry.place(x=133, y=33)
entry_btn = ctk.CTkButton(first, text='Submit', command=_no_of_player_)
entry_btn.place(x=343, y=33)
print(no_players)

score = {}
n,z = 0,1
for i in range(no_players):
    name = ctk.CTkEntry(master=root, placeholder_text="Enter Players Name:")
    name.pack(padx=20, pady=10)
    name = input('Enter the nam')
    score[name] = 0
    name_list.append(name)



root.mainloop()