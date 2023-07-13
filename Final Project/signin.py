
import tkinter as tk
from tkinter import *
from customtkinter import *
from PIL import ImageTk,Image
import mysql.connector as msconn

set_appearance_mode("System")
set_default_color_theme("green")

def main():
    main = CTk()
    main.title("Zero Hotel Booking")
    main.minsize(height=720,width=1440)

    main_pic = CTkImage(Image.open('images/logo.jpg'),size = (720,720))
    main_label = CTkLabel(main,text = '', image = main_pic)
    main_label._image = main_pic
    main_label.place(x=0,y=0)

    details = CTkFrame(main,height=720,width=720)
    details.place(x=720)
    CTkLabel(details,text='Zero Hotel Management Sytem', font=('Berlin Sans FB',40)).place(relx=0.5, rely=0.38, anchor=CENTER)
    CTkLabel(details,text='Made By:', font=('Dubai',25)).place(relx=0.5, rely=0.47, anchor=CENTER)
    CTkLabel(details,text='Samyog 12A', font=('Dubai',25)).place(relx=0.5, rely=0.52, anchor=CENTER)

    main.after(500,lambda:call_signup(main))
    main.resizable(False,False)
    main.mainloop()

def signup():
    sign = CTk()
    sign.title("Zero Hotel Booking")
    sign.minsize(height=720,width=1440)

    cur = sqlcon.cursor()

    cur.execute('select cust_email from credentials')
    edata = cur.fetchall()
    emails = []
    for i in edata:
        emails.append(i[0])

    def save_signin():
        misc = CTkLabel(signup,text='',text_color='red',width=500)
        misc.place(relx = 0.5,y = 444,anchor = CENTER)

        at = dot = up = no = spl = False
        
        email = entry_email.get()
        if email == '':
            misc.configure(text='Enter Email.!',width = 500)
        elif email in emails:
            misc.configure(text='Email already registered',width = 500)
        else:
            if '@' in email:
                at = True
            if '.' in email:
                dot = True
            if at is False or dot is False:
                misc.configure(text='Enter Correct Email Id.',width = 500)

        passw = entry_passw.get()
        if passw == '':
            misc.configure(text='Enter Password.!',width = 500)
        else:
            schar = '!@#$%^&*()_+|-=\\\'./'
            for i in passw:
                if i.isupper():
                    up = True
                    break
            for i in passw:
                if i.isdigit():
                    no = True
                    break
            for i in passw:
                if i in schar:
                    spl = True
                    break
            if spl == False:
                misc.configure(text='Your Password must have atleast one Special character.',width = 500)
            if no == False:
                misc.configure(text='Your Password must have atleast one Number.',width = 500)
            if up == False:
                misc.configure(text='Your Password must have atleast one Upper case character.',width = 500)
            if len(passw)<=8:
                misc.configure(text='The Password must have atleast 8 Characters.',width = 500)

        name = entry_name.get()
        if name == '':
            misc.configure(text='Enter Name.!',width = 500)
        
        if misc._text == '':
            cur.execute('insert into credentials(cust_name,cust_email,cust_pass) values("%s","%s","%s")'%(name,email,passw))
            sqlcon.commit()
            cur.close()
            call_mainapp(sign)


    def save_login():
        lmisc = CTkLabel(login,text='',text_color='red',width=500)
        lmisc.place(relx = 0.5,y = 444,anchor = CENTER)

        password = ''
        email = enter_email.get()
        if email == '':
            lmisc.configure(text='Enter Email.!',width = 500)
        else:
            cur.execute('select cust_pass from credentials where cust_email = "%s"'%(email,))
            password = cur.fetchall()
            if password == []:
                lmisc.configure(text='Incorrect Email or Password',width = 500)

        passw = enter_passw.get()
        if passw == '':
            lmisc.configure(text='Enter Password.!',width = 500)
        else:
            if passw == password[0][0]:
                cur.close()
                call_mainapp(sign)
            else:
                lmisc.configure(text='Incorrect Email or Password',width = 500)

    main_pic = CTkImage(Image.open('images/logo.jpg'),size = (200,200))
    
    #signup page
    signup = CTkFrame(sign,height=720,width=1440,corner_radius=15)

    login_pic = CTkLabel(signup,text = '', image = main_pic)
    login_pic._image = main_pic
    login_pic.place(relx=0.5,rely=0.19,anchor = CENTER)

    signup.place(relx = 0.5,rely = 0.5, anchor=CENTER)
    entry_name = CTkEntry(signup,placeholder_text = 'Name',height=45,width=300)
    entry_name.place(relx = 0.5,y = 290, anchor=CENTER)
    entry_email = CTkEntry(signup,placeholder_text = 'Email',height=45,width=300)
    entry_email.place(relx = 0.5,y = 349,anchor = CENTER)
    entry_passw = CTkEntry(signup,placeholder_text = 'Password',height=45,width=300)
    entry_passw.place(relx = 0.5,y = 409,anchor = CENTER)
    login_text = CTkLabel(signup,text='Already have an account?',).place(relx = 0.44,y = 470,anchor = CENTER)
    login_ = CTkLabel(signup,text='Log In', text_color='#44f1a6')
    login_.place(relx = 0.6,y = 470,anchor = CENTER)
    login_.bind("<Button-1>", lambda x:login.tkraise())
    button_signup = CTkButton(signup,text = 'Sign Up',width=300,height=45,command = lambda: save_signin())
    button_signup.place(relx=0.5,y=518,anchor = CENTER)



    #login page
    login = CTkFrame(sign,height=720,width=1440,corner_radius=15)

    signin_pic = CTkLabel(login,text = '', image = main_pic)
    signin_pic._image = main_pic
    signin_pic.place(relx=0.5,rely=0.19,anchor = CENTER)

    login.place(relx = 0.5,rely = 0.5, anchor=CENTER)
    enter_email = CTkEntry(login,placeholder_text = 'Email',height=45,width=300)
    enter_email.place(relx = 0.5,y = 332,anchor = CENTER)
    enter_passw = CTkEntry(login,placeholder_text = 'Password',height=45,width=300)
    enter_passw.place(relx = 0.5,y = 409,anchor = CENTER)
    signup_text = CTkLabel(login,text='Don\'t have an account?',).place(relx = 0.44,y = 470,anchor = CENTER)
    signup_ = CTkLabel(login,text='Sign Up', text_color='#44f1a6')
    signup_.place(relx = 0.6,y = 470,anchor = CENTER)
    signup_.bind("<Button-1>", lambda x:signup.tkraise())
    button_login = CTkButton(login,text = 'Log In',width=300,height=45,command=lambda: save_login())
    button_login.place(relx=0.5,y=518,anchor = CENTER)

    sign.mainloop()

def mainapp():
    root = CTk()
    root.title("Zero Hotel Booking")
    root.minsize(height=720,width=1440)







    root.mainloop()

def call_mainapp(sign):
	sign.destroy()
	mainapp()
    
def call_signup(main):
	main.destroy()
	signup()

if __name__ == '__main__':
    sqlcon = msconn.connect(host = 'localhost', user = 'root', passwd = 'root', database = 'hotel')
    main()
    sqlcon.close()