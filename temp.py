import customtkinter
import tkinter

app = customtkinter.CTk()
app.minsize(height=200,width=440)
scrollable_frame = customtkinter.CTkScrollableFrame(app, width=200, height=200)
scrollable_frame.pack()
customtkinter.CTkLabel(scrollable_frame,height=1000).pack()
app.mainloop()