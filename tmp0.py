from tkinter import *
from tkinter import messagebox
def Main_Window():
      root.destroy()

def login():
    username=usernm.get()
    password=passwd.get()
    lc, uc, sp, nm = 0, 0, 0, 0
    uppercase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase="abcdefghijklmnopqrstuvwxyz"
    special="!@#$%^&~*_"
    number="0123456789"
    if (len(password) >= 8):
        for i in password:
                # counting lowercase alphabets
                if (i in lowercase):
                    lc+=1
                # counting uppercase alphabets
                if (i in uppercase):
                    uc+=1
                # counting digits
                if (i in number):
                    nm+=1
                # counting the mentioned special characters
                if(i in special):
                    sp+=1
    #Checking Validity of Username and Password
    if len(username)>=8 and (lc>=1 and uc>=1 and sp>=1 and nm>=1) and (lc+sp+uc+nm==len(password)):
        Main_Window() ######
    elif len(username)<8 and (lc<1 and uc<1 and sp<1 and nm<1)and lc+sp+uc+nm!=len(password):
                               messagebox.showerror("Login Unsucessful", "Invalid Username and Password")
    elif len(username)<8 :
        messagebox.showerror("Login Unsucessful", "Invalid Username")
    elif (lc<1 and uc<1 and sp<1 and nm<1)and lc+sp+uc+nm!=len(password):
        messagebox.showerror("Login Unsucessful", "Invalid Password")
#creating the Login window
root = Tk()
root.title ('Login')
root.geometry ('925x500+300+200')
root.configure(bg='#fff')
root.resizable(False, False)
#adding the image
imgs= PhotoImage(file='login.png')
Label(root, image=imgs, bg='white').place(x=50, y=50)
#creating textbox beside image
frame=Frame(root, width=350, height=350, bg='white')
frame.place(x=480, y=70)
#adding the title
heading=Label(frame, text='LOGIN', fg='#57a1f8', bg='white', font =('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=100, y=5)
#username
def on_enter(e):
    usernm.delete(0, 'end')
def on_leave(e):
    name=usernm.get()
    if name==' ':
        usernm.insert(0, 'Username')
usernm = Entry(frame, width =25, fg ='black', border=0, bg='white', font =('Microsoft YaHei UI Light', 11))
usernm.place(x=30, y=80)
usernm.insert(0, 'Username')
usernm.bind('<FocusIn>', on_enter)
usernm.bind('<FocusOut>', on_leave)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)
#password
def on_focus_in(event):
            passwd = event.widget
            if passwd.get() == 'Password':
                passwd.delete(0, 'end')
                passwd.config(show='▪️')
def on_focus_out(event):
    passwd = event.widget
    if passwd.get() == ' ':
        passwd.insert(0, 'Password')
        passwd.config(show=' ' )
passwd = Entry(frame, width=25, fg="black", border=0, bg="white", font=('Microsoft YaHei UI Light',10))
passwd.place(x=30,y=150)
passwd.bind("<FocusIn>", on_focus_in)
passwd.bind("<FocusOut>", on_focus_out)
passwd.insert(0,'Password')
Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)
#Sign in Button
Button(frame, width=39, pady=7, text='Login', bg="#57a1f8", fg ='white', border=0, command=login).place(x=35, y=230)
root.mainloop()