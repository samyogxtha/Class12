from tkinter import *

def onclick():
    mylable2 = Label(root, text = e.get())
    mylable2.pack()
    



root = Tk()                                       #main window
root.geometry('400x200')
#mylable = Label(root, text = 'Hello World!')               #creating the lable widget
#mylable.grid(row=1,column=0)                           #putting it in the screeen

#typing field
e = Entry(root, width = 10)
e.pack()
e.get()
e.insert(0,'Enter Name')

#button
mybutton = Button(root, text = 'Submit!', command = onclick, fg='blue')
mybutton.pack()











root.mainloop()                                     #loop thing