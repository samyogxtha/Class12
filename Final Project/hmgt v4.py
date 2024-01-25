from customtkinter import *
from tkcalendar import Calendar
from PIL import Image
from datetime import datetime as dt
import mysql.connector as msconn

def mainapp():
    root = CTk()
    root.title("Mavrik Hotel Booking")
    root.minsize(height = 720,width = 1280)

    #------------------FUNCTION-FOR-LOGGING-OUT------------------
    def logout():
        loggedin[0] = False
        login_details.clear()

        frame_logout = CTkFrame(root,height = 720,width = 1280)
        frame_logout.place(relheight = 1, relwidth = 1, relx = 0.5,rely = 0.5,anchor = CENTER)

        bottompic2 = CTkImage(Image.open('assets/loginbg.png'),size = (1920,1080))
        bpic2 = CTkLabel(frame_logout,text = '', image = bottompic2)
        bpic2._image = bottompic2
        bpic2.place(relx = 0.5,rely = 0.5,anchor = CENTER)

        logout_ = CTkFrame(frame_logout,height = 620,width = 540,corner_radius=20)
        logout_.place(relx = 0.5,rely = 0.5, anchor = CENTER)

        progressbar = CTkProgressBar(logout_,height = 50,mode="indeterminate")
        progressbar.place(relx = 0.5,rely = 0.5, anchor = CENTER)
        CTkLabel(logout_,text = 'Logging Out...',font = ('HP Simplified',20,'bold')).place(relx = 0.5,rely = 0.6,anchor = CENTER)
        progressbar.start()
        
        def logged_out():
            progressbar.stop()
            CTkLabel(logout_,height = 200,text = 'Logged Out Successfully!',font = ('HP Simplified',25,'bold')).place(relx = 0.5,rely = 0.5,anchor = CENTER)
            tabview.set("About")
            update_logbutton()
            root.after(2000,lambda:frame_logout.destroy())

        root.after(3000,lambda:logged_out())

    #------------------FUNCTION-FOR-LOGGING-AND-SIGNING-IN------------------
    def loggin():
        cur0 = sqlcon.cursor()
        cur0.execute('select email from customers')
        edata = cur0.fetchall()
        emails = []
        for i in edata:
            emails.append(i[0])

        main_pic = CTkImage(Image.open('assets/logo.png'),size = (200,200))
        bottompic1 = CTkImage(Image.open('assets/loginbg.png'),size = (1920,1080))

        frame_login = CTkFrame(root,height = 720,width = 1280)
        frame_login.place(relheight = 1, relwidth = 1, relx = 0.5,rely = 0.5, anchor = CENTER)
        
        bpic1 = CTkLabel(frame_login,text = '', image = bottompic1)
        bpic1._image = bottompic1
        bpic1.place(relx = 0.5,rely = 0.5,anchor = CENTER)
        
        #signup page
        signup = CTkFrame(frame_login,height = 620,width = 540,corner_radius=20)
        signup.place(relx = 0.5,rely = 0.5, anchor = CENTER)
        login_pic = CTkLabel(signup,text = '', image = main_pic)
        login_pic._image = main_pic
        login_pic.place(relx = 0.5,rely = 0.21,anchor = CENTER)

        def save_signin():
            misc = CTkLabel(signup,text = '',text_color = 'red',width = 500)
            misc.place(relx = 0.5,y = 444,anchor = CENTER)

            at = dot = up = no = spl = False
            
            email = entry_email.get()
            if email == '':
                misc.configure(text = 'Enter Email.!',width = 500)
            elif email in emails:
                misc.configure(text = 'Email already registered',width = 500)
            else:
                if '@' in email:
                    at = True
                if '.' in email:
                    dot = True
                if at is False or dot is False:
                    misc.configure(text = 'Enter Valid Email Id.',width = 500)

            passw = entry_passw.get()
            if passw == '':
                misc.configure(text = 'Enter Password.!',width = 500)
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
                    misc.configure(text = 'Your Password must have atleast one Special character.',width = 500)
                if no == False:
                    misc.configure(text = 'Your Password must have atleast one Number.',width = 500)
                if up == False:
                    misc.configure(text = 'Your Password must have atleast one Upper case character.',width = 500)
                if len(passw)<8:
                    misc.configure(text = 'The Password must have atleast 8 Characters.',width = 500)

            name = entry_name.get()
            if name == '':
                misc.configure(text = 'Enter Name.!',width = 500)
            
            if misc._text == '':
                cur0.execute('insert into customers(name,email,pass) values("%s","%s","%s")'%(name,email,passw))
                sqlcon.commit()
                cur0.execute('select * from customers where email = "%s"'%(email))
                data = cur0.fetchall()[0]
                loggedin[0] = True
                login_details.clear()
                login_details.insert(0,list(data))

                signin_ = CTkFrame(frame_login,height = 620,width = 540,corner_radius=20)
                signin_.place(relx = 0.5,rely = 0.5, anchor = CENTER)

                progressbar = CTkProgressBar(signin_,height = 50,mode="indeterminate")
                progressbar.place(relx = 0.5,rely = 0.5, anchor = CENTER)
                CTkLabel(signin_,text = 'Signing In...',font = ('HP Simplified',20,'bold')).place(relx = 0.5,rely = 0.6,anchor = CENTER)
                progressbar.start()

                def logged_in(progress):
                    progress.stop()
                    cur0.close()
                    sqlcon.commit()
                    CTkLabel(signin_,height = 620,width = 540,corner_radius=20,text = 'Signed In Successfully!',font = ('HP Simplified',25,'bold')).place(relx = 0.5,rely = 0.5,anchor = CENTER)
                    update_logbutton()
                    root.after(2000,lambda:frame_login.destroy())

                root.after(3000,lambda:logged_in(progressbar))
        
        CTkButton(signup,text = '←',height = 50,width = 50,corner_radius=30,fg_color = 'transparent', hover_color = '#333333', command=lambda:frame_login.destroy()).place(x = 1,y = 1)
        entry_name = CTkEntry(signup,placeholder_text = 'Name',height = 45,width = 300)
        entry_name.place(relx = 0.5,y = 290, anchor = CENTER)
        entry_email = CTkEntry(signup,placeholder_text = 'Email',height = 45,width = 300)
        entry_email.place(relx = 0.5,y = 349,anchor = CENTER)
        entry_passw = CTkEntry(signup,placeholder_text = 'Password',height = 45,width = 300)
        entry_passw.place(relx = 0.5,y = 409,anchor = CENTER)
        CTkLabel(signup,text = 'Already have an account?',).place(relx = 0.37,y = 470,anchor = CENTER)
        login_ = CTkLabel(signup,text = 'Log In', text_color = '#44f1a6')
        login_.place(relx = 0.73,y = 470,anchor = CENTER)
        login_.bind("<Button-1>", lambda x:login.tkraise())
        button_signup = CTkButton(signup,text = 'Sign Up',width = 300,height = 45,command = lambda: save_signin())
        button_signup.place(relx = 0.5,y = 518,anchor = CENTER)

        #login page
        login = CTkFrame(frame_login,height = 620,width = 540,corner_radius=20)
        login.place(relx = 0.5,rely = 0.5, anchor = CENTER)
        signin_pic = CTkLabel(login,text = '', image = main_pic)
        signin_pic._image = main_pic
        signin_pic.place(relx = 0.5,rely = 0.21,anchor = CENTER)

        def save_login():
            lmisc = CTkLabel(login,text = '',text_color = 'red',width = 500)
            lmisc.place(relx = 0.5,y = 444,anchor = CENTER)

            password = []
            email = enter_email.get()
            if email == '':
                lmisc.configure(text = 'Enter Email.!',width = 500)
            else:
                cur0.execute('select pass from customers where email = "%s"'%(email,))
                password.insert(0,cur0.fetchall())
                if password[0] == []:
                    lmisc.configure(text = 'Incorrect Email or Password',width = 500)

            passw = enter_passw.get()
            if passw == '':
                lmisc.configure(text = 'Enter Password.!',width = 500)
            elif password[0] == []:
                lmisc.configure(text = 'Incorrect Email or Password',width = 500)
            else:
                if passw == password[0][0][0]:
                    cur0.execute('select * from customers where email = "%s"'%(email))
                    data = cur0.fetchall()[0]
                    loggedin[0] = True
                    login_details.clear()
                    login_details.insert(0,list(data))

                    logoin_ = CTkFrame(frame_login,height = 620,width = 540,corner_radius=20)
                    logoin_.place(relx = 0.5,rely = 0.5, anchor = CENTER)

                    progressbar = CTkProgressBar(logoin_,height = 50,mode="indeterminate")
                    progressbar.place(relx = 0.5,rely = 0.5, anchor = CENTER)
                    CTkLabel(logoin_,text = 'Logging In...',font = ('HP Simplified',20,'bold')).place(relx = 0.5,rely = 0.6,anchor = CENTER)
                    progressbar.start()

                    def logged_in(progress):
                        progress.stop()
                        cur0.close()
                        CTkLabel(logoin_,height = 200,corner_radius=20,text = 'Logged In Successfully!',font = ('HP Simplified',25,'bold')).place(relx = 0.5,rely = 0.5,anchor = CENTER)
                        update_logbutton()
                        root.after(2000,lambda:frame_login.destroy())

                    root.after(3000,lambda:logged_in(progressbar))
                else:
                    lmisc.configure(text = 'Incorrect Email or Password',width = 500)
        
        CTkButton(login,text = '←',height = 50,width = 50,corner_radius=30,fg_color = 'transparent', hover_color = '#333333', command=lambda:frame_login.destroy()).place(x = 1,y = 1)
        enter_email = CTkEntry(login,placeholder_text = 'Email',height = 45,width = 300)
        enter_email.place(relx = 0.5,y = 332,anchor = CENTER)
        enter_passw = CTkEntry(login,placeholder_text = 'Password',height = 45,width = 300)
        enter_passw.place(relx = 0.5,y = 409,anchor = CENTER)
        CTkLabel(login,text = 'Don\'t have an account?',).place(relx = 0.35,y = 470,anchor = CENTER)
        signup_ = CTkLabel(login,text = 'Sign Up', text_color = '#44f1a6')
        signup_.place(relx = 0.728,y = 470,anchor = CENTER)
        signup_.bind("<Button-1>", lambda x:signup.tkraise())
        button_login = CTkButton(login,text = 'Log In',width = 300,height = 45,command=lambda: save_login())
        button_login.place(relx = 0.5,y = 518,anchor = CENTER)

    def update_logbutton():
        if loggedin[0] is True:
            profile_pic = CTkImage(Image.open('assets/logout.png'),size = (58,58))
            button_login.configure(text = '',command=lambda:logout(),image=profile_pic)
        elif loggedin[0] is False:
            button_login.configure(text = '',command=lambda:loggin(),image=profile_pic0)
  
    #main app
    frame = CTkFrame(root,height = 720,width = 1280,corner_radius=15)
    frame.place(relheight = 1, relwidth = 1, relx = 0.5,rely = 0.5, anchor = CENTER)
    
    backdrop = CTkImage(Image.open('assets/utbg0.jpg'),size = (1920,1080)) 

    #------------------TOP-BANNER------------------
    banner_pic = CTkImage(Image.open('assets/banner150.jpg'),size = (1920,150))
    topbanner = CTkLabel(frame,text = '', image = banner_pic)
    topbanner._image = banner_pic
    topbanner.place(relx = 0.5,rely = 0.086,anchor = CENTER)

    def resize_images(event):
        new_width = event.width
        new_height = (event.height)-600

        print(event.height,event.width)
        print(new_height,new_width)

        banner_pic_copy = CTkImage(Image.open('assets/banner150.jpg'), size = (1920, 150))

        topbanner.configure(image = banner_pic_copy)

    #frame.bind('<Configure>', resize_images)

    profile_pic0 = CTkImage(Image.open('assets/login.jpg'),size = (58,58))
    button_login = CTkButton(frame,width = 70,height = 70,text = '',image=profile_pic0,command=lambda:loggin())
    button_login._image = profile_pic0
    button_login.place(relx = 0.97,rely = 0.058,anchor = CENTER)
    
    #------------------CREATE-TABS------------------
    tabview = CTkTabview(frame,width = 1280,height = 630)
    tabview.place(relheight = 0.9, relwidth = 1, relx = 0.5,rely = 0.56,anchor = CENTER)

    #------------------ABOUT-TAB------------------
    about = tabview.add("About")
    
    pic = CTkScrollableFrame(about,height = 630,width = 1280,corner_radius=15)
    pic.place(relheight = 1, relwidth = 1, x = 0,y = 0)

    #image_files = ['assets/image0.jpg','assets/image1.jpg', 'assets/image2.jpg', 'assets/image3.jpg','assets/image4.jpg','assets/image5.jpg']
    image_files = ['assets/img0.jpg','assets/img1.jpg', 'assets/img2.jpg', 'assets/img3.jpg','assets/img4.jpg','assets/img5.jpg','assets/img6.jpg']
    images = []

    def load_images():
        for file in image_files:
            image = CTkImage(Image.open(file),size=(1280,740))
            images.append(image)
        canvas.configure(image=images[0])

    canvas = CTkLabel(pic, text = '', width = 1280, height = 740)
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

    backdrop1 = CTkLabel(contact,text = '', image=backdrop)
    backdrop1._image = backdrop
    backdrop1.place(relx = 0.5,rely = 0.5, anchor = CENTER)

    fr_mgr = CTkFrame(contact,height = 275,width = 680,corner_radius=15)
    fr_mgr.place(relx = 0.25,rely = 0.25, anchor = CENTER)

    mgr_pic = CTkImage(Image.open('assets/mgr.jpg'),size = (275,275))
    mgr = CTkLabel(fr_mgr,text = '', image = mgr_pic)
    mgr._image = mgr_pic
    mgr.place(x = 137.5,rely = 0.5,anchor = CENTER)

    CTkLabel(fr_mgr,text = "Manager",font = ('HP Simplified',47,'bold')).place(x = 290,y = 60)
    CTkLabel(fr_mgr,text = "Mr. Gru",font = ('HP Simplified',32,'bold')).place(x = 290,y = 109)
    CTkLabel(fr_mgr,text = "Extention : 117",font = ('HP Simplified',27)).place(x = 290,y = 150)
    CTkLabel(fr_mgr,text = "Mail : manager@mavrik.com",font = ('HP Simplified',27)).place(x = 290,y = 185)

    fr_rec = CTkFrame(contact,height = 275,width = 680,corner_radius=15)
    fr_rec.place(relx = 0.75,rely = 0.25, anchor = CENTER)

    rec_pic = CTkImage(Image.open('assets/rec.jpg'),size = (275,275))
    rec = CTkLabel(fr_rec,text = '', image = rec_pic)
    rec._image = rec_pic
    rec.place(x = 137.5,rely = 0.5,anchor = CENTER)

    CTkLabel(fr_rec,text = "Customer Service",font = ('HP Simplified',47,'bold')).place(x = 290,y = 60)
    CTkLabel(fr_rec,text = "Mr. Sam",font = ('HP Simplified',32,'bold')).place(x = 290,y = 109)
    CTkLabel(fr_rec,text = "Extention : 225",font = ('HP Simplified',27)).place(x = 290,y = 150)
    CTkLabel(fr_rec,text = "Mail : customerservice@mavrik.com",font = ('HP Simplified',27)).place(x = 290,y = 185)
    
    fr_serv = CTkFrame(contact,height = 275,width = 680,corner_radius=15)
    fr_serv.place(relx = 0.25,rely = 0.75, anchor = CENTER)

    serv_pic = CTkImage(Image.open('assets/serv.jpg'),size = (275,275))
    serv = CTkLabel(fr_serv,text = '', image = serv_pic)
    serv._image = serv_pic
    serv.place(x = 137.5,rely = 0.5,anchor = CENTER)

    CTkLabel(fr_serv,text = "Room Service",font = ('HP Simplified',47,'bold')).place(x = 290,y = 60)
    CTkLabel(fr_serv,text = "Ms. Anya",font = ('HP Simplified',32,'bold')).place(x = 290,y = 109)
    CTkLabel(fr_serv,text = "Extention : 147",font = ('HP Simplified',27)).place(x = 290,y = 150)
    CTkLabel(fr_serv,text = "Mail : roomservice@mavrik.com",font = ('HP Simplified',27)).place(x = 290,y = 185)

    fr_cook = CTkFrame(contact,height = 275,width = 680,corner_radius=15)
    fr_cook.place(relx = 0.75,rely = 0.75, anchor = CENTER)

    cook_pic = CTkImage(Image.open('assets/cook.jpg'),size = (275,275))
    cook = CTkLabel(fr_cook,text = '', image = cook_pic)
    cook._image = cook_pic
    cook.place(x = 137.5,rely = 0.5,anchor = CENTER)

    CTkLabel(fr_cook,text = "Restaurant",font = ('HP Simplified',47,'bold')).place(x = 290,y = 60)
    CTkLabel(fr_cook,text = "Mr. Kim",font = ('HP Simplified',32,'bold')).place(x = 290,y = 109)
    CTkLabel(fr_cook,text = "Extention : 125",font = ('HP Simplified',27)).place(x = 290,y = 150)
    CTkLabel(fr_cook,text = "Mail : dining@mavrik.com",font = ('HP Simplified',27)).place(x = 290,y = 185)

    #------------------PRICING-TAB------------------
    pricing = tabview.add("Rooms & Pricings")
    
    backdrop2 = CTkLabel(pricing,text = '', image=backdrop)
    backdrop2._image = backdrop
    backdrop2.place(relx = 0.5,rely = 0.5, anchor = CENTER)

    cur = sqlcon.cursor()
    cur.execute('select distinct type from rooms where availability = "yes"')
    rooms_avai_ = cur.fetchall()
    rooms_avai = []
    for i in rooms_avai_:
        rooms_avai.append(i[0])
    cur.close()
    rooms_unavai = ['Single','Double','Triple','Quad']
    for i in rooms_avai:
        if i in rooms_unavai:
            rooms_unavai.remove(i)

    price_type = ['None']
    def price_book(type):
        price_type[0] = type
        tabview.set('Book a Room')

    fr_single = CTkFrame(pricing,height = 275,width = 680,corner_radius=15)
    fr_single.place(relx = 0.25,rely = 0.25, anchor = CENTER)

    single_pic = CTkImage(Image.open('assets/single.jpg'),size = (275,275))
    single = CTkLabel(fr_single,text = '', image = single_pic)
    single._image = single_pic
    single.place(x = 137.5,rely = 0.5,anchor = CENTER)

    CTkLabel(fr_single,text = "Single Room",font = ('HP Simplified',47,'bold')).place(x = 290,y = 45)
    CTkLabel(fr_single,text = "$40 per night",font = ('HP Simplified',27)).place(x = 300,y = 100)
    CTkLabel(fr_single,text = "Luxurious hotel room with a king-size bed,",font = ('HP Simplified',20)).place(x = 300,y = 135)
    CTkLabel(fr_single,text = "modern amenities, city view, plush decor,",font = ('HP Simplified',20)).place(x = 300,y = 160)
    CTkLabel(fr_single,text = "and a spacious marble bathroom.",font = ('HP Simplified',20)).place(x = 300,y = 185)
    button1 = CTkButton(fr_single,text = 'Book',height = 50,width = 80, command=lambda:price_book('Single'))
    button1.place(relx = 0.92,rely = 0.85,anchor = CENTER)

    fr_double = CTkFrame(pricing,height = 275,width = 680,corner_radius=15)
    fr_double.place(relx = 0.75,rely = 0.25, anchor = CENTER)

    double_pic = CTkImage(Image.open('assets/double.jpg'),size = (275,275))
    double = CTkLabel(fr_double,text = '', image = double_pic)
    double._image = double_pic
    double.place(x = 137.5,rely = 0.5,anchor = CENTER)

    CTkLabel(fr_double,text = "Double Room",font = ('HP Simplified',47,'bold')).place(x = 290,y = 45)
    CTkLabel(fr_double,text = "$50 per night",font = ('HP Simplified',27)).place(x = 300,y = 100)
    CTkLabel(fr_double,text = "Elegant double room with twin beds,",font = ('HP Simplified',20)).place(x = 300,y = 135)
    CTkLabel(fr_double,text = "furnishings, en-suite bathroom, and serene",font = ('HP Simplified',20)).place(x = 300,y = 160)
    CTkLabel(fr_double,text = "ambiance for a comfortable experience.",font = ('HP Simplified',20)).place(x = 300,y = 185)
    button2 = CTkButton(fr_double,text = 'Book',height = 50,width = 80, command=lambda:price_book('Double'))
    button2.place(relx = 0.92,rely = 0.85,anchor = CENTER)
    
    fr_triple = CTkFrame(pricing,height = 275,width = 680,corner_radius=15)
    fr_triple.place(relx = 0.25,rely = 0.75, anchor = CENTER)

    triple_pic = CTkImage(Image.open('assets/triple.jpg'),size = (275,275))
    triple = CTkLabel(fr_triple,text = '', image = triple_pic)
    triple._image = triple_pic
    triple.place(x = 137.5,rely = 0.5,anchor = CENTER)

    CTkLabel(fr_triple,text = "Triple Room",font = ('HP Simplified',47,'bold')).place(x = 290,y = 45)
    CTkLabel(fr_triple,text = "$60 per night",font = ('HP Simplified',27)).place(x = 300,y = 100)
    CTkLabel(fr_triple,text = "Spacious triple room, three cozy beds,",font = ('HP Simplified',20)).place(x = 300,y = 135)
    CTkLabel(fr_triple,text = "contemporary, design, ample storage, ideal",font = ('HP Simplified',20)).place(x = 300,y = 160)
    CTkLabel(fr_triple,text = "for friends or small families.",font = ('HP Simplified',20)).place(x = 300,y = 185)
    button3 = CTkButton(fr_triple,text = 'Book',height = 50,width = 80, command=lambda:price_book('Triple'))
    button3.place(relx = 0.92,rely = 0.85,anchor = CENTER)

    fr_quad = CTkFrame(pricing,height = 275,width = 680,corner_radius=15)
    fr_quad.place(relx = 0.75,rely = 0.75, anchor = CENTER)

    quad_pic = CTkImage(Image.open('assets/quad.jpg'),size = (275,275))
    quad = CTkLabel(fr_quad,text = '', image = quad_pic)
    quad._image = quad_pic
    quad.place(x = 137.5,rely = 0.5,anchor = CENTER)

    CTkLabel(fr_quad,text = "Quad Room",font = ('HP Simplified',47,'bold')).place(x = 290,y = 45)
    CTkLabel(fr_quad,text = "$70 per night",font = ('HP Simplified',27)).place(x = 300,y = 100)
    CTkLabel(fr_quad,text = "Modern quad room designed for groups,",font = ('Dubai',20)).place(x = 300,y = 135)
    CTkLabel(fr_quad,text = "offering four beds, stylish decor and homelike",font = ('HP Simplified',20)).place(x = 300,y = 160)
    CTkLabel(fr_quad,text = "atmosphere for shared experiences.",font = ('HP Simplified',20)).place(x = 300,y = 185)
    button4 = CTkButton(fr_quad,text = 'Book',height = 50,width = 80, command=lambda:price_book('Quad'))
    button4.place(relx = 0.92,rely = 0.85,anchor = CENTER)

    for r in rooms_unavai:
        if r == 'Single':
            button1.configure(text = 'Booked', state = DISABLED)
        if r == 'Double':
            button2.configure(text = 'Booked', state = DISABLED)
        if r == 'Triple':
            button3.configure(text = 'Booked', state = DISABLED)
        if r == 'Quad':
            button4.configure(text = 'Booked', state = DISABLED)

    #-----------------------------NEW-BOOKING-TAB---------------------------------
    booking_ = tabview.add("Book a Room")

    backdrop3 = CTkLabel(booking_,text = '', image=backdrop)
    backdrop3._image = backdrop
    backdrop3.place(relx = 0.5,rely = 0.5, anchor = CENTER)

    select_date_ = CTkFrame(booking_,height = 540,width = 540,corner_radius=20)
    select_date_.place(relx = 0.5,rely = 0.5, anchor = CENTER)

    def select_datein():
        fr_indate = CTkFrame(booking_,height = 250,width = 200)
        fr_indate.place(relx = 0.7,rely = 0.3, anchor = CENTER)

        tkc1 = Calendar(fr_indate,selectmode = "day",year = int(today[0:4]),month = int(today[6:7]),date=int(today[9:]))
        tkc1.pack(padx = 10,pady = 10)

        def fetch_date():
            checkin_date.configure(state='normal')
            fr_indate.destroy()
            checkin_date.delete(0,10)
            checkin_date.insert(0,tkc1.selection_get().strftime('%Y-%m-%d'))
            checkin_date.configure(state=DISABLED)

        button = CTkButton(fr_indate,text = "Select Date",command=fetch_date)
        button.pack(padx = 10,pady = 10)
        
    CTkLabel(select_date_,text = "Checkin Date (yyyy-mm-dd)*",font = ('HP Simplified',17)).place(relx = 0.5,rely = 0.4, anchor = CENTER)
    checkin_date = CTkEntry(select_date_,placeholder_text = 'Checkin Date*',height = 45,width = 300)
    checkin_date.place(relx = 0.5,rely = 0.3, anchor = CENTER)
    checkin_date.bind("<Button-1>", lambda x:select_datein())

    def select_dateout():
        fr_outdate = CTkFrame(booking_,height = 250,width = 200)
        fr_outdate.place(relx = 0.7,rely = 0.6, anchor = CENTER)

        tkc1 = Calendar(fr_outdate,selectmode = "day",year = int(today[0:4]),month = int(today[6:7]),date=int(today[9:]))
        tkc1.pack(padx = 10,pady = 10)

        def fetch_date():
            checkout_date.configure(state='normal')
            fr_outdate.destroy()
            checkout_date.delete(0,10)
            checkout_date.insert(0,tkc1.selection_get().strftime('%Y-%m-%d'))
            checkout_date.configure(state=DISABLED)

        button = CTkButton(fr_outdate,text = "Select Date",command=fetch_date)
        button.pack(padx = 10,pady = 10)

    CTkLabel(select_date_,text = "Checkout Date (yyyy-mm-dd)*",font = ('HP Simplified',17)).place(relx = 0.5,rely = 0.7, anchor = CENTER)
    checkout_date = CTkEntry(select_date_,placeholder_text = 'Checkout Date*',height = 45,width = 300)
    checkout_date.place(relx = 0.5,rely = 0.6, anchor = CENTER)
    checkout_date.bind("<Button-1>", lambda x:select_dateout())

    err_msg0 = CTkLabel(select_date_,text = '',text_color = 'red')
    err_msg0.place(relx = 0.5,rely = 0.95,anchor = CENTER)

    def next_sel():
        global diff
        now_diff = (dt.strptime(checkin_date.get(), "%Y-%m-%d") - dt.strptime(today, "%Y-%m-%d")).days
        if now_diff > -1:
            diff = (dt.strptime(checkout_date.get(), "%Y-%m-%d") - dt.strptime(checkin_date.get(), "%Y-%m-%d")).days
            if diff > 0:
                select_type()
            else:
                err_msg0.configure(text = 'Please Select a valid date range!')
        else:
            err_msg0.configure(text = 'Checkin date cannot be in the past')

    CTkButton(booking_,height = 100,width = 100,text = 'Next →', font = ('HP Simplified',17), command=lambda:next_sel() if checkin_date.get() != '' and checkout_date.get() != '' else err_msg0.configure(text = '*Please enter Date*')).place(relx = 0.85,rely = 0.5,anchor = CENTER)

    def select_type():
        select_type_ = CTkFrame(booking_,height = 540,width = 540,corner_radius=20)
        select_type_.place(relx = 0.5,rely = 0.5, anchor = CENTER)

        CTkLabel(select_type_,corner_radius=20,text = 'Please choose the type of room',font = ('HP Simplified',25,'bold')).place(relx = 0.5,y = 45,anchor = CENTER)

        radio_var = StringVar()

        radiobutton_1 = CTkRadioButton(select_type_, text = "Single", font = ('HP Simplified',13), variable= radio_var, value='Single')
        radiobutton_2 = CTkRadioButton(select_type_, text = "Double", font = ('HP Simplified',13), variable= radio_var, value='Double')
        radiobutton_3 = CTkRadioButton(select_type_, text = "Triple", font = ('HP Simplified',13), variable= radio_var, value='Triple')
        radiobutton_4 = CTkRadioButton(select_type_, text = "Quad", font = ('HP Simplified',13), variable= radio_var, value='Quad')

        radiobutton_1.place(relx = 0.25,rely = 0.5,anchor = CENTER)
        radiobutton_2.place(relx = 0.75,rely = 0.5,anchor = CENTER)
        radiobutton_3.place(relx = 0.25,rely = 0.9,anchor = CENTER)
        radiobutton_4.place(relx = 0.75,rely = 0.9,anchor = CENTER)

        pic1 = CTkImage(Image.open('assets/single.jpg'),size = (175,175))
        pic_1 = CTkLabel(select_type_,corner_radius=10,text = '', image = pic1)
        pic_1._image = pic1
        pic_1.place(relx = 0.25,rely = 0.3,anchor = CENTER)
        pic_1.bind("<Button-1>", lambda x:radiobutton_1.invoke())

        pic2 = CTkImage(Image.open('assets/double.jpg'),size = (175,175))
        pic_2 = CTkLabel(select_type_,text = '', image = pic2)
        pic_2._image = pic2
        pic_2.place(relx = 0.75,rely = 0.3,anchor = CENTER)
        pic_2.bind("<Button-1>", lambda x:radiobutton_2.invoke())

        pic3 = CTkImage(Image.open('assets/triple.jpg'),size = (175,175))
        pic_3 = CTkLabel(select_type_,text = '', image = pic3)
        pic_3._image = pic3
        pic_3.place(relx = 0.25,rely = 0.7,anchor = CENTER)
        pic_3.bind("<Button-1>", lambda x:radiobutton_3.invoke())

        pic4 = CTkImage(Image.open('assets/quad.jpg'),size = (175,175))
        pic_4 = CTkLabel(select_type_,text = '', image = pic4)
        pic_4._image = pic4
        pic_4.place(relx = 0.75,rely = 0.7,anchor = CENTER)
        pic_4.bind("<Button-1>", lambda x:radiobutton_4.invoke())

        for r in rooms_unavai:
            if r == 'Single':
                radiobutton_1.configure(state=DISABLED)
                pic1_ = CTkImage(Image.open('assets/singlebooked.jpg'),size = (175,175))
                pic_1.configure(image = pic1_)
            if r == 'Double':
                radiobutton_2.configure(state=DISABLED)
                pic2_ = CTkImage(Image.open('assets/doublebooked.jpg'),size = (175,175))
                pic_2.configure(image = pic2_)
            if r == 'Triple':
                radiobutton_3.configure(state=DISABLED)
                pic3_ = CTkImage(Image.open('assets/triplebooked.jpg'),size = (175,175))
                pic_3.configure(image = pic3_)
            if r == 'Quad':
                radiobutton_4.configure(state=DISABLED)
                pic4_ = CTkImage(Image.open('assets/quadbooked.jpg'),size = (175,175))
                pic_4.configure(image = pic4_)

        err_msg1 = CTkLabel(select_type_,text = '',text_color = 'red')
        err_msg1.place(relx = 0.5,rely = 0.95,anchor = CENTER)

        def back_date():
            next_misc_.destroy()
            back_date_.destroy()
            select_type_.destroy()

        back_date_ = CTkButton(booking_,height = 100,width = 100,text = '← Back', font = ('HP Simplified',17), command=lambda:back_date())
        back_date_.place(relx = 0.15,rely = 0.5,anchor = CENTER)

        if price_type[0] == 'None':
            pass
        elif price_type[0] == 'Single':
            radiobutton_1.invoke()
        elif price_type[0] == 'Double':
            radiobutton_2.invoke()
        elif price_type[0] == 'Triple':
            radiobutton_3.invoke()
        elif price_type[0] == 'Quad':
            radiobutton_4.invoke()
      
        def select_misc():
            select_misc_ = CTkFrame(booking_,height = 540,width = 540,corner_radius=20)
            select_misc_.place(relx = 0.5,rely = 0.5, anchor = CENTER)

            CTkLabel(select_misc_,corner_radius=20,text = 'Enhance your stay. Select add-ons and extras:',font = ('Dubai',25,'bold')).place(relx = 0.5,rely = 0.05,anchor = CENTER)
            
            fr_transfer = CTkFrame(select_misc_,corner_radius=20,height = 150,width = 520)
            fr_transfer.place(relx = 0.5,rely = 0.24,anchor = CENTER)
            transfer_img = CTkImage(Image.open('assets/car.jpg'),size = (150,150))
            transfer_img_ = CTkLabel(fr_transfer,text = '', image = transfer_img)
            transfer_img_._image = transfer_img
            transfer_img_.place(x = 75,rely = 0.5,anchor = CENTER)
            CTkLabel(fr_transfer,text = 'Airport Transfer', font = ('HP Simplified',30)).place(x = 265,rely = 0.4,anchor = CENTER)
            CTkLabel(fr_transfer,text = '$50 per unit', font = ('HP Simplified',15)).place(x = 210,rely = 0.6,anchor = CENTER)
            transfer_var = StringVar()
            checkbox_transfer = CTkCheckBox(fr_transfer,text = '',variable=transfer_var, onvalue='yes', offvalue='no')
            checkbox_transfer.place(relx = 0.95,rely = 0.5, anchor = CENTER)
            transfer_img_.bind("<Button-1>", lambda x:checkbox_transfer.toggle())
            fr_transfer.bind("<Button-1>", lambda x:checkbox_transfer.toggle())

            fr_tour = CTkFrame(select_misc_,corner_radius=20,height = 150,width = 520)
            fr_tour.place(relx = 0.5,rely = 0.54,anchor = CENTER)
            tour_img = CTkImage(Image.open('assets/tour.jpg'),size = (150,150))
            tour_img_ = CTkLabel(fr_tour,text = '', image = tour_img)
            tour_img_._image = tour_img
            tour_img_.place(x = 75,rely = 0.5,anchor = CENTER)
            CTkLabel(fr_tour,text = 'City Tour', font = ('HP Simplified',30)).place(x = 220,rely = 0.4,anchor = CENTER)
            CTkLabel(fr_tour,text = '$170 per night', font = ('HP Simplified',15)).place(x = 220,rely = 0.6,anchor = CENTER)
            tour_var = StringVar()
            checkbox_tour = CTkCheckBox(fr_tour,text = '',variable=tour_var, onvalue='yes', offvalue='no')
            checkbox_tour.place(relx = 0.95,rely = 0.5, anchor = CENTER)
            tour_img_.bind("<Button-1>", lambda x:checkbox_tour.toggle())
            fr_tour.bind("<Button-1>", lambda x:checkbox_tour.toggle())

            fr_feast = CTkFrame(select_misc_,corner_radius=20,height = 150,width = 520)
            fr_feast.place(relx = 0.5,rely = 0.84,anchor = CENTER)
            feast_img = CTkImage(Image.open('assets/feast.jpg'),size = (150,150))
            feast_img_ = CTkLabel(fr_feast,text = '', image = feast_img)
            feast_img_._image = feast_img
            feast_img_.place(x = 75,rely = 0.5,anchor = CENTER)
            CTkLabel(fr_feast,text = 'Breakfast and Lunch', font = ('HP Simplified',30)).place(x = 290,rely = 0.4,anchor = CENTER)
            CTkLabel(fr_feast,text = '$100 per night', font = ('HP Simplified',15)).place(x = 220,rely = 0.6,anchor = CENTER)
            feast_var = StringVar()
            checkbox_feast = CTkCheckBox(fr_feast,text = '',variable=feast_var, onvalue='yes', offvalue='no')
            checkbox_feast.place(relx = 0.95,rely = 0.5, anchor = CENTER)
            feast_img_.bind("<Button-1>", lambda x:checkbox_feast.toggle())
            fr_feast.bind("<Button-1>", lambda x:checkbox_feast.toggle())

            def back_sel():
                select_misc_.destroy()
                misc_back.destroy()
                misc_next.destroy()

            misc_back = CTkButton(booking_,height = 100,width = 100,text = '← Back', font = ('HP Simplified',17), command=lambda:back_sel())
            misc_back.place(relx = 0.15,rely = 0.5,anchor = CENTER)

            def show_details():
                show_details_ = CTkFrame(booking_,height = 540,width = 540,corner_radius=20)
                show_details_.place(relx = 0.5,rely = 0.5, anchor = CENTER)
                #--------------------show-details-of-booking--------------------
                CTkLabel(show_details_,corner_radius=20,text = 'Booking Summary:',font = ('Dubai',25,'bold')).place(relx = 0.5,rely = 0.1,anchor = CENTER)
                CTkLabel(show_details_,text = f"Checkin Date: {checkin_date.get()}",font = ('HP Simplified',17)).place(relx = 0.3,rely = 0.2, anchor = CENTER)
                CTkLabel(show_details_,text = f"Checkout Date: {checkout_date.get()}",font = ('HP Simplified',17)).place(relx = 0.3,rely = 0.3, anchor = CENTER)
                CTkLabel(show_details_,text = f"Number of Days: {diff}",font = ('HP Simplified',17)).place(relx = 0.3,rely = 0.4, anchor = CENTER)
                CTkLabel(show_details_,text = f"Type: {radio_var.get()}",font = ('HP Simplified',17)).place(relx = 0.75,rely = 0.2, anchor = CENTER)
                cur = sqlcon.cursor()
                cur.execute(f'select * from rooms where type = "{radio_var.get()}" and availability = "yes"')
                current_room = cur.fetchall()
                cur.close()  
                CTkLabel(show_details_,text = f"Room No: {current_room[0][0]}",font = ('HP Simplified',17)).place(relx = 0.75,rely = 0.3, anchor = CENTER)
                CTkLabel(show_details_,text = f"Price: ${current_room[0][3]}",font = ('HP Simplified',17)).place(relx = 0.75,rely = 0.4, anchor = CENTER)
                
                CTkLabel(show_details_,text = "Addons",font = ('HP Simplified',17,'bold')).place(relx = 0.3,rely = 0.55, anchor = CENTER)
                CTkLabel(show_details_,text = "Total",font = ('HP Simplified',17,'bold')).place(relx = 0.79,rely = 0.55, anchor = CENTER)
                




                addons_ = CTkFrame(show_details_,corner_radius=20,width = 300)
                addons_.place(relx = 0.3,rely = 0.77, anchor = CENTER)
                add0 = CTkLabel(addons_,text = '',font = ('HP Simplified',17))
                add0.place(relx = 0.5,rely = 0.25,anchor = CENTER)
                add1 = CTkLabel(addons_,text = '',font = ('HP Simplified',17))
                add1.place(relx = 0.5,rely = 0.5,anchor = CENTER)
                add2 = CTkLabel(addons_,text = '',font = ('HP Simplified',17))
                add2.place(relx = 0.5,rely = 0.75,anchor = CENTER)
                
                total = int(current_room[0][3])*diff
                addons = ['no','no','no']
                if transfer_var.get() == 'yes':
                    add0.configure(text = 'Airport Transfer')
                    total += 50
                    addons[0] = 'yes'
                    if tour_var.get() == 'yes':
                        add1.configure(text = "City Tour")
                        total += 170
                        addons[1] = 'yes'
                        if feast_var.get() == 'yes':
                            add2.configure(text = 'Breakfast and Lunch')
                            total += 100
                            addons[2] = 'yes'
                    elif feast_var.get() == 'yes':
                        add1.configure(text = 'Breakfast and Lunch')
                        total += 100
                        addons[2] = 'yes'
                elif tour_var.get() == 'yes':
                    add0.configure(text = 'City Tour')
                    total += 170
                    addons[1] = 'yes'
                    if feast_var.get() == 'yes':
                        add1.configure(text = 'Breakfast and Lunch')
                        total += 100
                        addons[2] = 'yes'
                elif feast_var.get() == 'yes':
                    add0.configure(text = 'Breakfast and Lunch')
                    total += 100
                    addons[2] = 'yes'
                else:
                    add1.configure(text = 'None')

                total_ = CTkFrame(show_details_,corner_radius=20)
                total_.place(relx = 0.79,rely = 0.77, anchor = CENTER)
                titl = CTkLabel(total_,text =f'${total}',font = ('HP Simplified',19,'bold'))
                titl.place(relx = 0.5,rely = 0.5,anchor = CENTER)

                def back_misc():
                    show_details_.destroy()
                    details_back.destroy()
                    proceed.destroy()

                details_back = CTkButton(booking_,height = 100,width = 100,text = '← Back', font = ('HP Simplified',17), command=lambda:back_misc())
                details_back.place(relx = 0.15,rely = 0.5,anchor = CENTER)

                def book():
                    #------------------PRINT-RECIPT------------------
                    def print_recipt():
                        sqlcon.commit()
                        cur = sqlcon.cursor()
                        cur.execute(f'select * from customers where cust_id = {login_details[0][0]}')
                        login_details.clear()
                        login_details.append(cur.fetchall()[0])

                        #-------------------ADD-RECIPT-PDF------------------
                        from PyPDF2 import PdfWriter, PdfReader
                        import io
                        from reportlab.pdfgen import canvas
                        from reportlab.lib.pagesizes import letter

                        packet = io.BytesIO()
                        can = canvas.Canvas(packet, pagesize=letter)
                        can.drawString(70, 700, f'Booking Id: {booking_details[0][0]}' )
                        can.drawString(350, 700, f'Customer Id: {booking_details[0][1]}' )
                        can.drawString(70, 670, f'Customer Name: {login_details[0][1]}') 
                        can.drawString(350, 670, f'Checkin Date: {booking_details[0][3]}' )
                        can.drawString(70, 640, f'No of days staying: {booking_details[0][5]}')
                        can.drawString(350, 640, f'Checkout Date: {booking_details[0][4]}' )
                        can.drawString(70, 610, f'Room No: {booking_details[0][2]}')
                        can.drawString(350, 610, f'Airport Transfer: {booking_details[0][7]}' )
                        can.drawString(70, 580, f'Type: {current_room[0][2]}')
                        can.drawString(350, 580, f'City Tour: {booking_details[0][8]}' )
                        can.drawString(70, 550, f'Total Price: {booking_details[0][6]}$')
                        can.drawString(350, 550,  f'Breakfast and Lunch: {booking_details[0][9]}')
                        can.drawString(270, 15,  'Thank You.!')
                        can.save()

                        packet.seek(0)

                        new_pdf = PdfReader(packet)

                        existing_pdf = PdfReader(open('assets/rec.pdf', 'rb'))
                        output = PdfWriter()

                        page = existing_pdf.pages[0]
                        page.merge_page(new_pdf.pages[0])
                        output.add_page(page)

                        output_stream = open(f'{booking_details[0][0]} Recipt.pdf', 'wb')
                        output.write(output_stream)
                        output_stream.close() 

                        CTkLabel(rec_,text = 'Thank You!',font = ('HP Simplified',27),width = 500,height = 200,corner_radius=30).place(relx = 0.5,rely = 0.5,anchor = CENTER)
                        
                        def closeall():
                            tabview.set('About')
                            show_details_.destroy()
                            select_misc_.destroy()
                            select_type_.destroy()
                            rec.destroy()
                            rec_.destroy()
                            price_type[0] = 'None'
                            checkout_date.configure(state='normal')
                            checkout_date.delete(0,10)
                            checkin_date.configure(state='normal')
                            checkin_date.delete(0,10)
                            err_msg0.configure(text = '')
                            next_misc_.destroy()
                            misc_next.destroy()
                            back_date_.destroy()
                            misc_back.destroy()
                            details_back.destroy()
                            proceed.destroy()
                            
                        CTkButton(rec_,text = 'Done',height = 50,width = 100, command=lambda:closeall()).place(relx = 0.5,rely = 0.75,anchor = CENTER)

                    def recload_stop():
                        progressbar.stop()
                        try:
                            cur = sqlcon.cursor()
                            cur.execute(f'update rooms set availability = "no" where room_no = {current_room[0][0]}')
                            cur.execute(f'insert into bookings(cust_id,room_no,checkin_date,checkout_date,no_stay,transfer,tour,feast,price) values({login_details[0][0]},{current_room[0][0]},"{checkin_date.get()}","{checkout_date.get()}",{diff},"{addons[0]}","{addons[1]}","{addons[2]}",{total})')
                            CTkLabel(rec_,height = 200,text = 'Room Booked Successfully!',font = ('HP Simplified',25,'bold')).place(relx = 0.5,rely = 0.5,anchor = CENTER)
                            cur.execute('select * from bookings order by booking_id desc limit 1')
                            det = cur.fetchall()[0]
                            booking_details.clear()
                            booking_details.append(det)
                            root.after(2000,lambda:print_recipt())
                            cur.close()
                        except:
                            CTkLabel(rec_,height = 200,text = 'Booking Failed', width = 520,font = ('HP Simplified',25,'bold')).place(relx = 0.5,rely = 0.5,anchor = CENTER)
                            root.after(2000,lambda:rec.destroy())

                    rec = CTkFrame(booking_,height = 590,width = 1422,corner_radius=30)
                    rec.place(relheight = 1, relwidth = 1, relx = 0.5,rely = 0.5, anchor = CENTER)

                    recpic = CTkLabel(rec,text = '', image = backdrop)
                    recpic._image = backdrop
                    recpic.place(relx = 0.5,rely = 0.5,anchor = CENTER)

                    rec_ = CTkFrame(booking_,height = 520,width = 540,corner_radius=30)
                    rec_.place(relx = 0.5,rely = 0.5, anchor = CENTER)

                    progressbar = CTkProgressBar(rec_,height = 50,mode="indeterminate")
                    progressbar.place(relx = 0.5,rely = 0.5, anchor = CENTER)
                    CTkLabel(rec_,text = 'Booking...',font = ('HP Simplified',20,'bold')).place(relx = 0.5,rely = 0.6,anchor = CENTER)
                    progressbar.start()

                    root.after(3000,lambda:recload_stop())
                
                def showsignin():
                    req = CTkFrame(root, width = 1280, height = 720)
                    req.place(relheight = 1, relwidth = 1, relx = 0.5,rely = 0.5, anchor = CENTER)

                    bottompic2 = CTkImage(Image.open('assets/loginbg.png'),size = (1920,1080))
                    bpic2 = CTkLabel(req,text = '', image = bottompic2)
                    bpic2._image = bottompic2
                    bpic2.place(relx = 0.5,rely = 0.5,anchor = CENTER)

                    signupreq = CTkFrame(req,height = 620,width = 540,corner_radius=20)
                    signupreq.place(relx = 0.5,rely = 0.5, anchor = CENTER)

                    CTkLabel(signupreq,corner_radius=20,text = 'Please Log In',font = ('HP Simplified',25,'bold')).place(relx = 0.5,rely = 0.5,anchor = CENTER)

                    root.after(2000,lambda:req.destroy())

                proceed = CTkButton(booking_,height = 100,width = 100,text = 'Book', font = ('HP Simplified',17), command=lambda:book() if loggedin[0] is True else showsignin())
                proceed.place(relx = 0.85,rely = 0.5,anchor = CENTER)

            misc_next = CTkButton(booking_,height = 100,width = 100,text = 'Done →', font = ('HP Simplified',17), command=lambda:show_details())
            misc_next.place(relx = 0.85,rely = 0.5,anchor = CENTER)

        next_misc_ = CTkButton(booking_,height = 100,width = 100,text = 'Next →', font = ('HP Simplified',17), command=lambda:select_misc() if radio_var.get() != '' else err_msg1.configure(text = '*Please select an Option!*'))
        next_misc_.place(relx = 0.85,rely = 0.5,anchor = CENTER)   

    root.mainloop()

if __name__ == '__main__':
    set_appearance_mode('dark')
    set_default_color_theme('green')

    loggedin = [False]
    login_details = []
    booking_details = []

    today = dt.today().strftime('%Y-%m-%d')
    
    sqlcon = msconn.connect(host = 'localhost', user = 'root', passwd = 'samy', database = 'hotel0')
    mainapp()
    sqlcon.close()