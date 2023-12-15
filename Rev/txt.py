from tkinter import *

def prints():
    d = c.get()
    #mobile=503645873

    query = 'delete from employee where salary = {}'. format(d)
    print(d)
    print(d)
    print(query)

Petrol = Tk()
petrol = Label(Petrol, width=20, text="Petrol", font=30).grid(row=0, column=0)
PEtrol = Label(Petrol, width=50, text="Enter how much Petrol you have bought in litres.", font=20).grid(row=1, column=0)
c = Entry(Petrol, width=50, bg="grey", fg="white", borderwidth=4)
c.grid(row=2, column=0)
Seperator7 = Label(Petrol, text=" ", width=46, height=2).grid(row=3, column=0, columnspan=2)

Button(Petrol,text='cfd',command=lambda:prints()).grid()

Petrol.mainloop()

