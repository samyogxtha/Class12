from customtkinter import CTk,CTkButton,CTkProgressBar,CTkImage,CTkEntry,CTkLabel,CTkFrame,StringVar,CTkCheckBox,CTkTabview,CTkRadioButton,CTkScrollableFrame,CTkComboBox,CENTER,DISABLED,IntVar,set_default_color_theme,set_appearance_mode
from tkcalendar import Calendar
from PIL import Image
from datetime import datetime as dt
import mysql.connector as msconn

def main():
    main = CTk()
    main.title("Mavrik Hotel Booking")
    main.minsize(height=520,width=1040)
    main.attributes('-topmost', 1)
    main.overrideredirect(True)

    main_pic = CTkImage(Image.open('assets/logo.png'),size = (520,520))
    main_label = CTkLabel(main,text = '', image = main_pic)
    main_label._image = main_pic
    main_label.place(x=0,y=0)

    details = CTkFrame(main,height=520,width=520)
    details.place(x=520)
    CTkLabel(details,text='Mavrik Hotel', font=('HP Simplified',50)).place(relx=0.5, rely=0.35, anchor=CENTER)
    CTkLabel(details,text='Management Sytem', font=('HP Simplified',50)).place(relx=0.5, rely=0.45, anchor=CENTER)
    CTkLabel(details,text='Made By:', font=('Dubai',25)).place(relx=0.5, rely=0.55, anchor=CENTER)
    CTkLabel(details,text='Samyog 12A', font=('Dubai',25)).place(relx=0.5, rely=0.65, anchor=CENTER)

    main.after(3000,lambda:call_mainapp(main))
    main.resizable(False,False)
    main.mainloop()

def mainapp():
    root = CTk()
    root.title("Mavrik Hotel Booking")
    root.minsize(height=720,width=1440)

    #------------------FUNCTION-FOR-LOGGING-OUT------------------
    def logout():
        def logged_out():
            progressbar.stop()
            CTkLabel(logout_,height=200,text='Logged Out Successfully!',font=('HP Simplified',25,'bold')).place(relx=0.5,rely=0.5,anchor = CENTER)
            tabview.set("About")
            tabview.delete('Check Out')
            root.after(2000,lambda:frame_logout.destroy())

        loggedin[0] = False
        login_details.clear()
        button_login.configure(text='Log In',image=None ,command=lambda:loggin())

        frame_logout = CTkFrame(root,height=720,width=1440)
        frame_logout.place(relx = 0.5,rely = 0.5,anchor = CENTER)

        bottompic2 = CTkImage(Image.open('assets/loginbg.png'),size = (1440,720))
        bpic2 = CTkLabel(frame_logout,text = '', image = bottompic2)
        bpic2._image = bottompic2
        bpic2.place(relx=0.5,rely=0.5,anchor = CENTER)

        logout_ = CTkFrame(frame_logout,height=620,width=540,corner_radius=20)
        logout_.place(relx = 0.5,rely = 0.5, anchor=CENTER)

        progressbar = CTkProgressBar(logout_,height=50,mode="indeterminate")
        progressbar.place(relx = 0.5,rely = 0.5, anchor=CENTER)
        CTkLabel(logout_,text='Logging Out...',font=('HP Simplified',20,'bold')).place(relx=0.5,rely=0.6,anchor = CENTER)
        progressbar.start()

        root.after(3000,lambda:logged_out())

    #------------------FUNCTION-FOR-LOGGING-AND-SIGNING-IN------------------
    def loggin():
        cur0 = sqlcon.cursor()

        cur0.execute('select email from customers')
        edata = cur0.fetchall()
        emails = []
        for i in edata:
            emails.append(i[0])

        def save_signin():
            def logged_in(progress):
                progress.stop()
                cur0.close()
                sqlcon.commit()
                CTkLabel(signin_,height=620,width=540,corner_radius=20,text='Signed In Successfully!',font=('HP Simplified',25,'bold')).place(relx=0.5,rely=0.5,anchor = CENTER)
                update_logbutton()
                update_checkout()
                root.after(2000,lambda:frame_login.destroy())

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
                    misc.configure(text='Enter Valid Email Id.',width = 500)

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
                if len(passw)<8:
                    misc.configure(text='The Password must have atleast 8 Characters.',width = 500)

            name = entry_name.get()
            if name == '':
                misc.configure(text='Enter Name.!',width = 500)
            
            if misc._text == '':
                cur0.execute('insert into customers(name,email,pass) values("%s","%s","%s")'%(name,email,passw))
                sqlcon.commit()
                cur0.execute('select * from customers where email = "%s"'%(email))
                data = cur0.fetchall()[0]
                loggedin[0] = True
                login_details.clear()
                login_details.insert(0,list(data))

                signin_ = CTkFrame(frame_login,height=620,width=540,corner_radius=20)
                signin_.place(relx = 0.5,rely = 0.5, anchor=CENTER)

                progressbar = CTkProgressBar(signin_,height=50,mode="indeterminate")
                progressbar.place(relx = 0.5,rely = 0.5, anchor=CENTER)
                CTkLabel(signin_,text='Signing In...',font=('HP Simplified',20,'bold')).place(relx=0.5,rely=0.6,anchor = CENTER)
                progressbar.start()

                root.after(3000,lambda:logged_in(progressbar))

        def save_login():
            def logged_in(progress):
                progress.stop()
                cur0.close()
                CTkLabel(logoin_,height=200,corner_radius=20,text='Logged In Successfully!',font=('HP Simplified',25,'bold')).place(relx=0.5,rely=0.5,anchor = CENTER)
                update_logbutton()
                update_checkout()
                root.after(2000,lambda:frame_login.destroy())

            lmisc = CTkLabel(login,text='',text_color='red',width=500)
            lmisc.place(relx = 0.5,y = 444,anchor = CENTER)

            password = []
            email = enter_email.get()
            if email == '':
                lmisc.configure(text='Enter Email.!',width = 500)
            else:
                cur0.execute('select pass from customers where email = "%s"'%(email,))
                password.insert(0,cur0.fetchall())
                if password[0] == []:
                    lmisc.configure(text='Incorrect Email or Password',width = 500)

            passw = enter_passw.get()
            if passw == '':
                lmisc.configure(text='Enter Password.!',width = 500)
            elif password[0] == []:
                lmisc.configure(text='Incorrect Email or Password',width = 500)
            else:
                if passw == password[0][0][0]:
                    cur0.execute('select * from customers where email = "%s"'%(email))
                    data = cur0.fetchall()[0]
                    loggedin[0] = True
                    login_details.clear()
                    login_details.insert(0,list(data))

                    logoin_ = CTkFrame(frame_login,height=620,width=540,corner_radius=20)
                    logoin_.place(relx = 0.5,rely = 0.5, anchor=CENTER)

                    progressbar = CTkProgressBar(logoin_,height=50,mode="indeterminate")
                    progressbar.place(relx = 0.5,rely = 0.5, anchor=CENTER)
                    CTkLabel(logoin_,text='Logging In...',font=('HP Simplified',20,'bold')).place(relx=0.5,rely=0.6,anchor = CENTER)
                    progressbar.start()

                    root.after(3000,lambda:logged_in(progressbar))
                else:
                    lmisc.configure(text='Incorrect Email or Password',width = 500)

        main_pic = CTkImage(Image.open('assets/logo.png'),size = (200,200))
        bottompic1 = CTkImage(Image.open('assets/loginbg.png'),size = (1440,720))

        frame_login = CTkFrame(root,height=720,width=1440)
        frame_login.place(relx = 0.5,rely = 0.5, anchor=CENTER)
        
        bpic1 = CTkLabel(frame_login,text = '', image = bottompic1)
        bpic1._image = bottompic1
        bpic1.place(relx=0.5,rely=0.5,anchor = CENTER)
        
        #signup page
        signup = CTkFrame(frame_login,height=620,width=540,corner_radius=20)
        signup.place(relx = 0.5,rely = 0.5, anchor=CENTER)
        login_pic = CTkLabel(signup,text = '', image = main_pic)
        login_pic._image = main_pic
        login_pic.place(relx=0.5,rely=0.21,anchor = CENTER)
        
        CTkButton(signup,text='←',height=50,width=50,corner_radius=30,fg_color='transparent', hover_color='#333333', command=lambda:frame_login.destroy()).place(x=1,y=1)
        entry_name = CTkEntry(signup,placeholder_text = 'Name',height=45,width=300)
        entry_name.place(relx = 0.5,y = 290, anchor=CENTER)
        entry_email = CTkEntry(signup,placeholder_text = 'Email',height=45,width=300)
        entry_email.place(relx = 0.5,y = 349,anchor = CENTER)
        entry_passw = CTkEntry(signup,placeholder_text = 'Password',height=45,width=300)
        entry_passw.place(relx = 0.5,y = 409,anchor = CENTER)
        CTkLabel(signup,text='Already have an account?',).place(relx = 0.37,y = 470,anchor = CENTER)
        login_ = CTkLabel(signup,text='Log In', text_color='#44f1a6')
        login_.place(relx = 0.73,y = 470,anchor = CENTER)
        login_.bind("<Button-1>", lambda x:login.tkraise())
        button_signup = CTkButton(signup,text = 'Sign Up',width=300,height=45,command = lambda: save_signin())
        button_signup.place(relx=0.5,y=518,anchor = CENTER)

        #login page
        login = CTkFrame(frame_login,height=620,width=540,corner_radius=20)
        login.place(relx = 0.5,rely = 0.5, anchor=CENTER)

        signin_pic = CTkLabel(login,text = '', image = main_pic)
        signin_pic._image = main_pic
        signin_pic.place(relx=0.5,rely=0.21,anchor = CENTER)
        
        CTkButton(login,text='←',height=50,width=50,corner_radius=30,fg_color='transparent', hover_color='#333333', command=lambda:frame_login.destroy()).place(x=1,y=1)
        enter_email = CTkEntry(login,placeholder_text = 'Email',height=45,width=300)
        enter_email.place(relx = 0.5,y = 332,anchor = CENTER)
        enter_passw = CTkEntry(login,placeholder_text = 'Password',height=45,width=300)
        enter_passw.place(relx = 0.5,y = 409,anchor = CENTER)
        CTkLabel(login,text='Don\'t have an account?',).place(relx = 0.35,y = 470,anchor = CENTER)
        signup_ = CTkLabel(login,text='Sign Up', text_color='#44f1a6')
        signup_.place(relx = 0.728,y = 470,anchor = CENTER)
        signup_.bind("<Button-1>", lambda x:signup.tkraise())
        button_login = CTkButton(login,text = 'Log In',width=300,height=45,command=lambda: save_login())
        button_login.place(relx=0.5,y=518,anchor = CENTER)

    def update_logbutton():
        #profile_pic = CTkImage(Image.open('assets/profile.png'),size = (58,58))
        button_login.configure(text='Log Out',command=lambda:logout())#text='',image=profile_pic
        #button_login._image = profile_pic
        
    def update_checkout():
        try:
            cur = sqlcon.cursor()
            cur.execute(f'select * from bookings where cust_id = {login_details[0][0]} order by booking_id desc limit 1')
            det = cur.fetchall()[0]
            booking_details.clear()
            booking_details.append(det)
            
            def checkout():
                def checkout_():

                    def closeall():
                        out.destroy()

                    CTkLabel(fr_chkout,height=200,text='Checked Out Successfully!',font=('HP Simplified',25,'bold')).place(relx=0.5,rely=0.5,anchor = CENTER)
                    
                    root.after(2000,lambda:closeall())
                    cur.close()
                out = CTkFrame(chk_out,height=590,width=1422,corner_radius=30)
                out.place(relx = 0.5,rely = 0.5, anchor=CENTER)

                outp = CTkImage(Image.open('assets/loginbg.png'),size = (1440,720))
                outpic = CTkLabel(out,text = '', image = outp)
                outpic._image = outp
                outpic.place(relx=0.5,rely=0.5,anchor = CENTER)

                out_ = CTkFrame(out,height=520,width=540,corner_radius=30)
                out_.place(relx = 0.5,rely = 0.5, anchor=CENTER)

                progressbar = CTkProgressBar(out_,height=50,mode="indeterminate")
                progressbar.place(relx = 0.5,rely = 0.5, anchor=CENTER)
                CTkLabel(out_,text='Checking Out...',font=('HP Simplified',20,'bold')).place(relx=0.5,rely=0.6,anchor = CENTER)
                progressbar.start()

                root.after(3000,lambda:checkout_())

            chk_out = tabview.add("Check Out")
            fr_chkout = CTkFrame(chk_out, width=1440, height=720)
            fr_chkout.place(relx = 0.5,rely = 0.5, anchor=CENTER)
            
            CTkButton(fr_chkout,text='Check Out',command=lambda:checkout()).place(relx = 0.5,rely = 0.5, anchor=CENTER)
        except:
            pass
        
    #main app
    frame = CTkFrame(root,height=720,width=1440,corner_radius=15)
    frame.place(relx = 0.5,rely = 0.5, anchor=CENTER)

    #------------------TOP-BANNER------------------
    banner_pic = CTkImage(Image.open('assets/banner2.png'),size = (1440,120))
    topbanner = CTkLabel(frame,text = '', image = banner_pic)
    topbanner._image = banner_pic
    topbanner.place(relx=0.5,rely=0.086,anchor = CENTER)

    button_login = CTkButton(frame,width=70,height=70,text='Log In',command=lambda:loggin())
    button_login.place(relx=0.97,rely=0.065,anchor=CENTER)
    
    #------------------CREATE-TABS------------------
    tabview = CTkTabview(frame,width=1440,height=630)
    tabview.place(relx=0.5,rely=0.56,anchor=CENTER)

    #------------------ABOUT-TAB------------------
    about = tabview.add("About")
    
    pic = CTkFrame(about,height=630,width=1440,corner_radius=15)
    pic.place(relx = 0.5,rely = 0.5, anchor=CENTER)

    image_files = ['assets/image0.jpg','assets/image1.jpg', 'assets/image2.jpg', 'assets/image3.jpg','assets/image4.jpg','assets/image5.jpg']
    images = []

    def load_images():
        for file in image_files:
            image = CTkImage(Image.open(file),size=(1440,630))
            images.append(image)
        canvas.configure(image=images[0])

    canvas = CTkLabel(pic, text = '', width=1440, height=630)
    canvas.pack()

    def next_image(index):
        canvas.configure(image=images[index])
        index += 1
        if index >= len(images):
            index = 0
        root.after(5000, next_image, index)

    load_images()
    next_image(0)

    #------------------CONTACS-TAB------------------
    contact = tabview.add("Contact")

    fr_mgr = CTkFrame(contact,height=275,width=680,corner_radius=15)
    fr_mgr.place(relx = 0.25,rely = 0.25, anchor=CENTER)

    mgr_pic = CTkImage(Image.open('assets/mgr.jpg'),size = (275,275))
    mgr = CTkLabel(fr_mgr,text = '', image = mgr_pic)
    mgr._image = mgr_pic
    mgr.place(x=137.5,rely=0.5,anchor = CENTER)

    CTkLabel(fr_mgr,text="Manager",font=('HP Simplified',47,'bold')).place(x=290,y=60)
    CTkLabel(fr_mgr,text="Mr. Gru",font=('HP Simplified',32,'bold')).place(x=290,y=109)
    CTkLabel(fr_mgr,text="Extention : 117",font=('HP Simplified',27)).place(x=290,y=150)
    CTkLabel(fr_mgr,text="Mail : manager@mavrik.com",font=('HP Simplified',27)).place(x=290,y=185)

    fr_rec = CTkFrame(contact,height=275,width=680,corner_radius=15)
    fr_rec.place(relx = 0.75,rely = 0.25, anchor=CENTER)

    rec_pic = CTkImage(Image.open('assets/rec.jpg'),size = (275,275))
    rec = CTkLabel(fr_rec,text = '', image = rec_pic)
    rec._image = rec_pic
    rec.place(x=137.5,rely=0.5,anchor = CENTER)

    CTkLabel(fr_rec,text="Customer Service",font=('HP Simplified',47,'bold')).place(x=290,y=60)
    CTkLabel(fr_rec,text="Mr. Sam",font=('HP Simplified',32,'bold')).place(x=290,y=109)
    CTkLabel(fr_rec,text="Extention : 225",font=('HP Simplified',27)).place(x=290,y=150)
    CTkLabel(fr_rec,text="Mail : customerservice@mavrik.com",font=('HP Simplified',27)).place(x=290,y=185)
    
    fr_serv = CTkFrame(contact,height=275,width=680,corner_radius=15)
    fr_serv.place(relx = 0.25,rely = 0.75, anchor=CENTER)

    serv_pic = CTkImage(Image.open('assets/serv.jpg'),size = (275,275))
    serv = CTkLabel(fr_serv,text = '', image = serv_pic)
    serv._image = serv_pic
    serv.place(x=137.5,rely=0.5,anchor = CENTER)

    CTkLabel(fr_serv,text="Room Service",font=('HP Simplified',47,'bold')).place(x=290,y=60)
    CTkLabel(fr_serv,text="Ms. Anya",font=('HP Simplified',32,'bold')).place(x=290,y=109)
    CTkLabel(fr_serv,text="Extention : 147",font=('HP Simplified',27)).place(x=290,y=150)
    CTkLabel(fr_serv,text="Mail : roomservice@mavrik.com",font=('HP Simplified',27)).place(x=290,y=185)

    fr_cook = CTkFrame(contact,height=275,width=680,corner_radius=15)
    fr_cook.place(relx = 0.75,rely = 0.75, anchor=CENTER)

    cook_pic = CTkImage(Image.open('assets/cook.jpg'),size = (275,275))
    cook = CTkLabel(fr_cook,text = '', image = cook_pic)
    cook._image = cook_pic
    cook.place(x=137.5,rely=0.5,anchor = CENTER)

    CTkLabel(fr_cook,text="Restaurant",font=('HP Simplified',47,'bold')).place(x=290,y=60)
    CTkLabel(fr_cook,text="Mr. Kim",font=('HP Simplified',32,'bold')).place(x=290,y=109)
    CTkLabel(fr_cook,text="Extention : 125",font=('HP Simplified',27)).place(x=290,y=150)
    CTkLabel(fr_cook,text="Mail : dining@mavrik.com",font=('HP Simplified',27)).place(x=290,y=185)

    #------------------PRICING-TAB------------------
    pricing = tabview.add("Rooms & Pricings")

    def price_book(type):
        cur2 = sqlcon.cursor()
        cur2.execute(f'select * from rooms where type = "{type}" and availability = "yes"')
        fil_data = cur2.fetchall()
        table.configure(row=len(fil_data), column=7, values=fil_data)
        cur2.close()
        tabview.set('Book a Room')

    fr_single = CTkFrame(pricing,height=275,width=680,corner_radius=15)
    fr_single.place(relx = 0.25,rely = 0.25, anchor=CENTER)

    single_pic = CTkImage(Image.open('assets/single.jpg'),size = (275,275))
    single = CTkLabel(fr_single,text = '', image = single_pic)
    single._image = single_pic
    single.place(x=137.5,rely=0.5,anchor = CENTER)

    CTkLabel(fr_single,text="Single Room",font=('HP Simplified',47,'bold')).place(x=290,y=45)
    CTkLabel(fr_single,text="Basic    $200",font=('HP Simplified',27)).place(x=300,y=100)
    CTkLabel(fr_single,text="WiFi       +$50",font=('HP Simplified',27)).place(x=300,y=130)
    CTkLabel(fr_single,text="TV          +$50",font=('HP Simplified',27)).place(x=300,y=160)
    CTkLabel(fr_single,text="AC          +$50",font=('HP Simplified',27)).place(x=300,y=185)
    CTkButton(fr_single,text='Book',height=50,width=80, command=lambda:price_book('Single')).place(relx=0.92,rely=0.85,anchor=CENTER)

    fr_double = CTkFrame(pricing,height=275,width=680,corner_radius=15)
    fr_double.place(relx = 0.75,rely = 0.25, anchor=CENTER)

    double_pic = CTkImage(Image.open('assets/double.jpg'),size = (275,275))
    double = CTkLabel(fr_double,text = '', image = double_pic)
    double._image = double_pic
    double.place(x=137.5,rely=0.5,anchor = CENTER)

    CTkLabel(fr_double,text="Double Room",font=('HP Simplified',47,'bold')).place(x=290,y=45)
    CTkLabel(fr_double,text="Basic    $250",font=('HP Simplified',27)).place(x=300,y=100)
    CTkLabel(fr_double,text="WiFi       +$50",font=('HP Simplified',27)).place(x=300,y=130)
    CTkLabel(fr_double,text="TV          +$50",font=('HP Simplified',27)).place(x=300,y=160)
    CTkLabel(fr_double,text="AC          +$50",font=('HP Simplified',27)).place(x=300,y=185)
    CTkButton(fr_double,text='Book',height=50,width=80, command=lambda:price_book('Double')).place(relx=0.92,rely=0.85,anchor=CENTER)
    
    fr_triple = CTkFrame(pricing,height=275,width=680,corner_radius=15)
    fr_triple.place(relx = 0.25,rely = 0.75, anchor=CENTER)

    triple_pic = CTkImage(Image.open('assets/triple.jpg'),size = (275,275))
    triple = CTkLabel(fr_triple,text = '', image = triple_pic)
    triple._image = triple_pic
    triple.place(x=137.5,rely=0.5,anchor = CENTER)

    CTkLabel(fr_triple,text="Triple Room",font=('HP Simplified',47,'bold')).place(x=290,y=45)
    CTkLabel(fr_triple,text="Basic    $300",font=('HP Simplified',27)).place(x=300,y=100)
    CTkLabel(fr_triple,text="WiFi       +$50",font=('HP Simplified',27)).place(x=300,y=130)
    CTkLabel(fr_triple,text="TV          +$50",font=('HP Simplified',27)).place(x=300,y=160)
    CTkLabel(fr_triple,text="AC          +$50",font=('HP Simplified',27)).place(x=300,y=185)
    CTkButton(fr_triple,text='Book',height=50,width=80, command=lambda:price_book('Triple')).place(relx=0.92,rely=0.85,anchor=CENTER)

    fr_quad = CTkFrame(pricing,height=275,width=680,corner_radius=15)
    fr_quad.place(relx = 0.75,rely = 0.75, anchor=CENTER)

    quad_pic = CTkImage(Image.open('assets/quad.jpg'),size = (275,275))
    quad = CTkLabel(fr_quad,text = '', image = quad_pic)
    quad._image = quad_pic
    quad.place(x=137.5,rely=0.5,anchor = CENTER)

    CTkLabel(fr_quad,text="Quad Room",font=('HP Simplified',47,'bold')).place(x=290,y=45)
    CTkLabel(fr_quad,text="Basic    $350",font=('HP Simplified',27)).place(x=300,y=100)
    CTkLabel(fr_quad,text="WiFi       +$50",font=('HP Simplified',27)).place(x=300,y=130)
    CTkLabel(fr_quad,text="TV          +$50",font=('HP Simplified',27)).place(x=300,y=160)
    CTkLabel(fr_quad,text="AC          +$50",font=('HP Simplified',27)).place(x=300,y=185)
    CTkButton(fr_quad,text='Book',height=50,width=80, command=lambda:price_book('Quad')).place(relx=0.92,rely=0.85,anchor=CENTER)

    #-----------------------------NEW-BOOKING-TAB---------------------------------
    booking_ = tabview.add("Book")

    booking_bg = CTkImage(Image.open('utbg0.png'),size = (1440,720))
    bookingbg = CTkLabel(booking_,text='', image=booking_bg)
    bookingbg._image = booking_bg
    bookingbg.place(relx = 0.5,rely = 0.5, anchor=CENTER)

    select_date_ = CTkFrame(booking_,height=540,width=540,corner_radius=20)
    select_date_.place(relx = 0.5,rely = 0.5, anchor=CENTER)

    def select_datein():
        fr_indate = CTkFrame(booking_,height=250,width=200)
        fr_indate.place(relx = 0.7,rely = 0.3, anchor=CENTER)

        tkc1 = Calendar(fr_indate,selectmode = "day",year=int(today[0:4]),month=int(today[6:7]),date=int(today[9:]))
        tkc1.pack(padx=10,pady=10)

        def fetch_date():
            checkin_date.configure(state='normal')
            fr_indate.destroy()
            checkin_date.delete(0,10)
            checkin_date.insert(0,tkc1.selection_get().strftime('%Y-%m-%d'))
            checkin_date.configure(state=DISABLED)

        button = CTkButton(fr_indate,text="Select Date",command=fetch_date)
        button.pack(padx=10,pady=10)
        
    CTkLabel(select_date_,text="Checkin Date (yyyy-mm-dd)*",font=('HP Simplified',17)).place(relx = 0.5,rely = 0.4, anchor=CENTER)
    checkin_date = CTkEntry(select_date_,placeholder_text = 'Checkin Date*',height=45,width=300)
    checkin_date.place(relx = 0.5,rely = 0.3, anchor=CENTER)
    checkin_date.bind("<Button-1>", lambda x:select_datein())

    def select_dateout():
        fr_outdate = CTkFrame(booking_,height=250,width=200)
        fr_outdate.place(relx = 0.7,rely = 0.6, anchor=CENTER)

        tkc1 = Calendar(fr_outdate,selectmode = "day",year=int(today[0:4]),month=int(today[6:7]),date=int(today[9:]))
        tkc1.pack(padx=10,pady=10)

        def fetch_date():
            checkout_date.configure(state='normal')
            fr_outdate.destroy()
            checkout_date.delete(0,10)
            checkout_date.insert(0,tkc1.selection_get().strftime('%Y-%m-%d'))
            checkout_date.configure(state=DISABLED)

        button = CTkButton(fr_outdate,text="Select Date",command=fetch_date)
        button.pack(padx=10,pady=10)

    CTkLabel(select_date_,text="Checkout Date (yyyy-mm-dd)*",font=('HP Simplified',17)).place(relx = 0.5,rely = 0.7, anchor=CENTER)
    checkout_date = CTkEntry(select_date_,placeholder_text = 'Checkout Date*',height=45,width=300)
    checkout_date.place(relx = 0.5,rely = 0.6, anchor=CENTER)
    checkout_date.bind("<Button-1>", lambda x:select_dateout())

    err_msg0 = CTkLabel(select_date_,text='',text_color='red')
    err_msg0.place(relx=0.5,rely=0.95,anchor=CENTER)

    def next_sel():
        global diff
        now_diff = (dt.strptime(checkin_date.get(), "%Y-%m-%d") - dt.strptime(today, "%Y-%m-%d")).days
        if now_diff > -1:
            diff = (dt.strptime(checkout_date.get(), "%Y-%m-%d") - dt.strptime(checkin_date.get(), "%Y-%m-%d")).days
            if diff > 0:
                select_type()
            else:
                err_msg0.configure(text='Please Select a valid date range!')
        else:
            err_msg0.configure(text='Checkin date cannot be in the past')

    CTkButton(booking_,height=100,width=100,text='Next →', font=('HP Simplified',17), command=lambda:next_sel() if checkin_date.get() != '' and checkout_date.get() != '' else err_msg0.configure(text='*Please enter Date*')).place(relx=0.85,rely=0.5,anchor = CENTER)

    def select_type():
        select_type_ = CTkFrame(booking_,height=540,width=540,corner_radius=20)
        select_type_.place(relx = 0.5,rely = 0.5, anchor=CENTER)

        CTkLabel(select_type_,corner_radius=20,text='Please choose the type of room',font=('HP Simplified',25,'bold')).place(relx=0.5,y=45,anchor = CENTER)

        radio_var = StringVar()

        radiobutton_1 = CTkRadioButton(select_type_, text="Single", font=('HP Simplified',13), variable= radio_var, value='Single')
        radiobutton_2 = CTkRadioButton(select_type_, text="Double", font=('HP Simplified',13), variable= radio_var, value='Double')
        radiobutton_3 = CTkRadioButton(select_type_, text="Triple", font=('HP Simplified',13), variable= radio_var, value='Triple')
        radiobutton_4 = CTkRadioButton(select_type_, text="Quad", font=('HP Simplified',13), variable= radio_var, value='Quad')

        radiobutton_1.place(relx=0.25,rely=0.5,anchor = CENTER)
        radiobutton_2.place(relx=0.75,rely=0.5,anchor = CENTER)
        radiobutton_3.place(relx=0.25,rely=0.9,anchor = CENTER)
        radiobutton_4.place(relx=0.75,rely=0.9,anchor = CENTER)

        pic1 = CTkImage(Image.open('assets/single.jpg'),size = (175,175))
        pic_1 = CTkLabel(select_type_,corner_radius=10,text = '', image = pic1)
        pic_1._image = pic1
        pic_1.place(relx=0.25,rely=0.3,anchor = CENTER)
        pic_1.bind("<Button-1>", lambda x:radiobutton_1.invoke())

        pic2 = CTkImage(Image.open('assets/double.jpg'),size = (175,175))
        pic_2 = CTkLabel(select_type_,text = '', image = pic2)
        pic_2._image = pic2
        pic_2.place(relx=0.75,rely=0.3,anchor = CENTER)
        pic_2.bind("<Button-1>", lambda x:radiobutton_2.invoke())

        pic3 = CTkImage(Image.open('assets/triple.jpg'),size = (175,175))
        pic_3 = CTkLabel(select_type_,text = '', image = pic3)
        pic_3._image = pic3
        pic_3.place(relx=0.25,rely=0.7,anchor = CENTER)
        pic_3.bind("<Button-1>", lambda x:radiobutton_3.invoke())

        pic4 = CTkImage(Image.open('assets/quad.jpg'),size = (175,175))
        pic_4 = CTkLabel(select_type_,text = '', image = pic4)
        pic_4._image = pic4
        pic_4.place(relx=0.75,rely=0.7,anchor = CENTER)
        pic_4.bind("<Button-1>", lambda x:radiobutton_4.invoke())

        err_msg1 = CTkLabel(select_type_,text='',text_color='red')
        err_msg1.place(relx=0.5,rely=0.95,anchor=CENTER)

        def back_date():
            next_misc_.destroy()
            back_date_.destroy()
            select_type_.destroy()

        back_date_ = CTkButton(booking_,height=100,width=100,text='← Back', font=('HP Simplified',17), command=lambda:back_date())
        back_date_.place(relx=0.15,rely=0.5,anchor = CENTER)

        next_misc_ = CTkButton(booking_,height=100,width=100,text='Next →', font=('HP Simplified',17), command=lambda:select_misc() if radio_var.get() != '' else err_msg1.configure(text='*Please select an Option!*'))
        next_misc_.place(relx=0.85,rely=0.5,anchor = CENTER)
        
        def select_misc():
            select_misc_ = CTkFrame(booking_,height=540,width=540,corner_radius=20)
            select_misc_.place(relx = 0.5,rely = 0.5, anchor=CENTER)

            CTkLabel(select_misc_,corner_radius=20,text='Enhance your stay. Select add-ons and extras:',font=('Dubai',25,'bold')).place(relx=0.5,rely=0.05,anchor = CENTER)
            
            fr_transfer = CTkFrame(select_misc_,corner_radius=20,height=150,width=520)
            fr_transfer.place(relx=0.5,rely = 0.24,anchor = CENTER)
            transfer_img = CTkImage(Image.open('assets/car.jpg'),size = (150,150))
            transfer_img_ = CTkLabel(fr_transfer,text = '', image = transfer_img)
            transfer_img_._image = transfer_img
            transfer_img_.place(x=75,rely=0.5,anchor = CENTER)
            CTkLabel(fr_transfer,text='Airport Transfer', font=('HP Simplified',30)).place(x=265,rely=0.4,anchor = CENTER)
            CTkLabel(fr_transfer,text='$50 per unit', font=('HP Simplified',15)).place(x=210,rely=0.6,anchor = CENTER)
            transfer_var = StringVar()
            checkbox_transfer = CTkCheckBox(fr_transfer,text='',variable=transfer_var, onvalue='yes', offvalue='no')
            checkbox_transfer.place(relx = 0.95,rely = 0.5, anchor=CENTER)
            transfer_img_.bind("<Button-1>", lambda x:checkbox_transfer.toggle())
            fr_transfer.bind("<Button-1>", lambda x:checkbox_transfer.toggle())

            fr_tour = CTkFrame(select_misc_,corner_radius=20,height=150,width=520)
            fr_tour.place(relx=0.5,rely = 0.54,anchor = CENTER)
            tour_img = CTkImage(Image.open('assets/tour.jpg'),size = (150,150))
            tour_img_ = CTkLabel(fr_tour,text = '', image = tour_img)
            tour_img_._image = tour_img
            tour_img_.place(x=75,rely=0.5,anchor = CENTER)
            CTkLabel(fr_tour,text='City Tour', font=('HP Simplified',30)).place(x=220,rely=0.4,anchor = CENTER)
            CTkLabel(fr_tour,text='$170 per night', font=('HP Simplified',15)).place(x=220,rely=0.6,anchor = CENTER)
            tour_var = StringVar()
            checkbox_tour = CTkCheckBox(fr_tour,text='',variable=tour_var, onvalue='yes', offvalue='no')
            checkbox_tour.place(relx = 0.95,rely = 0.5, anchor=CENTER)
            tour_img_.bind("<Button-1>", lambda x:checkbox_tour.toggle())
            fr_tour.bind("<Button-1>", lambda x:checkbox_tour.toggle())

            fr_feast = CTkFrame(select_misc_,corner_radius=20,height=150,width=520)
            fr_feast.place(relx=0.5,rely = 0.84,anchor = CENTER)
            feast_img = CTkImage(Image.open('assets/feast.jpg'),size = (150,150))
            feast_img_ = CTkLabel(fr_feast,text = '', image = feast_img)
            feast_img_._image = feast_img
            feast_img_.place(x=75,rely=0.5,anchor = CENTER)
            CTkLabel(fr_feast,text='Breakfast and Lunch', font=('HP Simplified',30)).place(x=290,rely=0.4,anchor = CENTER)
            CTkLabel(fr_feast,text='$100 per night', font=('HP Simplified',15)).place(x=220,rely=0.6,anchor = CENTER)
            feast_var = StringVar()
            checkbox_feast = CTkCheckBox(fr_feast,text='',variable=feast_var, onvalue='yes', offvalue='no')
            checkbox_feast.place(relx = 0.95,rely = 0.5, anchor=CENTER)
            feast_img_.bind("<Button-1>", lambda x:checkbox_feast.toggle())
            fr_feast.bind("<Button-1>", lambda x:checkbox_feast.toggle())

            def back_sel():
                select_misc_.destroy()
                misc_back.destroy()
                misc_next.destroy()

            misc_back = CTkButton(booking_,height=100,width=100,text='← Back', font=('HP Simplified',17), command=lambda:back_sel())
            misc_back.place(relx=0.15,rely=0.5,anchor = CENTER)

            def show_details():
                show_details_ = CTkFrame(booking_,height=540,width=540,corner_radius=20)
                show_details_.place(relx = 0.5,rely = 0.5, anchor=CENTER)

                CTkLabel(show_details_,corner_radius=20,text='Booking Summary:',font=('Dubai',25,'bold')).place(relx=0.5,rely=0.05,anchor = CENTER)
                #             #show details of selected booking
                CTkLabel(show_details_,text=f"Checkin Date: {checkin_date.get()}",font=('HP Simplified',17)).place(relx = 0.25,rely = 0.2, anchor=CENTER)
                CTkLabel(show_details_,text=f"Checkout Date: {checkout_date.get()}",font=('HP Simplified',17)).place(relx = 0.25,rely = 0.3, anchor=CENTER)
                CTkLabel(show_details_,text=f"Number of Days: {diff}",font=('HP Simplified',17)).place(relx = 0.25,rely = 0.4, anchor=CENTER)
                CTkLabel(show_details_,text=f"Type: {radio_var.get()}",font=('HP Simplified',17)).place(relx = 0.75,rely = 0.2, anchor=CENTER)
                cur = sqlcon.cursor()
                cur.execute(f'select * from rooms where type = "{radio_var.get()}"')
                cur_room = cur.fetchall()[0]
                CTkLabel(show_details_,text=f"Room No: {cur_room[0]}",font=('HP Simplified',17)).place(relx = 0.75,rely = 0.3, anchor=CENTER)
                CTkLabel(show_details_,text="Addons",font=('HP Simplified',17,'bold')).place(relx = 0.3,rely = 0.55, anchor=CENTER)
                CTkLabel(show_details_,text="Total",font=('HP Simplified',17,'bold')).place(relx = 0.79,rely = 0.55, anchor=CENTER)
                
                addons = CTkFrame(show_details_,corner_radius=20,width=300)
                addons.place(relx = 0.3,rely = 0.77, anchor=CENTER)
                add0 = CTkLabel(addons,text='',font=('HP Simplified',17))
                add0.place(relx=0.5,rely=0.25,anchor = CENTER)
                add1 = CTkLabel(addons,text='',font=('HP Simplified',17))
                add1.place(relx=0.5,rely=0.5,anchor = CENTER)
                add2 = CTkLabel(addons,text='',font=('HP Simplified',17))
                add2.place(relx=0.5,rely=0.75,anchor = CENTER)

                if transfer_var.get() == 'yes':
                    add0.configure(text='Airport Transfer')
                    if tour_var.get() == 'yes':
                        add1.configure(text="City Tour")
                        if feast_var.get() == 'yes':
                            add2.configure(text='Breakfast and Lunch')
                    elif feast_var.get() == 'yes':
                        add1.configure(text='Breakfast and Lunch')
                elif tour_var.get() == 'yes':
                    add0.configure(text='City Tour')
                    if feast_var.get() == 'yes':
                        add1.configure(text='Breakfast and Lunch')
                elif feast_var.get() == 'yes':
                    add0.configure(text='Breakfast and Lunch')
                else:
                    add1.configure(text='None')

                total = CTkFrame(show_details_,corner_radius=20)
                total.place(relx = 0.79,rely = 0.77, anchor=CENTER)
                titl = CTkLabel(total,text ='Total:',font=('HP Simplified',19,'bold'))
                titl.place(relx=0.5,rely=0.5,anchor = CENTER)










                def back_misc():
                    show_details_.destroy()
                    details_back.destroy()
                    proceed.destroy()

                details_back = CTkButton(booking_,height=100,width=100,text='← Back', font=('HP Simplified',17), command=lambda:back_misc())
                details_back.place(relx=0.15,rely=0.5,anchor = CENTER)

                def book():
                    pass

                proceed = CTkButton(booking_,height=100,width=100,text='Book', font=('HP Simplified',17), command=lambda:book() if loggedin[0] is True else showsignin())
                proceed.place(relx=0.85,rely=0.5,anchor = CENTER)

            misc_next = CTkButton(booking_,height=100,width=100,text='Done →', font=('HP Simplified',17), command=lambda:show_details())
            misc_next.place(relx=0.85,rely=0.5,anchor = CENTER)
        
    def room_unavailable():
        req = CTkFrame(root, width=1440, height=720)
        req.place(relx = 0.5,rely = 0.5, anchor=CENTER)

        bottompic2 = CTkImage(Image.open('assets/loginbg.png'),size = (1440,720))
        bpic2 = CTkLabel(req,text = '', image = bottompic2)
        bpic2._image = bottompic2
        bpic2.place(relx=0.5,rely=0.5,anchor = CENTER)

        signupreq = CTkFrame(req,height=620,width=540,corner_radius=20)
        signupreq.place(relx = 0.5,rely = 0.5, anchor=CENTER)

        CTkLabel(signupreq,corner_radius=20,text='Room Unavailable',font=('HP Simplified',25,'bold')).place(relx=0.5,rely=0.5,anchor = CENTER)

        root.after(2000,lambda:req.destroy())

    def showsignin():
        req = CTkFrame(root, width=1440, height=720)
        req.place(relx = 0.5,rely = 0.5, anchor=CENTER)

        bottompic2 = CTkImage(Image.open('assets/loginbg.png'),size = (1440,720))
        bpic2 = CTkLabel(req,text = '', image = bottompic2)
        bpic2._image = bottompic2
        bpic2.place(relx=0.5,rely=0.5,anchor = CENTER)

        signupreq = CTkFrame(req,height=620,width=540,corner_radius=20)
        signupreq.place(relx = 0.5,rely = 0.5, anchor=CENTER)

        CTkLabel(signupreq,corner_radius=20,text='Please Log In',font=('HP Simplified',25,'bold')).place(relx=0.5,rely=0.5,anchor = CENTER)

        root.after(2000,lambda:req.destroy())        

    tabview.set("Book")
    root.mainloop()

def call_mainapp(main):
	main.destroy()
	mainapp()

if __name__ == '__main__':
    #set_appearance_mode('light')
    set_default_color_theme('green')

    loggedin = [False]
    login_details = []
    room_details = []
    booking_details = []

    today = dt.today().strftime('%Y-%m-%d')
    
    sqlcon = msconn.connect(host = 'localhost', user = 'root', passwd = 'samy', database = 'hotel0')
    #main()
    mainapp()
    sqlcon.close()