from CTkTable import CTkTable
from customtkinter import CTkButton,CTk,CTkProgressBar,CTkImage,CTkEntry,CTkLabel,CTkFrame,StringVar,CTkCheckBox,CTkTabview,CTkScrollableFrame,CTkComboBox,CENTER,DISABLED,set_default_color_theme,set_appearance_mode
from PIL import Image
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

    def logout():
            def logged_out():
                progressbar.stop()
                CTkLabel(logout_,height=620,width=540,corner_radius=20,text='Logged Out Successfully!',font=('HP Simplified',25,'bold')).place(relx=0.5,rely=0.5,anchor = CENTER)
                tabview.set("About")
                root.after(2000,lambda:frame_logout.destroy())

            loggedin[0] = False
            login_details.clear()
            button_login.configure(text='Log In',image=None)
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

    def loggin():
        cur0 = sqlcon.cursor()

        cur0.execute('select cust_email from credentials')
        edata = cur0.fetchall()
        emails = []
        for i in edata:
            emails.append(i[0])

        def save_signin():
            def logged_in(progress):
                progress.stop()
                cur0.close()
                CTkLabel(signin_,height=620,width=540,corner_radius=20,text='Signed In Successfully!',font=('HP Simplified',25,'bold')).place(relx=0.5,rely=0.5,anchor = CENTER)
                tabview.set("About")
                update_logbutton()
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
                cur0.execute('insert into credentials(cust_name,cust_email,cust_pass) values("%s","%s","%s")'%(name,email,passw))
                sqlcon.commit()
                cur0.execute('select cust_id from credentials where cust_email = "%s"'%(email))
                custid = cur0.fetchall()[0]
                loggedin[0] = True
                login_details.insert(0,email)
                login_details.insert(0,name)
                login_details.insert(0,custid)

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
                CTkLabel(logoin_,height=620,width=540,corner_radius=20,text='Logged In Successfully!',font=('HP Simplified',25,'bold')).place(relx=0.5,rely=0.5,anchor = CENTER)
                tabview.set("About")
                update_logbutton()
                root.after(2000,lambda:frame_login.destroy())

            lmisc = CTkLabel(login,text='',text_color='red',width=500)
            lmisc.place(relx = 0.5,y = 444,anchor = CENTER)

            password = ''
            email = enter_email.get()
            if email == '':
                lmisc.configure(text='Enter Email.!',width = 500)
            else:
                cur0.execute('select cust_pass from credentials where cust_email = "%s"'%(email,))
                password = cur0.fetchall()
                if password == []:
                    lmisc.configure(text='Incorrect Email or Password',width = 500)

            passw = enter_passw.get()
            if passw == '':
                lmisc.configure(text='Enter Password.!',width = 500)
            else:
                if passw == password[0][0]:
                    cur0.execute('select * from credentials where cust_email = "%s"'%(email))
                    data = cur0.fetchall()[0]
                    loggedin[0] = True
                    login_details.insert(0,email)
                    login_details.insert(0,data[1])
                    login_details.insert(0,data[0])

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

    #main app
    cur = sqlcon.cursor()

    frame = CTkFrame(root,height=720,width=1440,corner_radius=15)
    frame.place(relx = 0.5,rely = 0.5, anchor=CENTER)

    banner_pic = CTkImage(Image.open('assets/banner2.png'),size = (1440,120))
    topbanner = CTkLabel(frame,text = '', image = banner_pic)
    topbanner._image = banner_pic
    topbanner.place(relx=0.5,rely=0.086,anchor = CENTER)

    button_login = CTkButton(frame,width=70,height=70,text='Log In',command=lambda:loggin())
    button_login.place(relx=0.97,rely=0.065,anchor=CENTER)
    
    #tabs
    tabview = CTkTabview(frame,width=1440,height=630)
    tabview.place(relx=0.5,rely=0.56,anchor=CENTER)

    #about tab
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

    #rooms tab
    room = tabview.add("Our Rooms")
    
    cur.execute('select * from rooms')
    room_data = cur.fetchall()

    filters = CTkFrame(room,height=100,width=1420)
    filters.pack()

    fil = ['All','no','no','no','no']

    def filter_all():
        cur2 = sqlcon.cursor()
        #pb = CTkProgressBar(filters,mode='indeterminate',width=140,height=28)
        #pb.place(relx = 0.775,rely = 0.25, anchor=CENTER)
        #pb.start()
        if fil[0] == 'All':
            cur2.execute('select * from rooms where  availability = "%s" and wifi = "%s" and tv = "%s" and ac = "%s"'%(fil[1],fil[2],fil[3],fil[4]))
            fil_data = cur2.fetchall()
        else:
            cur2.execute('select * from rooms where type = "%s" and availability = "%s" and wifi = "%s" and tv = "%s" and ac = "%s"'%(fil[0],fil[1],fil[2],fil[3],fil[4]))
            fil_data = cur2.fetchall()
        
        #filters.after(2000,pb.destroy())
        table.configure(row=len(fil_data), column=7, values=fil_data)
        cur2.close()

    def filter_clear():
        table.configure(row=64, column=7, values=room_data)

    def tableclick(cell):
        column = cell['column']
        if column == 7:
            row = cell['row']
            roomno.insert(0,table.get()[row][0])
            tabview.set("Book a Room")
            
    def combobox_callback(choice):
        fil[0] = choice
    combobox = CTkComboBox(filters, font=('HP Simplified',13),values=['All', 'Single','Double','Triple','Quad'],
                                        command=combobox_callback)
    combobox.place(relx = 0.08,rely = 0.25, anchor=CENTER)
    combobox.set('All')

    check_var_avai = StringVar()
    def checkbox_avai_event():
        fil[1] = check_var_avai.get()
    checkbox_avai = CTkCheckBox(filters, font=('HP Simplified',13), text='Availability', command=checkbox_avai_event,
                                        variable=check_var_avai, onvalue='yes', offvalue='no')
    checkbox_avai.place(relx = 0.22,rely = 0.25, anchor=CENTER)
    
    check_var_wifi = StringVar()
    def checkbox_wifi_event():
        fil[2] = check_var_wifi.get()
    checkbox_wifi = CTkCheckBox(filters, font=('HP Simplified',13), text='WiFi', command=checkbox_wifi_event,
                                        variable=check_var_wifi, onvalue='yes', offvalue='no')
    checkbox_wifi.place(relx = 0.36,rely = 0.25, anchor=CENTER)

    check_var_tv = StringVar()
    def checkbox_tv_event():
        fil[3] = check_var_tv.get()
    checkbox_tv = CTkCheckBox(filters, font=('HP Simplified',13), text='TV', command=checkbox_tv_event,
                                        variable=check_var_tv, onvalue='yes', offvalue='no')
    checkbox_tv.place(relx = 0.5,rely = 0.25, anchor=CENTER)

    check_var_ac = StringVar()
    def checkbox_event_ac():
        fil[4] = check_var_ac.get()
    checkbox_ac = CTkCheckBox(filters, font=('HP Simplified',13), text='AC', command=checkbox_event_ac,
                                        variable=check_var_ac, onvalue='yes', offvalue='no')
    checkbox_ac.place(relx = 0.635,rely = 0.25, anchor=CENTER)

    button_filter = CTkButton(filters, font=('HP Simplified',13),text='Filter',command=lambda:filter_all())
    button_filter.place(relx = 0.775,rely = 0.25, anchor=CENTER)

    button_clear = CTkButton(filters, font=('HP Simplified',13),text='Clear Filters',command=lambda:filter_clear())
    button_clear.place(relx = 0.915,rely = 0.25, anchor=CENTER)

    button0 = CTkButton(filters,text='Sl.No.', font=('HP Simplified',13),width=250,corner_radius=0,state=DISABLED,text_color_disabled='white')
    button0.place(relx = 0.08,rely = 0.75, anchor=CENTER)
    button1 = CTkButton(filters,text='Availability', font=('HP Simplified',13),width=250,corner_radius=0,state=DISABLED,text_color_disabled='white')
    button1.place(relx = 0.2,rely = 0.75, anchor=CENTER)
    button2 = CTkButton(filters,text='Type', font=('HP Simplified',13),width=250,corner_radius=0,state=DISABLED,text_color_disabled='white')
    button2.place(relx = 0.31,rely = 0.75, anchor=CENTER)
    button3 = CTkButton(filters,text='WiFi', font=('HP Simplified',13),width=250,corner_radius=0,state=DISABLED,text_color_disabled='white')
    button3.place(relx = 0.435,rely = 0.75, anchor=CENTER)
    button4 = CTkButton(filters,text='TV', font=('HP Simplified',13),width=250,corner_radius=0,state=DISABLED,text_color_disabled='white')
    button4.place(relx = 0.555,rely = 0.75, anchor=CENTER)
    button5 = CTkButton(filters,text='AC', font=('HP Simplified',13),width=250,corner_radius=0,state=DISABLED,text_color_disabled='white')
    button5.place(relx = 0.675,rely = 0.75, anchor=CENTER)
    button6 = CTkButton(filters,text='Price', font=('HP Simplified',13),width=250,corner_radius=0,state=DISABLED,text_color_disabled='white')
    button6.place(relx = 0.79,rely = 0.75, anchor=CENTER)
    button7 = CTkButton(filters,text='Book', font=('HP Simplified',13),width=250,corner_radius=0,state=DISABLED,text_color_disabled='white')
    button7.place(relx = 0.915,rely = 0.75, anchor=CENTER)

    room_scrollframe = CTkScrollableFrame(room, width=1400, height=470)
    room_scrollframe.pack()

    table = CTkTable(room_scrollframe, font=('HP Simplified',13),height=40, row=64, column=8, hover_color= '#575757', values=room_data,command=tableclick)
    table.pack(expand=False, fill='both', padx=20)

    #contacs tab
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

    #pricing tab
    pricing = tabview.add("Pricings")

    def price_book(type):
        print(type)
        


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

    #booking tab
    book = tabview.add("Book a Room")
    dates = CTkFrame(book,height=100,width=1420)
    dates.pack()
    
    date_checkin = CTkEntry(dates,placeholder_text = 'Check In Date',height=45,width=300)
    date_checkin.pack(padx=20,pady=20)#place(relx=0.5,rely=0.85,anchor=CENTER)
    
    date_checkout = CTkEntry(dates,placeholder_text = 'Check Out Date',height=45,width=300)
    date_checkout.pack(padx=20,pady=20)#place(relx=0.5,rely=0.85,anchor=CENTER)







    tabview.set("Book a Room")
    cur.close()
    root.mainloop()

def call_mainapp(main):
	main.destroy()
	mainapp()

if __name__ == '__main__':
    set_appearance_mode('system')
    set_default_color_theme('green')

    loggedin = [False]
    login_details = []
    roomno = []
    
    sqlcon = msconn.connect(host = 'localhost', user = 'root', passwd = 'root', database = 'hotel')
    #main()
    mainapp()
    sqlcon.close()